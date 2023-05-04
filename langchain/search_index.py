from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Milvus

from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.llms import OpenAI


MILVUS_HOST = "127.0.0.1"
MILVUS_PORT = "19530"


def main():
    embeddings = OpenAIEmbeddings(model="ada")

    vector_store = Milvus.from_documents(
        [],
        embeddings,
        connection_args={"host": MILVUS_HOST, "port": MILVUS_PORT},
    )

    chain = load_qa_with_sources_chain(
        OpenAI(temperature=0),
        chain_type="map_reduce",
        return_intermediate_steps=True,
    )
    while True:
        query = input("what do you want to ask?\n")
        if query == "exit":
            print("good bye")
            break
        docs = vector_store.similarity_search(query)
        response = chain(
            {"input_documents": docs, "question": query}, return_only_outputs=True
        )
        print(response["output_text"])


if __name__ == "__main__":
    main()
