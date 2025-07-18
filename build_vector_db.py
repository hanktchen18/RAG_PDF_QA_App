from langchain_community.document_loaders import PyPDFDirectoryLoader # Load pdfs from a specific directory
from langchain_text_splitters import RecursiveCharacterTextSplitter # Cut the pdf into small chunks
import chromadb

# Setting the environment variables
DATA_PATH = r"data"
CHROMA_PATH = r"chroma_db"

chroma_client = chromadb.PersistentClient(path=CHROMA_PATH) # Initialize chroma client

collection = chroma_client.get_or_create_collection(name = "law_docs")

# Load the documents
loader = PyPDFDirectoryLoader(DATA_PATH)

raw_documents = loader.load()

# Split the documents into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=100,
    length_function=len,
    is_separator_regex=False,
)

chunks = text_splitter.split_documents(raw_documents)

# Add the document chunks to chromadb

documents = []
metadata = []
ids = []

i = 0

for chunk in chunks:
    documents.append(chunk.page_content)
    ids.append("ID" + str(i))
    metadata.append(chunk.metadata)
    i += 1

collection.upsert(
    documents=documents,
    metadatas=metadata,
    ids=ids,
)

print(f"Sucessfully created {len(documents)} chunks")