import os
import openai
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API Key from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set threshold for flagging suspicious transactions
AML_THRESHOLD = float(os.getenv("AML_THRESHOLD", 1000000))

# Sample transaction data (this could be dynamic in a real system)
sample_transaction = {
    "tx_id": "abc123xyz",
    "sender": "address1",
    "receiver": "address2",
    "amount": 1500000,  # Example of a large transaction
    "timestamp": "2024-12-31T15:00:00Z",
    "metadata": "Suspicious activity detected in sender address."
}

# LangChain setup: Initialize LLM (OpenAI GPT-4 here)
llm = OpenAI(temperature=0.7, model="gpt-4")

# Define a prompt template for transaction analysis
template = """
Analyze the following blockchain transaction for signs of money laundering or fraud.
Look for unusual transaction volumes, suspicious addresses, or inconsistencies in metadata.

Transaction Details:
Transaction ID: {tx_id}
Sender: {sender}
Receiver: {receiver}
Amount: {amount}
Timestamp: {timestamp}
Metadata: {metadata}

Provide a concise analysis and flag if there are any suspicious activities.
"""

# Initialize LangChain's prompt and chain
prompt = PromptTemplate(input_variables=["tx_id", "sender", "receiver", "amount", "timestamp", "metadata"], template=template)
chain = LLMChain(llm=llm, prompt=prompt)

# Function to analyze a transaction using LangChain
def analyze_transaction(transaction):
    # Run the LangChain analysis on the transaction
    analysis = chain.run(
        tx_id=transaction["tx_id"],
        sender=transaction["sender"],
        receiver=transaction["receiver"],
        amount=transaction["amount"],
        timestamp=transaction["timestamp"],
        metadata=transaction["metadata"]
    )

    return analysis

# Function to check if the transaction is suspicious
def check_transaction(transaction):
    # Perform analysis using LangChain
    analysis = analyze_transaction(transaction)

    # Flagging suspicious transactions based on certain criteria
    if transaction["amount"] > AML_THRESHOLD or "suspicious" in analysis.lower():
        print(f"Transaction ID {transaction['tx_id']} flagged as suspicious.")
        print(f"Analysis: {analysis}")
        return True  # Suspicious transaction
    else:
        print(f"Transaction ID {transaction['tx_id']} appears legitimate.")
        return False  # Legitimate transaction

# Analyze a sample transaction
check_transaction(sample_transaction)
