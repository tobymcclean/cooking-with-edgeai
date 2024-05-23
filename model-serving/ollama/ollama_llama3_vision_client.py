import argparse
import sys

from ollama import Client

URL_TEMPATE = 'http://{host}:{port}'
APP_DESCRIPTION = 'ollama llava (vision model) example using the ollama python client'

def main(args):
    print(APP_DESCRIPTION)
    print(f'Host: {args.host}')
    print(f'Port: {args.port}\n')
    client = Client(host=URL_TEMPATE.format(host=args.host, port=args.port))
    response = client.chat(
        model='llava',
        messages=[{'role': 'user', 'content': args.prompt, 'images': [args.image]}],
    )
    print(response['message']['content'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ollama llama3 LangChain')
    parser.add_argument('--host', type=str, default='localhost', help='The host of the ollama service')
    parser.add_argument('--port', type=int, default=11434, help='The port of the ollama service')
    parser.add_argument('--prompt', type=str, default='Describe this image:', help='The prompt to send to the ollama service')
    parser.add_argument('--image', type=str, default='./imgs/jmb.jpg', help='The image to send to the ollama service')
    args = parser.parse_args()

    main(args)
    sys.exit(0)
