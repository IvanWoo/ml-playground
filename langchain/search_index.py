import click
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Milvus
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

MILVUS_HOST = "127.0.0.1"
MILVUS_PORT = "19530"


@click.command()
@click.option(
    "--memory", default=False, is_flag=True, help="Enable memory in conversation."
)
def main(memory: bool):
    embeddings = OpenAIEmbeddings()

    vectordb = Milvus.from_documents(
        [],
        embeddings,
        connection_args={"host": MILVUS_HOST, "port": MILVUS_PORT},
    )
    retriever = vectordb.as_retriever()

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Use three sentences maximum. Keep the answer as concise as possible. Always say "thanks for asking!" at the end of the answer.
    {context}
    Question: {question}
    Helpful Answer:"""
    QA_CHAIN_PROMPT = PromptTemplate.from_template(template)
    if memory:
        _memory = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True
        )
        qa_chain = ConversationalRetrievalChain.from_llm(
            llm,
            retriever=retriever,
            memory=_memory,
        )
    else:
        qa_chain = RetrievalQA.from_chain_type(
            llm,
            retriever=retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
            chain_type="stuff",
        )

    while True:
        query = input("Q: ")
        if query == "exit":
            print("good bye")
            break
        if memory:
            result = qa_chain({"question": query})
            print(result["answer"])
        else:
            result = qa_chain({"query": query})
            print(result["result"])
            print(result["source_documents"][0])
        print("\n")


if __name__ == "__main__":
    main()
