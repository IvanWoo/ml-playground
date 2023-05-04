from langchain.document_loaders import GitbookLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Milvus


MILVUS_HOST = "127.0.0.1"
MILVUS_PORT = "19530"


def main():
    loader = GitbookLoader("https://docs.kolena.io", load_all_paths=True)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1024, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings(model="ada")

    vector_store = Milvus.from_documents(
        docs,
        embeddings,
        connection_args={"host": MILVUS_HOST, "port": MILVUS_PORT},
        drop_old=True,
    )
    return vector_store


if __name__ == "__main__":
    main()
