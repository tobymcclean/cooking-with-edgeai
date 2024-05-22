import sys
import argparse

from langchain_community.chat_models import ChatOllama

URL_TEMPATE = 'http://{host}:{port}'


def main(args):
    url = URL_TEMPATE.format(host=args.host, port=args.port)
    llm = ChatOllama(model='llama3', temperature=0, base_url=url)
    response = llm.invoke(args.prompt)
    print(response.content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ollama llama3 LangChain')
    parser.add_argument('--host', type=str, default='localhost', help='The host of the ollama service')
    parser.add_argument('--port', type=int, default=11434, help='The port of the ollama service')
    parser.add_argument('--prompt', type=str, default='who wrote the book godfather?', help='The prompt to send to the ollama service')
    args = parser.parse_args()

    main(args)
    sys.exit(0)
