# [LangChain](https://python.langchain.com/en/latest/index.html)

## Question Answering over Docs

### start the milvus based on [this doc](/README.md)

### download data

```sh
pdm run data_kolena
```

### build index

```sh
DB_BACKEND=pgvector pdm run ml_playground/langchain/build_index.py
```

### chatbot

#### cli

```sh
DB_BACKEND=pgvector pdm run langchain_cli
```

#### gui

```sh
DB_BACKEND=pgvector pdm run langchain_gui
```
