import os
import openai
import json

# Initialize OpenAI API key
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

# Fetch the available models
models_data = openai.Model.list()
model_names = [
    model.id for model in models_data.data if model.id.startswith('gpt-')]


def generate_app_description(event, context):
    data = json.loads(event['body'])
    selected_model = data.get('selected_model', model_names[0])
    category = data.get('category', '')
    purpose_statement = data.get('purpose_statement', '')
    features = data.get('features', '')
    working_name = data.get('working_name', None)

    conversation = [
        {"role": "system", "content": "You are an assistant that will help me submit my new app idea to the App Store. I need specific information about my app to submit it. Here are some notes to keep track of"},
        {"role": "system", "content": "The title should be quirky and fun. The description should be a 3 paragraph summary of the purpose_statement and features, written in a fun, exciting, and descriptive way."},
        {"role": "system",
            "content": "Output should be in JSON. It should be a single object with the following keys: choices: [{ name, description }] (2 choices), category, and keywords[] (10). The name should be a string, the description should be a string, the category should be a string, and the keywords should be an array of strings."},
        {"role": "system",
            "content": "Output should be in JSON. It should be a single object with the following keys: choices: [{ name, description }] (2 choices), category, and keywords[] (10). The name should be a string, the description should be a string, the category should be a string, and the keywords should be an array of strings."},
        {"role": "system", "content": "The description should be several paragraphs containing an overview, features, and benefits."},
        {"role": "user", "content": f"I want to create a mobile app that falls under the category of {category}. The main purpose of this app is: {purpose_statement}."},
        {"role": "user", "content": f"The features of the app include: {features}."}
    ]

    response = openai.ChatCompletion.create(
        model=selected_model,
        messages=conversation,
        temperature=0.7,
    )

    app_description = response.choices[0].message['content']
    app_description = app_description.split('\n\nFor the output format,')[0]

    response_json = {
        "choices": [
            {
                "name": working_name,
                "description": app_description
            }
        ],
        "category": category,
        "keywords": features.split(', ')
    }

    return {
        'statusCode': 200,
        'body': json.dumps(response_json)
    }
