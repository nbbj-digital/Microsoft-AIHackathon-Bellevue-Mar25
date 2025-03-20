# 🏆 Challenge 04: Setting Up LLMs for a Chatbot and its Dependencies

## 📖 Learning Objectives
Retrieval Augmented Generation (RAG) is a technique used to **build chat-based applications** that leverage custom data to generate more **factual, relevant** responses. Instead of relying solely on a model’s pre-training, RAG retrieves **grounding data** from your own data store (for example, Azure AI Search) and **augments** the prompt with that data. In this challenge, you’ll use **Azure AI Foundry** to orchestrate these steps.

By completing this challenge, you'll be able to:

- **Identify** the need to ground your language model with RAG  
- **Index** your data with **Azure AI Search** to make it searchable for language models  
- **Build** an AI agent on your own data in the **Azure AI Foundry portal**  
- **Create** a **prompt flow** to maintain **chat history**  
- **Retain** conversation context so the chatbot can respond accordingly in multi-round conversations  

---

## ⚙️ Prerequisites
Before starting, ensure you have:

- **Familiarity** with fundamental AI/ML concepts in Azure.  
- **Permissions** to create an Azure AI Foundry hub (or have one created for you).  
- **Azure roles**: If your role is **Contributor** or **Owner**, you can follow these steps. If your role is **Azure AI Developer**, the hub must already be created, and your user role must be **Azure AI Developer, Contributor, or Owner** on that hub.

