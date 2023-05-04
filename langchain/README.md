# [LangChain](https://python.langchain.com/en/latest/index.html)

## Question Answering over Docs

### start the milvus based on [this doc](/README.md)

### build index

```sh
pdm run langchain/build_index.py
```

### search index

```sh
pdm run langchain/search_index.py
```

known issues:

- `openai.error.InvalidRequestError: This model's maximum context length is 4097 tokens, however you requested 4699 tokens (4443 in your prompt; 256 for the completion). Please reduce your prompt; or completion length.`
