from django.conf import settings
from langchain.vectorstores import Chroma
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings




# Database setup
persist_directory = str(settings.BASE_DIR / 'chroma_db')
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# Initialize Chroma database
db = Chroma(persist_directory=persist_directory, embedding_function=embedding_function)
