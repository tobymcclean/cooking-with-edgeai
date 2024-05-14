ARG BASE_IMAGE_URL=nvcr.io/nvidia/nemo/nemofw-inference
ARG BASE_IMAGE_TAG=23.10-for-rag

FROM ${BASE_IMAGE_URL}:${BASE_IMAGE_TAG}

ENV LD_LIBRARY_PATH=/opt/tritonserver/backends/tensorrtllm:$LD_LIBRARY_PATH

# example source repository
RUN git clone https://github.com/NVIDIA/GenerativeAIExamples.git --single-branch /tmp/examples

# install model-server automation
RUN cp -r /tmp/examples/RetrievalAugmentedGeneration/llm-inference-server/conversion_scripts /opt/conversion_scripts && \
cp -r /tmp/examples/RetrievalAugmentedGeneration/llm-inference-server/ensemble_models /opt/ensemble_models && \
cp -r /tmp/examples/RetrievalAugmentedGeneration/llm-inference-server/model_server /opt/model_server && \
cp -r /tmp/examples/RetrievalAugmentedGeneration/llm-inference-server/model_server_client /opt/model_server_client && \
cp /tmp/examples/RetrievalAugmentedGeneration/llm-inference-server/requirements.txt /opt/requirements.txt && \
rm -rf /tmp/examples

RUN pip install --no-cache-dir -r /opt/requirements.txt

# Create basic directories

RUN mkdir /model && chmod 1777 /model && \
    mkdir -p /home/triton-server && chown 1000:1000 /home/triton-server && chmod 700 /home/triton-server

WORKDIR /opt
ENTRYPOINT ["/usr/bin/python3", "-m", "model_server"]