[Check this for more information](https://microsoft.github.io/AI-For-Beginners/)

---

## 🏆 Challenge Overview


✅ Create, Define, and Explore LLMs for a Chatbot and the Resources Needed to Set Up the Same.  

✅ Add Custom Data to Your Project and Explore the Response of Chatbot Post Indexing and Grounding.  

✅ Build & Customize – Create, Iterate, and Debug Your Orchestration Flows.

✅ Learn how to use frameworks to programatically create AI agents and achive tailormade solutions for complex use cases with more flexiblity


Milestones High Level :
### Milestone #1: **Create, Define, and Explore** LLMs + Resources
1. **Create** your Resource Group, Key Vault, Azure Storage, Azure AI Service, and Azure AI Search.
2. **Set up** an AI Foundry **Hub** and **Project**.
3. **Deploy** two models: an **embedding** model (e.g., `text-embedding-ada-002`) and a **chat** model (e.g., `gpt-35-turbo-16k`).
4. **Test** your chatbot in the **playground** with simple questions.

### Milestone #2: **Add Data** to Your Project and **Ground** the Chatbot
1. **Enable Managed Identity** and **assign roles** for your AI service, AI Search, and storage.
2. **Create** connections in the AI Foundry (ml.azure.com or ai.azure.com).
3. **Index** your data with **Azure AI Search**.
4. **Attach** that index to your chat model so it uses your **custom data** to respond.

### Milestone #3: **Build & Customize** – Prompt Flow with Orchestration
1. **Clone** the “Multi-Round Q&A on Your Data” sample.
2. **Incorporate** your vector index to retrieve relevant info.
3. **Deploy** a **prompt flow** endpoint that retains chat history.
4. **Test** multi-turn Q&A that references your data.

### Milestone #4: **Advanced** – Query Multiple CSV Files with Langchain + Azure OpenAI
1. **Create** or verify your **Azure OpenAI** resource for `gpt-35-turbo-instruct`.
2. **Combine** multiple CSVs into one local CSV (or manage them individually).
3. **Use** `create_csv_agent` in Python to ask structured queries in plain English.
4. **Achieve** more complex or SQL-like queries without memorizing syntax.
---

## 🚀 Generic TIPS:

- Try to keep all resources and RG in the same Region for ease of understanding and standardization.
- Most companies have organizational policies on auto-creation of Key Vault & Storage account, so here we will be creating all resources separately and will stitch them together.
- Add a tag to the Resources and resource group when you create them so that we can identify them later for cost management or other aspects.
- Ensure that all necessary resource providers are registered. For example, you might need to register Microsoft.PolicyInsights and Microsoft.Cdn policies by selecting them and clicking the register button in the Azure Portal.
- Make sure the location or region for each of the resources is preferably one of the following, to ensure smooth testing of all resources:
  - Australia East
  - Canada East
  - East US
  - East US 2
  - France Central
  - Japan East
  - North Central US
  - Sweden Central
  - Switzerland
- Check the TPM quota for your subscription for the LLMs `text-embedding-ada-002` and `gpt-35-turbo-16k` and `gpt-35-turbo-instruct`. If you are already familiar with the same, request a quota addition if the current quota is in the 2-digit range (10k–90k) and increase it to whatever is maximum for each model.

---

## 🚀 Milestone #1: Create, Define, and Explore LLMs for a Chatbot and the Resources Needed to Set Up the Same

### 1️⃣ Create the Resource Group (RG)
### 2️⃣ Create/Use the existing Storage account (this will be source of our custom data)
**TIP**: The source of your data can be Fabric or Data Lake Gen2 from the previous challenges, but that will involve some additional steps to fulfill and might require some extra efforts to set the same up.  
Since we are time-bound, we will just use the Dimension Xls (which will be converted to csv/txt here) for the purpose of this challenge. If you were able to successfully finish the first 3 challenges, you already have 3 Dim xls files with you in Fabric Lakehouse and can convert the files to CSV (using a dataflow to transform, then a data copy pipeline to copy from Fabric to the new storage account) and upload them into the storage account we are going to create below.

First, use a dataflow Gen2 transformation on the files.  
Second step is to convert the transformed files to csv using the snippet in a notebook:

Once the storage account is created, create a container `refined-data` and upload all four CSV files into the container (inside a folder named `csv-data` or `txt-data`). By the end of this step, you will have:
   - A **storage account** with a **container** inside
   - A **subfolder** in that container
   - All the files in CSV format inside that subfolder
For ease of data transfer we have the same copied under the path "Data Sources/csv_data" you can just upload the folder to the container you just created 


### 3️⃣ Create the Key Vault
### 4️⃣ Create a Search Service Connection to Index the Sample Product Data
### 5️⃣ Create an Azure AI Service
**Remarks**: By now, you have everything needed (Hub, Project) in **AI Foundry**.
### 6️⃣ Create a Hub
### 7️⃣ Create a Project once the Hub is completed 

**Remarks**: This shouldn’t take more than 20 minutes. Once done, head to [https://ai.azure.com](https://ai.azure.com). Choose your project, and we’ll proceed inside that environment.

**TIP**: With no organizational constraints, you can sign up at [https://ai.azure.com](https://ai.azure.com) and create the project directly. All other resources will be created automatically. You just need an AI search service resource.

### 8️⃣ Deploy Models

You need two models:
- **An embedding model** (text-embedding-ada-002)
- **A generative model** (like gpt-35-turbo-16k)

1) In **Azure AI Foundry**, open your **project** → **My assets** → **Models + endpoints**.
2) **New deployment** of `text-embedding-ada-002` (click **Customize**):
   - **Deployment name**: `text-embedding-ada-002`
   - **Type**: Standard
   - **Model version**: default
   - **AI resource**: the one you created
   - **Tokens per Minute**: max
   - **Content filter**: DefaultV2
   - **Enable dynamic quota**: optional  
   > If insufficient quota, you’ll be asked to choose a different location; a new AI resource will be created.

3) **Repeat** the deployment for `gpt-35-turbo-16k` under the name `gpt-35-turbo-16k`.
4) **Select** `gpt-35-turbo-16k` → **Open in playground**.
5) Test with “What do you do?” to see the default response.
6) **Now change** instructions/context:

![Model Instructions](https://github.com/DavidArayaS/AI-Powered-Insights-Fraud-Detection-Hackathon/blob/7b4a95aa515d6cea3bffc4253b32ac0981bb527a/04-AI%20Chatbot/Reference%20Pictures/model9.png)

**Objective**: Provide financial advice as a knowledgeable advisor.

**Capabilities**:
- Market trends, investment options, financial products
- Personalized advice (risk tolerance, financial goals)
- Budgeting, saving, risk management tips
- Financial planning: retirement, tax strategies, wealth management
- Answers to common financial Qs, solutions to issues

**Instructions**:
1) Engage as a friendly, professional financial advisor
2) Use resources for accurate info
3) Tailor responses to specific needs
4) Be practical and consider safety
5) Encourage follow-up questions

