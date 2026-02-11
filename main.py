# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain_pinecone import PineconeVectorStore
# from pinecone import Pinecone
# from dotenv import load_dotenv
# import os
# from langchain_google_genai import ChatGoogleGenerativeAI
#
# load_dotenv()
# api_key = os.getenv("PINECONE_API_KEY")
#
# vector_store = None
# def load_pdfs(pdf_paths: list):
#     documents = []
#     for path in pdf_paths:
#         loader = PyPDFLoader(path)
#         docs = loader.load()
#         documents.extend(docs)
#     return documents
#
#
# # Example usage
# pdf_files = [
#     "docs/android_architecture.pdf",
#     "docs/mobile_security.pdf"
# ]
#
#
# def text_split(paths: list):
#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=1000,
#         chunk_overlap=150
#     )
#     raw_documents = load_pdfs(paths)
#     print(f"Loaded {len(raw_documents)} pages")
#     split_documents = text_splitter.split_documents(raw_documents)
#     print(f"Created {len(split_documents)} text chunks")
#     return split_documents
#
#
# def get_vector_store():
#     global vector_store
#     docs = text_split(pdf_files)
#     embeddings = GoogleGenerativeAIEmbeddings(
#         model="models/embedding-001",
#         google_api_key=os.getenv("GOOGLE_API_KEY")
#     )
#
#     pc = Pinecone(api_key=api_key)
#     index = pc.Index("pdf_texts")
#     vector_store = PineconeVectorStore.from_documents(embedding=embeddings, index=index, documents=docs )
#     return vector_store
#
#
# def llmm():
#     llm = ChatGoogleGenerativeAI(
#         model="gemini-1.5-flash",
#         temperature=0
#     )
#
#
# if __name__ == "__main__":
#     print("")


import tensorflow as tf
print("TensorFlow version:", tf.__version__)