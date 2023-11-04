from langchain.vectorstores import Milvus

MILVUS_HOST = "127.0.0.1"
MILVUS_PORT = "19530"


def from_documents(docs, embeddings, db: str = "milvus", **kwargs):
    """
    langchain vectorstores.from_documents wrapper extended with db backend options
    """
    db = db.lower()
    if db == "milvus":
        return Milvus.from_documents(
            docs,
            embeddings,
            connection_args={"host": MILVUS_HOST, "port": MILVUS_PORT},
            **kwargs,
        )
    else:
        raise ValueError(f"unsupported {db=}")
