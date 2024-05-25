# Securing Ollama with a Reverse Proxy

This guide will walk you through how to secure Ollama with a reverse proxy. We will use Nginx as the reverse proxy server and configure it to use HTTPS.

## What is a Reverse Proxy?

A reverse proxy is a server that sits between the client application and the inference server(s), forwarding requests to the inference server and returning the server's responses back to the application. It acts as an intermediary for requests from applications seeking inferences from servers that provide those inferences.

In the context of inference serving, a reverse proxy can provide various benefits such as:

1. **Increased Security:** By masking the identity of backend servers, a reverse proxy can protect servers from direct exposure to the internet, reducing the risk of attacks.
2**SSL Termination:** It can handle the SSL encryption/decryption process (i.e., the processing of secure requests), offloading this task from the inference servers to free up resources.


In your project, Nginx is being used as a reverse proxy to secure the Ollama service. It listens to incoming requests and forwards them to the Ollama service running on a different port. It also includes various security headers in its responses to enhance the security of the application.

## Using Docker Composer to Run Nginx and Ollama

### Prerequisites

1. Docker and Docker Compose installed on your machine.
2. [Minica](https://github.com/jsha/minica) installed on your machine.

### Process

1. **Use Minica to generate SSL certificates**
    
    - Create a `certs` directory in the project root directory.
    
   ```bash
    mkdir certs && cd certs
   ```
   - Generate the SSL certificates using Minica.
    
   ```bash
    minica --domains localhost
   ```
   
    This will generate the SSL certificates in the `localhost` directory, and a root certificate if it doesn't already exist in the `certs` directory.


2. **Launch the Services**
 
    ```bash
   docker-compose up
   ```
   
    This command will start the Nginx and Ollama services. Nginx will be listening on port 443 (HTTPS) and forwarding requests to the Ollama service running on port 8000.

3. **Test the setup**
    
    Open a web browser and navigate to `https://localhost`. You should see a webpage with the message `Ollama is running`.