7) **Apply changes**.
8) **Test the chatbot** with the question “What do you do?” to see a context-specific response. Notably, if you asked the same question before updating the context, the answer would have been more generic.

## 🚀 Milestone #1: Result

---
You can test the model by opening the **playground** and chatting with it. Ask some generic questions, and you’ll get generic answers. At this point, the model is looking for data it was originally trained on and is **not yet grounded** in **your custom data**. However, we did manage to tailor the instructions and context to yield more specific responses.

---

## 🚀 Milestone #2: Add Data to Your Project and Explore the Response of the Chatbot Post Indexing and Grounding

1. **Enable Managed Identity**  
   - **(a)** Enable **Managed Identity (MI)** for both the **AI service** and the **AI search service**.  
   - **(b)** In the **Search service** resource (in the Azure portal):  
     1. Go to **Settings** → **Identity**  
     2. Switch **Status** to **On**  
     3. Select **Save**  
   - **(c)** In the **Azure AI services** resource (in the Azure portal):  
     1. Go to **Resource Management** → **Identity**  
     2. Switch **Status** to **On**  
     3. Select **Save**

2. **Set API Access Control for Search**  
   - **(a)** In the **Search service** resource (in the Azure portal):  
     1. Go to **Settings** → **Keys**  
     2. Under **API Access control**, select **Both**  
     3. When prompted, select **Yes** to confirm

3. **Assign Roles**  
   - **(a)** The general pattern for assigning role-based access control (RBAC) is:  
     1. In the **Azure portal**, open the relevant resource  
     2. Select **Access control (IAM)** from the left pane  
     3. Click **+ Add > Add role assignment**  
     4. Search for the role, select it, then **Next**  
     5. When assigning a role to yourself:
        - Choose **User, group, or service principal**
        - **Select members**
        - Search for your name, select it
     6. When assigning a role to another resource:
        - Choose **Managed identity**
        - **Select members**
        - Pick the target resource type (e.g., Azure AI services or Search service)
        - Select your resource from the list
     7. Click **Review + assign** to finalize  
   - **(b)** Use these steps for each resource in this tutorial:
     1. **Search service** (Azure portal):
        - **Search Index Data Reader** → Azure AI services managed identity  
        - **Search Service Contributor** → Azure AI services managed identity  
        - **Contributor** → yourself (switch to **Privileged administrator roles** if needed)
     2. **Azure AI services** (Azure portal):
        - **Cognitive Services OpenAI Contributor** → Search service managed identity  
        - **Contributor** → yourself (if not already)
     3. **Azure Blob storage** (Azure portal):
        - **Storage Blob Data Contributor** → Azure AI services managed identity & Azure AI services managed identity  
        - **Contributor** → yourself (if not already)

   > **TIP**: If you’re using identity-based authentication, **Storage Blob Data Contributor**, **Storage File Privileged Contributor** (inside Storage account), and **Cognitive Services OpenAI Contributor** (inside AI services) must be assigned to any user or managed identity needing storage access.

