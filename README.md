# AML Blockchain System

This project implements an **Anti-Money Laundering (AML) system** for blockchain transactions using **LangChain** and **OpenAI**. The system flags suspicious transactions based on volume, known addresses, and metadata using a large language model.

## Prerequisites

- Python 3.x
- OpenAI API Key (or another LLM provider)
- LangChain library

## Setup

1. Clone this repository:
git clone https://github.com/confucius/aml-system.git

2. Install dependencies:
pip install -r requirements.txt


3. Create a `.env` file with your OpenAI API Key:
OPENAI_API_KEY=__
AML_THRESHOLD=1000000


4. Run the AML analysis:
python aml_system.py

