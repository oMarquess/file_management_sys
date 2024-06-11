import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from django.conf import settings

# Load environment variables
load_dotenv()

# API Key and LLM name configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'default_api_key')
llm_name = os.getenv('llm_name', 'gpt-3.5-turbo-1106')

llm = ChatOpenAI(model_name=llm_name, temperature=0)
