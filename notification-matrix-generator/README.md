# Notifications Matrix Generator

This notebook provides a way to generate notification strategies based on various parameters like app category, product features, special app features, target audience, and tone of voice. It leverages the power of OpenAI's GPT model and the PromptLayer API to generate these strategies.

## Goal

The primary goal of this notebook is to automate the process of creating notification strategies tailored to specific user segments and business goals. By inputting specific parameters, users can obtain a matrix of notifications that are optimized for engagement, retention, and user satisfaction.

## How It Works

1. **Input Parameters**: The user provides input parameters such as the app category, product features, special app features, target audience, and tone of voice.
2. **LLM Model Call**: The provided parameters are used to generate a prompt that is then passed to the OpenAI GPT model via the PromptLayer API.
3. **Response Parsing**: The response from the model is parsed to extract relevant notification strategies.
4. **Output**: A matrix of notifications is generated, detailing the user segment, notification type, business goal, timing rule, generated message, and justification for each strategy.

## Requirements

- OpenAI API key
- PromptLayer API key
