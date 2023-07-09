from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Milvus
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

MILVUS_HOST = "127.0.0.1"
MILVUS_PORT = "19530"


def main():
    embeddings = OpenAIEmbeddings()

    vectordb = Milvus.from_documents(
        [],
        embeddings,
        connection_args={"host": MILVUS_HOST, "port": MILVUS_PORT},
    )

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Use three sentences maximum. Keep the answer as concise as possible. Always say "thanks for asking!" at the end of the answer.
    {context}
    Question: {question}
    Helpful Answer:"""
    QA_CHAIN_PROMPT = PromptTemplate.from_template(template)
    # TODO: add memory
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=vectordb.as_retriever(),
        return_source_documents=True,
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
        chain_type="stuff",
    )
    while True:
        query = input("what do you want to ask?\n")
        if query == "exit":
            print("good bye")
            break
        result = qa_chain({"query": query})
        print(result["result"])
        print(result["source_documents"][0])
        print("\n")


if __name__ == "__main__":
    main()
