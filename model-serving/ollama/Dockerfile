FROM python:3.11

RUN curl -fsSL https://ollama.com/install.sh | sh

RUN apt update && apt install -y tmux && apt clean && rm -rf /var/lib/apt/lists/*

ENV OLLAMA_HOST=0.0.0.0:11434

EXPOSE 11434

CMD ["ollama", "serve"]
