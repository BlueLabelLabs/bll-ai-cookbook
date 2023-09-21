# Instagram Post Classifier
This notebook demonstrates how to use LangChain's MapReduceDocumentChain to output a global set of "topics" that describe the content contained within the Instagram captions.

# Goal
The goal of this notebook is to use an LLM such as GPT-4 to create a global list of "topics" which describe the content contained within all of the Instagram Post captions that it is run against. 

For instance, this notebook is designed to analyze the complete post history of a Instagram influencer who is a Reproductive Endocrinologist and who has an extensive history of posts containing captions that are essays on a wide ranging set of fertility, reproductive health and medical issues. This notebook demonstrates how these posts can be analyzed to create a global set of topics that can then be used as classifications attached to each individual post (this second part is beyond the scope of this notebook).

# How It Works
The challenge in creating this global classification is that each post caption can be hundreds of words long and there are hundreds of Instagram posts to analyze. Attempting to process this in a single shot with an LLM would very quickly overrun the input token limit. 

To solve this problem a MapReduceDocumentChain is used where by:
- "Map" Step: Analyzes each post caption and derives a local set of classifications related to fertility and reproductive health.
- "Reduce" Step: The output of all of the "map" steps run across each caption are then brought together and unified to eliminate any duplicates and collapse similar classifications into one.

The output of the MapReduceDocumentChain is then passed to a separate LLMChain instance which then performs one more collapse step whereby it compares the final set of new "topics" generated against a set of already defined "topics" that were read in at the start of the run. Finally, it updates to file the new set of global "topics" to a CSV file.

# Pre-Requisites
To run this sample you will need:
- An OpenAI API key.
- A free account with PromptLayer and an API key to use for tracing.


