# BlueLabel AI Cookbook
This repository contains a set of Jupyter notebooks created by the [BlueLabel](https://bluelabellabs.com) engineering team that demonstrate how to use Large Language Models (LLM) and their associated APIs and toolchains to create tools that solve a variety of common app development, content creation and marketing tasks. The tools demonstrated in this cookbook are done in the form of Jupyter notebooks, however to see how they work in the real-world you can browse the [BlueLabel AI Toolbox](https://www.bluelabellabs.com/ai) where you can find a variety of publically available tools that leverage the functionality demonstrated within these notebooks.  

Each folder in the repository represents a separate tool and within it you will find a README.md file describing its purpose and how to run it. While this cookbook only contains Jupyter notebooks, some of these tools also have their own source code repositories where the complete source code for them can be found.

## App Store Connect Metadata Generator
The [App Store Connect Metadata Generator](https://github.com/bll-bobbygill/bll-ai-cookbook/tree/main/appstore-connect-info-generator) demonstrates how to use LangChain and ChatGPT to automate the creation of a full set of Apple App Store metadata when simply given a name, category and functionality. You can try out this tool on the [BlueLabel AI Toolbox](https://www.bluelabellabs.com/ai/appstore-metadata-generator).

## Notification Tactician
The [Notification Tactician](https://github.com/BlueLabelLabs/bll-ai-cookbook/tree/main/notification-matrix-generator) aims to simplify the development and optimization of a push notification strategy for a mobile app. By using GPT-4 and aligning with OneSignal best practices, the tool will automatically produce a push-notification matrix outlining optimal notification parameters for different user segments. You can try out this tool on the [BlueLabel AI Toolbox](https://www.bluelabellabs.com/ai/#ai-toolbox).

## Product Analytics Architect
The Product Analytics Architect uses GPT-4 to generate a list of in-app analytics events for a mobile app based on the provided product description, app category, product features, special app features, target audience, and tone of voice. You can try out this tool on the [BlueLabel AI Toolbox](https://www.bluelabellabs.com/ai/#ai-toolbox).

## North Star Metric Generator
The [North Star Metric Generator](https://github.com/BlueLabelLabs/bll-ai-cookbook/tree/main/north-star-metric-tool) is designed to guide users in creating a ["North Star Metric"](https://amplitude.com/blog/product-north-star-metric) and associated input metrics, aligning with the product's core value proposition, user engagement, and expected impacts. The tool will utilize a model trained with GPT-4, utilizing insights from the ["Amplitude North Star Playbook"](https://info.amplitude.com/rs/138-CDN-550/images/Amplitude-The-North-Star-Playbook.pdf) to generate relevant and aligned metrics.. You can try out this tool on the [BlueLabel AI Toolbox](https://www.bluelabellabs.com/ai/#ai-toolbox).

## Instagram Post Classifier
The [Instagram Post Classifier](https://github.com/BlueLabelLabs/bll-ai-cookbook/tree/main/instagram-classifier) demonstrates how to classify a large data set of Instagram post captions into a set of normalized, unique topics that can then be fed into an LLM to do content creation for a blog. Read more about how we used LangChain's MapReduce to tackle this problem in conjuction with GPT-4 in this post on the [BlueLabel blog](https://www.bluelabellabs.com/blog/how-to-use-langchain-and-mapreduce/).

## Instagram Reel -> YouTube Short Title Converter
The [Instagram Reel -> YouTube Short Title Converter](https://github.com/BlueLabelLabs/bll-ai-cookbook/tree/main/instagram-reel-to-youtube-short-converter) demonstrates how to use GPT with Langchain to take Instagram Reel captions and create snappy YouTube Short Titles that are engaging and also relevant to the content it is trying to describe.

## AutoTweeter
The [AutoTweeter](https://github.com/bll-bobbygill/bll-ai-cookbook/tree/main/auto-tweeter) notebook demonstrates how to use ChatGPT, LangChain, and Reddit to fully automate research and creation of content for a user's Twitter feed. Read more about how this tool works in this post on the [BlueLabel blog](https://www.bluelabellabs.com/blog/autotweeter-langchain-gpt4-ai-twitter-bot/).

## WhatsApp Chat Analysis
The [WhatsApp Chat Analysis](https://github.com/bll-bobbygill/bll-ai-cookbook/tree/main/whatsapp-chat-analysis) project shows how LangChain can be used to ingest a WhatsApp chat history and use that history to generate responses to new messages in the same tone as the sender of messages in the history.