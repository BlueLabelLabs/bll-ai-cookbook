
# WhatsApp Chat Analysis with Pinecone and OpenAI

This Jupyter notebook allows you to analyze WhatsApp chat logs using Pinecone and OpenAI. It loads chat data from a directory, processes it, and then uses OpenAI embeddings to generate conversational responses based on the chat context.

## Prerequisites

1.  **Python**: Ensure you have Python installed. This notebook was developed using Python 3.x.
    
2.  **Jupyter Notebook**: If you haven't already, you'll need to install Jupyter. You can do this using pip:
    
    `pip install jupyter` 
    
3.  **Dependencies**: Before running the notebook, you need to install the required Python libraries. You can do this using pip:
    
    `pip install os dotenv pinecone langchain` 
    
4.  **Data Folder**: Place your WhatsApp chat logs in a folder named `data/` in the same directory as the notebook. The chat logs should be in `.txt` format.
    
5.  **Environment Variables**: Create a `.env` file in the same directory as the notebook. This file should contain the following constants:
        
    ```
    OPENAI_API_KEY=your_openai_api_key
    PINECONE_API_KEY=your_pinecone_api_key
    PINECONE_ENV=your_pinecone_environment
    ```
    
    Replace `your_openai_api_key`, `your_pinecone_api_key`, and `your_pinecone_environment` with your actual keys and environment details.
    
## Running the Notebook

1.  Navigate to the directory containing the notebook using the terminal or command prompt.
    
2.  Launch Jupyter Notebook:
    
    `jupyter notebook` 
    
3.  In the Jupyter dashboard that opens in your browser, click on the notebook file (with `.ipynb` extension) to open it.
    
4.  Run the cells in the notebook sequentially by selecting each cell and pressing `Shift + Enter`.
    
5.  The notebook will process the chat logs, connect to Pinecone, and generate a conversational response based on a predefined query. The result will be displayed within the notebook.
    
## Notes

-   Ensure that the `data/` folder contains valid WhatsApp chat logs in `.txt` format.
-   The `.env` file should be kept secure as it contains sensitive API keys.
-   The notebook uses OpenAI embeddings, so ensure you have the necessary permissions and quota on OpenAI to run it without issues.