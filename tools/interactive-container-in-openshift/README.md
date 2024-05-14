# How to Make Interactive Containers in OpenShift

Sometimes it is necessary to have a container that can run in an OpenShift cluster and allow you to interact with it. For example, as part of development you made need to launch a container within a cluster and manually run commands within the container. This guide shows how to enable this for a container in OpenShift.

> [!NOTE]
> **Before you start**
>
> This how-to assumes that you have an OpenShift cluster and access to it with the `oc` tool.

## Ingredients

1. A Kubernetes cluster
2. A node with the `oc` tool that is logged into the cluster.

## Instructions

1. Open the deployment resource in a text editor. For example,

   ```Bash
   kubectl edit deployment <deployment-name>
   ```

2. Add or edit the following lines in the deployment resource:

```yaml
kind: Deployment
apiVersion: apps/v1
...
spec:
  ...
  template:
    ...
    spec:
      containers:
         - name: <container-name>
           ...
           command:
             - /bin/bash # or any other command that will keep the container running
           stdin: true
           tty: true
```

3. Save the changes and exit the editor. This should cause the deployment to update and the container to restart.

4. Open a terminal and run the following command to get a shell in the container:

```Bash
kubectl exec -it <pod-name> -- /bin/bash
```
