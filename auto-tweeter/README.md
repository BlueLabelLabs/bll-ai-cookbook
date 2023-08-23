# AutoTweeter - Generate Tweets Using Reddit and LangChain
This notebook demonstrates a mechanism by which you can automate the creation of new content for a Twitter user's Twitter feed using content that is created purely by an LLM AI trained on that user's Tweet history and using Reddit as a source for new topics to Tweet about. This notebook utilizes the Reddit API, an in-memory vector database and LangChain SequentialChain to create a content generation pipeline.

This notebook demonstrates the core concepts that power the [AutoTwitter AI](https://github.com/bll-bobbygill/AutoTweeter) solution whose source code can be found on [GitHub](https://github.com/bll-bobbygill/AutoTweeter)

For a full outline on how the AutoTweeter AI content generation pipeline works, please read: ["AutoTweeter: How I Used LangChain, GPT-4 and AWS Lambda to Put AI in Control of My Twitter Feed"](https://bluelabellabs.com/autotweeter-langchain-gpt4-ai-twitter-bot)

## Pre-requisites
- Register a Reddit app [here](https://ssl.reddit.com/prefs/apps/) 
    - Set it up as a "Personal Use Script"
    - Note down the ClientID and ClientSecret (which will be emailed to you)
- Register for an [OpenAI API Key](https://platform.openai.com/account/api-keys) and API access to GPT-4 model. Ensure you have an environment variable set for OPENAI_API_KEY with this key.
- Setup a PromptLayer API key [here](https://promptlayer.com/home). PromptLayer is a free tool that gives you a very easy way to visually debug prompts sent to an LLM
- Obtain a CSV dump of the Tweet history for the Twitter user account you are looking to automate, follow the instructions [here](https://help.twitter.com/en/managing-your-account/how-to-download-your-twitter-archive). Copy this CSV into the root of this folder.

## Dependencies
This notebook requires Python 3.10

Prior to running the notebook, install all necessary Python dependencies:
```
pip install -r requirements.txt
```

## Setup
Replace the values in the Paramters node of the AutoTweeter.ipynb notebook with the values for the Reddit App, PromptLayer API Key and filename of Twitter data export.
```Python
#Register for a Reddit app API key and input the CLIENT_ID and CLIENT_SECRET here
REDDIT_CLIENT_ID='<REDDIT_CLIENT_ID>'
REDDIT_CLIENT_SECRET='<REDDIT_CLIENT_SECRET>'

#Download your Twitter archive data export and copy the CSV into the same folder as this notebook.
#See here for instructions on how to obtain it: https://help.twitter.com/en/managing-your-account/how-to-download-your-twitter-archive
TWEET_ARCHIVE_CSV_FILE='<TWITTER DATA EXPORT>.csv'

promptlayer.api_key = "<PROMPTLAYER API KEY>"
```