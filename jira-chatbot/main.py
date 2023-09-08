import os
from dotenv import load_dotenv
import csv
import pinecone
from langchain.chains import LLMChain
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.memory import ConversationBufferMemory
import gradio as gr

# Load environment variables from .env file
load_dotenv()

# Get OpenAI, Pinecone API keys from environment variables
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
PINECONE_ENV = os.environ.get("PINECONE_ENV")

# Connect to Pinecone
pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)

index_name = "jira-demo"

# Create embeddings
embeddings = OpenAIEmbeddings()


def convert_row_to_sentence(row):
    """Converts a row from a CSV file to a sentence."""
    sentence = "The ticket {} that is a {}, is asigned to {}, it is currently {} and has the following description: {}".format(
        row["Summary"], row["\ufeffIssue Type"], row["Assignee"], row["Status"], row["Description"]
    )
    return sentence

# Add a parameter to your function, e.g. force_recreate


def create_or_load_index(index_name, force_recreate=False):
    if force_recreate and index_name in pinecone.list_indexes():
        # If we need to force recreate, and the index already exists, delete it
        pinecone.delete_index(index_name)

    if index_name not in pinecone.list_indexes():
        # Now we create the index if it doesn't exist (or if we just deleted it)
        pinecone.create_index(
            name=index_name,
            metric='cosine',
            dimension=1536
        )

        print("Loading data...")

        # Load and parse data
        with open("./data/data.csv", encoding='utf-8') as f:
            reader = csv.DictReader(f)
            texts = []
            for row in reader:
                sentence = convert_row_to_sentence(row)
                texts.append(sentence)

        # Initialize Pinecone vector store
        vectorstore = Pinecone.from_texts(
            texts, embeddings, index_name=index_name)
    else:
        # Initialize Pinecone vector store
        vectorstore = Pinecone.from_existing_index(index_name, embeddings)

    return vectorstore


# Now we can use our function, e.g. with force_recreate=True if we want to regenerate the index
vectorstore = create_or_load_index(index_name, force_recreate=False)

# If we pass in a model explicitly, we need to make sure it supports the OpenAI function-calling API.
llm = ChatOpenAI(model="gpt-4", temperature=.7)

print("Chatbot is ready to chat!")

prompt_msgs = [
    SystemMessage(
        content="You are a support assistant that provides end-user support for a mobile app project called \"Hyer\". Your role is to help answer user questions about the functionality of the app as well as to help them complete common tasks in the app as well troubleshoot known issues."
    ),
    SystemMessage(
        content="You are provided as context a set of JIRA tickets that might be relevant to the user's question. JIRA tickets were IssueType is Task or Story describe the intended behavior of the app. JIRA tickets that have IssueType of Bug are known defects in the app."
    ),
    SystemMessagePromptTemplate.from_template("{context}"),
    SystemMessage(content="Tip: JIRA tickets that have a Status of Done should already be present in app. For JIRA tickets that are Bugs and are not Done, they also may contain steps to workaround the issue.."),
    SystemMessage(content="Tip: If you don't know the answer, you can reply with 'This seems to be an uknown issue, please report it to the project manager.'. Don't try to make up an answer."),
    SystemMessage(
        content="History:"
    ),
    SystemMessagePromptTemplate.from_template("{chat_history}"),
    HumanMessage(
        content="Message:"
    ),
    HumanMessagePromptTemplate.from_template("{input}"),
]
prompt = ChatPromptTemplate(
    messages=prompt_msgs, input_variables=["context", "input", "chat_history"]
)

memory = ConversationBufferMemory(memory_key="chat_history", input_key="input")
chain = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
    memory=memory,
)

def predict(message, history):
    # Search for relevant tickets
    result = vectorstore.similarity_search(message)

    prompt.format(context=result[0].page_content, input=message, chat_history=history)

    response = chain.run(input=message, context=result[0].page_content, chat_history=history)

    return response

CSS ="""
.contain { display: flex; flex-direction: column; }
.gradio-container { height: 100vh !important; }
#component-0 { height: 100%; }
#component-2 { height: 100% !important; }
#chatbot { flex-grow: 1; overflow: auto;}
"""

gr.ChatInterface(predict, css=CSS).launch(server_name="0.0.0.0", server_port=7860)
