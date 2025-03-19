

##Load and Combine CSV Files from Azure Storage

import pandas as pd
from io import StringIO
from azure.storage.blob import BlobServiceClient

# Azure Storage Connection
connection_string = "<<YOUR_STORAGE_CONNECTION_STRING>>"
container_name = "refined-data"
blob_names = ["DimAddress.csv", "DimApplicant.csv", "DimClient.csv", "factfinancial.csv"]

# Create a BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)

# Download and combine CSVs
dataframes = []
for blob_name in blob_names:
    blob_client = container_client.get_blob_client(blob_name)
    blob_content = blob_client.download_blob().content_as_text()
    
    # Convert CSV content to Pandas DataFrame
    df = pd.read_csv(StringIO(blob_content))
    dataframes.append(df)

# Merge all DataFrames
combined_df = pd.concat(dataframes, ignore_index=True)

# Save locally
combined_csv_path = "combined.csv"
combined_df.to_csv(combined_csv_path, index=False)

##Connect to Azure OpenAI and Deploy LLM

from langchain_openai import AzureOpenAI

# Define OpenAI Connection
llm = AzureOpenAI(
    deployment_name="gpt-35-turbo-instruct",
    openai_api_type="azure",
    openai_api_key="<<YOUR_OPENAI_API_KEY>>",
    azure_endpoint="<<YOUR_AZURE_OPENAI_ENDPOINT>>",
    api_version="<<YOUR_AZURE_OPENAI_API_VERSION>>"
)

##Create Langchain CSV Agent

from langchain_experimental.agents import create_csv_agent

# Create Langchain CSV Agent
agent = create_csv_agent(
    llm=llm, 
    path='combined.csv', 
    verbose=True, 
    low_memory=False, 
    allow_dangerous_code=True
)

##Query the Data Using Natural Language

# Simple Query: Count Addresses from Texas
agent.invoke("How many addresses are from Texas?")

# Complex Query: List All Address IDs from Texas
agent.invoke("Can you list all the address IDs for the addresses from Texas?")