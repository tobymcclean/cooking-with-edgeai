import argparse
import sys

import requests
import json

APP_DESCRIPTION = 'ollama llama3 HTTP Request'

URL_TEMPLATE = 'http://{host}:{post}/api/chat'

HEADERS = {
    'Content-Type': 'application/json'
}

def request_template(prompt: str, stream: bool = False):
    return {
        "model": "llama3",
        "messages": [
            {
              "role": "user",
              "content": prompt
            }
        ],
        "stream": stream
    }

def main(args):
    print(APP_DESCRIPTION)
    print(f'Host: {args.host}')
    print(f'Port: {args.port}')

    url = URL_TEMPLATE.format(host=args.host, post=args.port)
    print(f'URL: {url}')

    request = request_template(args.prompt)

    response = requests.post(url, headers=HEADERS, json=request)

    print(response.json()['message']['content'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='ollama llama3 HTTP Request')
    parser.add_argument('--host', type=str, default='localhost', help='The host of the ollama service')
    parser.add_argument('--port', type=int, default=11434, help='The port of the ollama service')
    parser.add_argument('--prompt', type=str, default='What is AI?', help='The prompt to send to the ollama service')
    args = parser.parse_args()
    main(args)

    sys.exit(0)
