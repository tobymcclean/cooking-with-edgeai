# How to Run nvidia-smi in a K8S Cluster

This shows how to deploy a `job` to run `nvidia-smi` on a node in a Kubernetes cluster.

> [!NOTE]
> **Before you start**
>
> This how-to assumes that you have a Kubernetes cluster with at least one node with an NVIDIA GPU. And the NVIDIA GPU Operator should be deployed in the cluster.
>


## Ingredients

1. A Kubernetes cluster
2. An accessible node with kubectl and a text editor that can reach the cluster.
3. A cluster node with an NVIDIA GPU.

## Instructions

Use your favorite text editor and a system with `kubectl` that can access the cluster.

1. Create a file to describe the ```job```

   ```bash
    touch nvidia-smi-job.yaml
   ```

2. Open the file in a text editor. For example,

   ```Bash
   nano nvidia-smi-job.yaml
   ```

3. Paste the following ```job``` description into the file

Make sure to change the `metadata.namespace` value to the namespace in which you want to launch the job. Similarly, the `spec.template.affinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchExpressions.values` should be changed to the node name on which you want to run the job.

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: nvidia-smi
  namespace: playground
spec:
  template:
    metadata:
      name: nvidia-smi
    spec:
      containers:
        - name: nvidia-smi
          image: 'nvcr.io/nvidia/cuda:12.1.0-runtime-ubuntu20.04'
          command:
            - nvidia-smi
      restartPolicy: Never
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
              - matchExpressions:
                  - key: kubernetes.io/hostname
                    operator: In
                    values:
                      - us-5501-nb.supermicro.com
```

4. Deploy the `job` to the cluster

```Bash
kubectl apply -f nvidia-smi.yaml
```

5. Examine the logs of the ```job```

After getting the pods with the first command, use the pod's name in the second command to get the logs for the pod created for the job.

```Bash
kubectl get -n <namespace> po
kubectl logs -n <namespace> <pod name> -f
```
