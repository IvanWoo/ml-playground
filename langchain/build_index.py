from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import MarkdownHeaderTextSplitter
from langchain.vectorstores import Milvus


MILVUS_HOST = "127.0.0.1"
MILVUS_PORT = "19530"


def main():
    # TODO: add api docs
    loader = DirectoryLoader(
        "./langchain/data/kolena/docs",
        glob="**/*.md",
        loader_cls=TextLoader,
        show_progress=True,
    )
    documents = loader.load()

    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
        ("####", "Header 4"),
    ]
    text_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
    splits = text_splitter.split_text(" ".join([d.page_content for d in documents]))

    embeddings = OpenAIEmbeddings()
    vectordb = Milvus.from_documents(
        splits,
        embeddings,
        connection_args={"host": MILVUS_HOST, "port": MILVUS_PORT},
        drop_old=True,
    )
    return vectordb


if __name__ == "__main__":
    main()
