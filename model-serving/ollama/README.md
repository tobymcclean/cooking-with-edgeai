
# Ollama

## Description

Ollama is a tool to manage models in a single repository. It allows to manage different versions of the models and to deploy them easily. This directory demonstrates deploying the llama3 8b model using Ollama in a container. It includes some example clients for using the model.

## Docker

### Build the image
In a terminal in this directory, run the following command to build the image:
```Bash
docker build -t ollama .
```

To check that image has been built, run the following command:
```Bash
docker images
```

You should see an image named `ollama`.

### Run the container

To run the container, in a terminal switch to this directory. If the '.ollama' directory does not exist, create it by running the following command:
```Bash
mkdir .ollama
```

Then, to run the container use the following command:
```Bash
docker run -it -v .:/workspace -v ./.ollama:/root/.ollama -w /workspace -p 11434:11434  --name ollama --rm ollama /bin/bash
```

This command will run the container and mount the current directory to the `/workspace` directory in the container. It will also mount the `.ollama` directory to the `/root/.ollama` directory in the container. The container will be removed when it is stopped. It will also expose the port `11434` to the host machine. Finally, it will open a bash shell in the container.

### Run the server
In order to be able to execute multiple commands in the container, we will use 'tmux'. To start a new session, run the following command:
```Bash
tmux
```

To start the server, run the following command:
```Bash
ollama server
```

### Download model
To download a model, we start by creating a new 'tmux' window using the following command:
```Bash
ctrl + b, c
```

Then, we run the following command to download the llama3 8b model:

```Bash
ollama download llama3
```

### Test the server
To test the server, open a terminal outside the container and run the following command:

```Bash
curl http://127.0.0.1:11434/api/chat -d '{
  "model": "llama3",
  "messages": [
    {
      "role": "user",
      "content": "who wrote the book godfather?"
    }
  ],
  "stream": false
}'
```
## Python Client: HTTP Request

To use the Python client, we use the `requests` library. An example, client making an HTTP request to the server can be found in the `ollama_llama3_request.py` file. To run the client, open a terminal in this directory and run the following command:

```Bash
python ollama_llama3_request.py
```

The application has the following optional arguments:

```text
usage: ollama_llama3_request.py [-h] [--host HOST] [--port PORT] [--prompt PROMPT]
```

| Option          | Description                              | Default     |
|-----------------|------------------------------------------|-------------|
| --host HOST     | The host of the ollama service           | localhost   |
| --port PORT     | The port of the ollama service           | 11434       |
| --prompt PROMPT | The prompt to send to the language model | What is AI? |


## Python Client: LangChain
To use the LangChain client, we use the `langchain-community` library. To install it run the following command:

```Bash
pip install langchain langchain-community
```

An example, client using LangChain can be found in the `ollama_llama3_langchain.py` file. To run the client, open a terminal in this directory and run the following command:

```Bash
python ollama_llama3_langchain.py
```

The application has the following optional arguments:

```text
usage: ollama_llama3_langchain.py [-h] [--host HOST] [--port PORT] [--prompt PROMPT]
```

| Option          | Description                              | Default     |
|-----------------|------------------------------------------|-------------|
| --host HOST     | The host of the ollama service           | localhost   |
| --port PORT     | The port of the ollama service           | 11434       |
| --prompt PROMPT | The prompt to send to the language model | who wrote the book godfather? |

## Python Client: ollama
To use the LangChain client, we use the `ollama` library. To install it run the following command:

```Bash
pip install ollama
```

An example, client using the `ollama` library can be found in the `ollama_llama3_client.py` file. To run the client, open a terminal in this directory and run the following command:

```Bash
python ollama_llama3_client.py
```

The application has the following optional arguments:

```text
usage: ollama_llama3_client.py [-h] [--host HOST] [--port PORT] [--prompt PROMPT]
```

| Option          | Description                              | Default     |
|-----------------|------------------------------------------|-------------|
| --host HOST     | The host of the ollama service           | localhost   |
| --port PORT     | The port of the ollama service           | 11434       |
| --prompt PROMPT | The prompt to send to the language model | who wrote the book godfather? |
