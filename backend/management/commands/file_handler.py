from django.core.management.base import BaseCommand, CommandError
from langchain.document_loaders import CSVLoader, PyPDFLoader
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from tqdm import tqdm
import os

class Command(BaseCommand):
    help = 'Process PDF and other documents'

    def add_arguments(self, parser):
        parser.add_argument('file_paths', nargs='+', type=str, help='Paths to the PDF, PPT, PPTX, CSV files')

    def handle(self, *args, **options):
        for file_path in options['file_paths']:
            try:
                file_extension = os.path.splitext(file_path)[1].lower()
                if file_extension == '.csv':
                    loader = CSVLoader(file_path=file_path, encoding="utf-8", csv_args={'delimiter': ','})
                else:
                    loader = UnstructuredFileLoader(file_path)

                self.stdout.write(f"Loading documents from {file_path}...")
                docs = [doc for doc in tqdm(loader.load(), desc='Loading')]

                self.stdout.write("Splitting documents...")
                text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=5)
                docs = [doc for doc in tqdm(text_splitter.split_documents(docs), desc='Splitting')]

                self.stdout.write("Embedding documents...")
                embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
                db = Chroma.from_documents(docs, embedding_function, ids=None, collection_name="langchain", persist_directory="./chroma_db")

                self.stdout.write(self.style.SUCCESS(f'Successfully processed and embedded documents from {file_path}'))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error processing file {file_path}: {e}"))
