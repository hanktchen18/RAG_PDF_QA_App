import chromadb
from google import genai
from dotenv import load_dotenv
import os


load_dotenv()

# Setting the environment variables
DATA_PATH = r"data"
CHROMA_PATH = r"chroma_db"

chroma_client = chromadb.PersistentClient(path=CHROMA_PATH) # Initialize chroma client

collection = chroma_client.get_or_create_collection(name = "law_docs")

while True:
    print("--------------------------------")
    user_query = input("What do you want to know about this law?\n(or press q to quit)\n\n")
    if user_query == "q":
        break

    results = collection.query(
        query_texts=[user_query],
        n_results=1
    )
    if results["documents"] == []:
        print("No relevant documents found in the database. The answer might be 'I don't know'.")
        continue
    
    # Initialize Gemini Client
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    system_prompt = """
    You are a helpful assistant that can answer questions about the law.
    But you only answer based on the documents provided. You don't use your internal knowledge
    and you don't make up information.

    If you don't know the answer, you say "I don't know. Please be more specific or ask a different question.".

    -------------------------

    The data: 

    """+str(results["documents"])+"""
    """

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[system_prompt]
    )

    print("\n\n--------------------------------\n\n")

    print(response.text)