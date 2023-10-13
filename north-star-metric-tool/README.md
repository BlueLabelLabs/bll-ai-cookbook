# Notifications Matrix Generator

This tool enables the automated generation of North Star Metrics and supporting input metrics, tailored according to user inputs such as user role, product category, core value proposition, leading indicator of value, and expected user engagement. It harnesses the capabilities of OpenAI's GPT model and the Langchain library, utilizing the PromptLayer API for enhanced predictability and response generation.

## Goal

The primary objective of this tool is to simplify and automate the process of identifying a North Star Metric and its supporting metrics, essential for product growth and improvement. Users can leverage this tool to derive metrics that resonate with user engagement, value realization, and strategic alignment, customized based on specific product attributes and user roles.

## How It Works

1. **User Inputs**: The user interacts with a graphical interface to input various parameters such as user role, product category, core value proposition, leading indicator of value, and expected user engagement.
2. **Template Configuration and Prompt Generation**: Based on user inputs, a prompt is dynamically created, integrating predefined templates and playbook contexts, ready to be processed by the language model.
3. **Language Model Interaction**: The crafted prompt is processed by OpenAI’s GPT model through the Langchain library and the PromptLayer API, generating a response that includes potential North Star Metrics and input metrics.
4. **Response Presentation**: The generated metrics, including the North Star Metric and the supporting metrics, are presented in a structured format, enabling users to analyze, utilize, and implement them in their strategic planning.

## Requirements

- OpenAI API key for interacting with the GPT model.
- PromptLayer API key
- Properly set up environment variables, including API keys and other configurations