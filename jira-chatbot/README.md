# Jira Chatbot

This Jupyter Notebook demonstrates the implementation of an AI-powered chatbot tailored for app development support. The chatbot utilizes state-of-the-art language models and integrates with Pinecone, an advanced vector search platform. It assists in answering user queries related to mobile app projects, provides information on project status, and offers guidance on common tasks and known issues. The chatbot is equipped with natural language processing capabilities and can access a set of JIRA tickets to provide context and relevant information. It also supports multi-step conversations with history tracking. The notebook offers an interactive chat loop where you can engage with the chatbot and receive real-time responses, making it a valuable tool for enhancing productivity and client engagement in your digital agency's app development projects.

## Goal

The goal of this AI-powered chatbot for app development support is to streamline and enhance the app development process within your digital agency. It aims to provide efficient and intelligent support to both your development team and clients by answering questions, offering project insights, and assisting with common tasks and known issues.

## How It Works

1. **User Interaction**: The chatbot interacts with users through a chat interface. Users can input questions, requests, or seek assistance related to app development projects.
2. **Contextual Understanding**: The chatbot starts by providing context about its role and the available information from JIRA tickets. It understands user queries and maintains a conversation history to provide meaningful responses.
3. **Access to JIRA Data**: The chatbot leverages Pinecone, a vector search platform, to access and search through JIRA tickets. It extracts relevant information from the tickets to support user queries.
4. **Natural Language Processing (NLP)**: Using state-of-the-art NLP techniques and OpenAI language models, the chatbot interprets and generates human-like responses to user inputs.
5. **Assistance and Recommendations**: The chatbot assists users by answering questions, providing project status updates, suggesting solutions to known issues, and offering guidance on common tasks.
6. **Multi-Step Conversations**: The chatbot maintains a conversation history, allowing users to engage in multi-step conversations. It tracks chat history for continuity and context awareness.

## Requirements

By following these steps, you can retrieve JIRA tickets in CSV format and make them accessible for use in your chatbot script. The CSV file will serve as the source of JIRA ticket data that the chatbot uses to provide context and information during conversations.

1. **Access JIRA**
   - Log in to your JIRA account or access your organization's JIRA instance.

2. **Create a Filter (if needed)**
   - If you have specific criteria for the tickets you want to export, create a filter in JIRA that includes the desired tickets. Filters allow you to define conditions such as project, status, issue type, etc.
   - Go to the "Issues" dropdown menu.
   - Select "Search for issues."
   - Use the JQL (JIRA Query Language) to create a filter that matches your criteria.
   - Save the filter with a meaningful name.

3. **Export to CSV**
   - Once you have the filter or have located the tickets you want to export:
   - Run the filter or select the tickets.
   - Click on the "Export" option, typically found in the upper right or under the "More" dropdown menu.
   - Choose the export format as "CSV."

4. **Customize Export Fields (Optional)**
   - JIRA may offer options to customize the fields you want to include in the CSV export. Select the fields that are relevant to your chatbot's requirements. Common fields include "Summary," "Assignee," "Status," "Issue Type," and "Description."

5. **Export and Save**
   - Click the "Export" or "Generate" button to initiate the export process. The system will generate a CSV file containing the ticket data.

6. **Save the CSV File**
   - Once the CSV file is generated, save it to a location on your local machine or server where it can be accessed by your chatbot script. Ensure that you have a consistent and known file path for the CSV file to be read by the script.

7. **Provide Access**
   - If your JIRA instance requires authentication or access permissions, ensure that the account running the chatbot script has the necessary access rights to retrieve the CSV file from the specified location.