4. **Storage Account Datastore Configuration**  
### 5. Create Connections to the Blob Storage & AI Search
### 6. Add the Custom Data to AI Foundry
> **TIP**: Click **job details** to see the indexing job in [https://ml.azure.com](https://ml.azure.com). Times may vary by data size/resources.

![Vector Indexing Status](https://github.com/DavidArayaS/AI-Powered-Insights-Fraud-Detection-Hackathon/blob/7b4a95aa515d6cea3bffc4253b32ac0981bb527a/04-AI%20Chatbot/Reference%20Pictures/vector13.png)

### 7. Add Your Custom Data to Your Chat Model

1. In your **Azure AI Foundry** project, under **Playgrounds**, open **try the chat playground**  
2. Click **Add your data**  
3. Pick the **project index** from the previous step  
4. For **Search type**, keep **hybrid**  
5. No other changes; your chatbot now includes **custom data**  
6. After refreshing, ask specific questions like:
   - “What is the Address of ADDR-29841?”
   - “What is the ApplicationID of the customer CLI-19708?”
   - “How many clients does Wayne Enterprises company have?”
   - “How many addresses are from Texas?”
   - “Can you list all the address IDs for the addresses from Texas?”

**Congratulations!**  
You’ve trained the model with **your data**, giving domain-specific answers. Note:

- **txt** format often yields better responses
- **csv** might cause inconsistent answers

In the later Milestones we wil solve that problems.

> **TIP**: If you used **csv** data, consider **txt** for better results. You’ll also see it’s easy to get single-record details but harder to do **bulk** responses—this setup needs more advanced frameworks or custom solutions for bigger queries.

## 🚀 Milestone #2: Result

---

You can **Build & Customize** a Generative AI app with your **own custom data**. Now, when you ask the same question as before, it references **your** data. Check the **References** button to see the underlying details.

---


## 🚀 Milestone #3: Build & Customize – Create, Iterate, and Debug Your Orchestration Flows

**Context**: This sample **prompt flow** manages a **multi-round conversation**, retaining history for each new user request. It uses a set of tools to:
1. **Append** the conversation history to form a contextual question  
2. **Retrieve** data from your index  
3. **Generate** prompt context using the retrieved data  
4. **Create** prompt variants (system message, structured history)  
5. **Submit** the final prompt to a language model to get a natural language response

### 1. Save the Current Prompt Flow

1. In **Azure AI Foundry**, open your **project** → **Playgrounds** → **chat model**  
2. Click **prompt flow** and save it with a name like `default-flow`  
3. Review the steps in the flow; you’ll soon clone it so the chat can include conversation history

### 2. Use the Index in a Prompt Flow

1. Your **vector index** is already stored in your **AI Foundry** project, making it simple to include in a prompt flow  
2. In the **AI Foundry** portal, open your **project** → **Build and customize** → **Prompt flow**  
3. **Create a new prompt flow** by cloning the **Multi-Round Q&A on Your Data** sample  
4. Save that clone in a folder named `product-flow`  
5. Click **Start compute session** to launch the runtime; wait until it’s ready  
6. In **Inputs**, confirm:
   - `chat_history`
   - `chat_input`  
   (The default sample includes some AI conversation.)

7. In **Outputs**, ensure:
   - `chat_output` = `${chat_with_context.output}`

8. In **modify_query_with_history**:
   - **Connection** = default Azure OpenAI
   - **Api** = `chat`
   - **deployment_name** = `gpt-35-turbo-16k`
   - **response_format** = `{"type":"text"}`

9. Once the compute session starts, go to **lookup**:
   - `mlindex_content`: click the blank field → **Generate** pane  
     - **index_type**: **Registered Index**  
     - **mlindex_asset_id**: `<your_vector_index>:1`  
     - **save**
   - `queries`: `${modify_query_with_history.output}`
   - `query_type`: **Hybrid** (vector + keyword)
   - `top_k`: 2

10. In **generate_prompt_context**, confirm `search_result (object)` = `${lookup.output}`

11. In **Prompt_variants**:
   - `contexts (string)` = `${generate_prompt_context.output}`
   - `chat_history (string)` = `${inputs.chat_history}`
   - `chat_input (string)` = `${inputs.chat_input}`

12. In **chat_with_context**:
   - **Connection** = `Default_AzureOpenAI`
   - **Api** = `Chat`
   - **deployment_name** = `gpt-35-turbo-16k`
   - **response_format** = `{"type":"text"}`
   - `prompt_text (string)` = `${Prompt_variants.output}`

13. On the **toolbar**, click **Save** to finalize changes in the prompt flow  
14. On the **toolbar**, select **Chat**. A pane opens with sample conversation history and default input (you can ignore it).  
15. Replace the default question with **how many clients does Wayne Enterprises company have?** and submit  
16. Examine the response, which should be sourced from your index  
17. Review the output of each tool in the flow  
18. Enter additional queries, for example:

    What is the status of the client with ClientId CLI-28048?.
    What is the Address of ADDR-29841?
    What is the ApplicationID of the customer CLI-19708?
    Is the loan approved?
    How many clients does Wayne Enterprises company has?
    How many addresses are from texas?
    Can you list down all the address ID for the addresses from Texas?

19. Notice how it uses **index data** and **chat history**  
20. Observe each tool’s transformations to build a contextual prompt

#### 3. Deploy the Flow

**Congratulations!** You’ve trained the model with your own data and created a custom prompt flow so users can chat iteratively while retaining history. The conversation context and history is included each time.This is done via GUI with no-to-low code 

### Milestone #3: Result

---
The sample prompt flow you are using implements the prompt logic for a chat application in which the user can iteratively submit text input to the chat interface. The conversational history is retained and included in the context for each iteration. With this, the challenge #3 is completed; we still have not solved the problem of bulk response query or rather SQL-formatted queries in human language. Hungry for more? Let’s explore further!

---

---

## 🚀 Milestone #4: Query Multiple CSV Files Using Azure OpenAI & Langchain Framework

**Context**: At the end of Milestone #2, we observed the model handling certain questions (e.g., specific data fields). But for **SQL-formatted queries** or more complex data in a **human-readable** format, our chat app isn’t fully autonomous yet. Larger or semi-structured data (like CSV or Excel) can be challenging. This is where an **AI Agent** plus **OpenAI** comes in, enabling powerful, flexible queries on more complex data.

### 1. Create an Azure OpenAI Resource from the Portal
### 2. Deploy Model

You need a model capable of generating **natural language responses** from your data.

- **Steps**:

1. In the **Azure AI Foundry** portal, within your **Azure OpenAI** resource, go to **Deployments** → **Model deployments** → **Deploy base model**.
2. Create a new deployment of `gpt-35-turbo-instruct` by selecting **Customize** after confirming:
3. **Test** your chatbot with a quick question like “What do you do?” to confirm it responds.

Now we’ll move to our local environment so this OpenAI service can connect with our CSV data in a **human-readable** manner.

**TIP**: We’re using **VSCode** as our editor. It’s helpful to have the following extensions:

```markdown
Azure Account  
Azure CLI Tools  
Azure Developer CLI  
Azure Machine Learning  
Jupyter  
Jupyter Notebook Renderers  
jupyter-notebook-vscode  
Linter  
Pylance  
Python  
Python Debugger  
Python snippets
```

### 3. Write the python Code using Langchain framework and read the csv from storage account ,combine and get it ready for querying using an agent,deploy an agent and invoke the agent to get answers

1. Install the various python packages we will be using during this coding session.open up a new file with .ipynb extension,this will help us run the code in cells and seperate functions ,this is better for troubleshooting and learning the python coding also

```python
%pip install openai
%pip install langchain
%pip install pandas
%pip install langchain_experimental
%pip install langchain_openai
%pip install tabulate
%pip install azure-storage-blob
```

2. Import the necessary packages and also connect to the Azure subscription, gather the details, get the CSV files in a loop, and combine them together using dataframes and place it in a single file

```python
import openai
import pandas as pd
from io import StringIO
from azure.storage.blob import BlobServiceClient
connection_string = "<<connectionstrong of your storage account>>"
container_name = "refined-data"
blob_names = ["DimAddress.csv", "DimApplicant.csv", "DimClient.csv", "factfinancial.csv"]
# Create a BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)
dataframes = []
for blob_name in blob_names:
    blob_client = container_client.get_blob_client(blob_name)

    # Download the blob content
    blob_content = blob_client.download_blob().content_as_text()

    # Read the content into a pandas DataFrame
    df = pd.read_csv(StringIO(blob_content))
    dataframes.append(df)

combined_df = pd.concat(dataframes, ignore_index=True)
print(combined_df.head())
```

3. Save the combined DataFrame to a CSV file and save locally

```python
combined_csv_path = "combined.csv"
combined_df.to_csv(combined_csv_path, index=False)
```

4. Connect to the OpenAI resource and the deployment which we created earlier

```python
from langchain_openai import AzureOpenAI

llm = AzureOpenAI(
    deployment_name="gpt-35-turbo-instruct",
    openai_api_type="azure",
    openai_api_key="<<your openAPI key>>",
    azure_endpoint="<<your openAI resource end point>>",
    api_version="<<gather this from the foundry>>"
)
```

6. Create the CSV agent using Langchain and combine the same to a single file and save locally to get the results faster

```python
%pip install langchain_experimental
from langchain_experimental.agents import create_csv_agent

agent = create_csv_agent(
    llm=llm, 
    path='combined.csv', 
    verbose=True, 
    low_memory=False, 
    allow_dangerous_code=True
)
```

7. Invoke the agent and ask the questions which are structured queries but in human-readable format

```python
agent.invoke("how many addresses are from Texas?")
```

8. Invoke the agent and ask more complicated questions which are structured queries but in human-readable format which also did not give us the right answers in the past milestones

```python
agent.invoke("can you list down all the address IDs for the addresses from Texas?")
```

Congratulations! 🎉 You are now able to talk to the CSV using the OpenAI resources programmatically. The last two questions weren't answered in the first 3 milestones, and we started getting the correct responses for the questions we asked in the format we want! 🏆

These 4 milestones represent the journey of GenAI apps over the last 24-36 months. 🕰️ At this point, we can converse with any type of data using OpenAI ML frameworks and Foundry offerings. 💬

## 🚀 Milestone #4: Result ✨

---
Your results are **significantly more accurate**, enabling you to query semi-structured or unstructured data in **human-readable prompts** without memorizing any syntax. 🤩 Next, you can explore different frameworks and create other **agents** to fulfill various organizational needs. 🎯 These can include multi-agent systems, single agents working across multiple frameworks or data sources, and potentially deploying your solution as a **web app** or simple site (e.g., using Azure Web Apps), or via Python-based lightweight deployment packages. 🌐

Having addressed all the use cases of reading different source files to retrieve domain-specific answers, 🥳 you’ve extended your application’s intelligence to match the expertise of the prompt engineer’s queries. But how do we push it further? **Enter multi-agent applications**! 🧠 These are small, autonomous subsystems that operate in parallel, in series, or back-and-forth to deliver a refined product—work that might otherwise require hours of manual analysis. 🚀  
Stay tuned to learn more about **multi-agent AI applications** in upcoming challenges! 📚

**Congratulations** once again! 👏
---

### Extra Credits 🌟

- **Deploy your web app** using the new deployment. Test it to see how it behaves in a real environment. 🚀  
- **Deploy your app using cosmos DB** so that the emeddings and vector data and actual data will both be stored in the same place 🚀
- **Enable CICD Pipeline** enable contnious integration and deployment using gitops for LLM models 🚀    
- Experiment with **Temperature** and **P value** to understand how they influence response creativity and variability. 🌡️  
- **Customize** the model’s context or instructions with a humorous or thematic style—maybe channel your favorite movie character’s voice. 🎭  
- Investigate how **Microsoft Fabric** can act as a data source for your AI app,which all features are in preview and what all are GA. 🧵 
---


## 💡 Key Definitions

- **Playground**: A low-code environment in Azure AI Foundry for experimenting with models.
- **Azure AI Services**: A collection of AI offerings (like Cognitive Services, Azure OpenAI, etc.).
- **Prompt flow**: A pipeline or workflow in Azure ML or AI Foundry that orchestrates how input, retrieval, augmentation, and model inference are chained together.
- **Grounding**: Providing the LLM with factual, relevant data to reduce hallucinations and improve context accuracy.
- **Retrieval Augmented Generation (RAG)**: A pattern where data is retrieved from an index or database, then appended to the user’s query before calling the LLM.
- **Azure AI Search**: A service to index and retrieve your data (supports vector-based, semantic, keyword, or hybrid search).
- **Agent**: In Foundry, an AI agent can automatically retrieve data, interact with knowledge sources, and produce answers or even execute actions.

---

## Why We Need RAG

When you ask an LLM a question, it normally only relies on **static training data**. If that data is outdated or missing details about your **specific** documents, the model might respond with **“hallucinated”** info.

**RAG** addresses this by:
1. Retrieving relevant context from an **external** data source (like your CSV or text files).
2. **Augmenting** the prompt with that context so the model uses fresh, correct info.
3. **Generating** a more **accurate** and **domain-specific** answer.

---
**Happy building and hacking!** 🚀
---
