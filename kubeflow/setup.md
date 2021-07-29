# Setup Guide

This is a setup guide to install Kubeflow on local machine. To install [Kubeflow](https://www.kubeflow.org/),
both [Kubernetes](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)
and [Kustomize version 3.2.0](https://kustomize.io/) are required. Follow the instructions based on local operating
system to get Kubeflow up and running before joining the vGHC OSD workshop
**An Illustrated Guide to MLOps using Kubeflow** on October 1st 2021.

- [Linux]()
    - [Ubuntu](#ubuntu)
    - [Fedora]()
- [MacOS](#macos)
- [Windows]()

##Ubuntu
1. **Install Kustomize**

   To install [Kustomize](https://github.com/kubernetes-sigs/kustomize/releases/tag/v3.2.0) version 3.2.0
     first download `kustomize_3.2.0_linux_amd64` by executing:
   ```
   wget https://github.com/kubernetes-sigs/kustomize/releases/download/v3.2.0/kustomize_3.2.0_linux_amd64
   ```
   Run the following to make `kustomize` executable and move it:
   
    ```
    chmod +x kustomize_3.2.0_linux_amd64 && sudo mv kustomize_3.2.0_darwin_amd64 /usr/local/bin/kustomize
    ```

2. **Install kubectl**

   Download the latest release with the command:
   ```
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
   ```
   Install [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/#install-kubectl-binary-with-curl-on-linux)
   ```
   sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
   ```
   Once installed, run the following command to validate successful installation
   ```
   kubectl version
   ```
   
   Output should look similar to below.
   ```
   Client Version: version.Info{Major:"1", Minor:"21", GitVersion:"x.xx.x", GitCommit:"xxxxx", GitTreeState:"clean", BuildDate:"xxxx-xx-xxTxx:xx:xxx", GoVersion:"gx.xx.x", Compiler:"gc", Platform:"linux/amd64"}
   ```

3. **Install Kubernetes locally.** </br>
   Choose one of the following options to install it:
   - <details>
      <summary>Kind</summary>
     
      [Kind](https://kind.sigs.k8s.io/docs/user/quick-start/) lets you run Kubernetes on your local computer. This tool requires that you have [Docker](https://docs.docker.com/get-docker/) installed and configured.
     ```
      curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.11.1/kind-linux-amd64
      chmod +x ./kind && mv ./kind /usr/local/bin/kind
     ```
      Start Kubernetes Cluster
      ```
      kind create cluster
     ```
     Successful creation of kind cluster should result in the following output:
     ```
     Creating cluster "kind" ...
     ✓ Ensuring node image (kindest/node:v1.21.1) 🖼
     ✓ Preparing nodes 📦  
     ✓ Writing configuration 📜
     ✓ Starting control-plane 🕹️
     ✓ Installing CNI 🔌
     ✓ Installing StorageClass 💾
     Set kubectl context to "kind-kind"
     
     You can now use your cluster with: 
     kubectl cluster-info --context kind-kind
     
     Thanks for using kind! 😊
      ```
   </details>

   - <details>
      <summary>minikube</summary>
     
     Prerequisites: Container or virtual machine manager, such as: Docker, Hyperkit, Hyper-V, KVM, Parallels, Podman, VirtualBox, or VMWare.
     
     To install the latest version of [minikube](https://minikube.sigs.k8s.io/docs/start/) execute:  
      ```
     curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
     sudo install minikube-linux-amd64 /usr/local/bin/minikube
     ```
     Start Kubernetes Cluster
      ```
      minikube start --cpus 8 --memory 16000 --disk-size=128g
      ```
      Successful creation of minikube cluster should result in the following output:
      ```
      😄  minikube v1.22.0 on Ubuntu 20.04
      ✨  Automatically selected the docker driver. Other choices: kvm2, ssh
      ❗  Your cgroup does not allow setting memory.
      ▪ More information: https://docs.docker.com/engine/install/linux-postinstall/#your-kernel-does-not-support-cgroup-swap-limit-capabilities
      👍  Starting control plane node minikube in cluster minikube
      🚜  Pulling base image ...
      🔥  Creating docker container (CPUs=8, Memory=16000MB) ...
      🐳  Preparing Kubernetes v1.21.2 on Docker 20.10.7 ...
      ▪ Generating certificates and keys ...
      ▪ Booting up control plane ...
      ▪ Configuring RBAC rules ...
      🔎  Verifying Kubernetes components...
      ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
      🌟  Enabled addons: storage-provisioner, default-storageclass
      🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
      ```
      1. Validate connection to Kubernetes cluster by running a `kubectl` command
      ```
      kubectl get nodes
      
      NAME       STATUS   ROLES                  AGE   VERSION
      minikube   Ready    control-plane,master   18s   v1.21.2
      ```

    </details>

4. [Install Kubeflow](#install-kubeflow)
5. [Clean up](#clean-up)

## MacOS

1. Install [Kustomize version 3.2.0](https://github.com/kubernetes-sigs/kustomize/releases/tag/v3.2.0)
    - Navigate to `Assets` and download `kustomize_3.2.0_darwin_amd64`
    - Run the following to make `kustomize` executable and move
    ```
    chmod +x kustomize_3.2.0_darwin_amd64 && mv kustomize_3.2.0_darwin_amd64 /usr/local/bin/kustomize
    ```
1. Install `kubectl` using brew
   ```
   brew install kubectl 
   ```

   Once installed, run the following command to validate successful installation
   ```
   kubectl version
   ```

   Output should look similar to below.
   ```
   Client Version: version.Info{Major:"1", Minor:"21", GitVersion:"x.xx.x", GitCommit:"xxxxx", GitTreeState:"clean", BuildDate:"xxxx-xx-xxTxx:xx:xxx", GoVersion:"x.xx.x", Compiler:"gc", Platform:"darwin/amd64"}
   ```
1. Choose one of the following options to install and run [Kubernetes](https://kubernetes.io/) locally.
    - [kind](#kind)
    - [Docker Desktop for Mac](#docker-desktop-for-mac)
    - [Minikube]()
1. [Install Kubeflow](#install-kubeflow)
1. [Clean up](#clean-up)

### kind

1. Download [kind](https://kind.sigs.k8s.io/) using brew
   ```
   brew install kind
   ```
1. Start Kubernetes Cluster
   ```
   kind create cluster
   ```
   Successful creation of kind cluster should result in the following output
   ```
   Creating cluster "kind" ...
     ✓ Ensuring node image (kindest/node:v1.21.1) 🖼
     ✓ Preparing nodes 📦
     ✓ Writing configuration 📜
     ✓ Starting control-plane 🕹️
     ✓ Installing CNI 🔌
     ✓ Installing StorageClass 💾
   Set kubectl context to "kind-kind"
   You can now use your cluster with:

   kubectl cluster-info --context kind-kind

   Thanks for using kind! 😊
   ```
1. Validate connection to Kubernetes cluster by running a `kubectl` command
   ```
   kubectl get nodes
   
   NAME                 STATUS   ROLES                  AGE   VERSION
   kind-control-plane   Ready    control-plane,master   57s   v1.21.1
   ```

### Docker Desktop for Mac

1. Download the [latest version of Docker Desktop for Mac](https://docs.docker.com/docker-for-mac/install/)
1. Navigate to preferences to change the resources
    - 8 CPU, 16 GB RAM, 128GB Disk
1. Navigate to [preferences to enable Kubernetes](https://docs.docker.com/desktop/kubernetes/#enable-kubernetes)
1. Validate connection to Kubernetes cluster by running a `kubectl` command
   ```
   kubectl get nodes
   
   NAME             STATUS   ROLES                  AGE   VERSION
   docker-desktop   Ready    control-plane,master   1m    v1.21.2
   ```

### Minikube

1. Install [VMware Fusion](https://www.vmware.com/products/fusion.html) or [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

1. Download [minikube](https://minikube.sigs.k8s.io/docs/) using brew
   ```
   brew install minikube
   ```
   or
   ```
   brew cask install minikube
   ```
1. Start Kubernetes Cluster
   ```
   minikube start --cpus 8 --memory 16000 --disk-size=128g
   ```
   Successful creation of minikube cluster should result in the following output
   ```
   😄  minikube v1.22.0 on Darwin 11.5
   ✨  Automatically selected the docker driver. Other choices: hyperkit, vmware, virtualbox, ssh
   👍  Starting control plane node minikube in cluster minikube
   🚜  Pulling base image ...
   💾  Downloading Kubernetes v1.21.2 preload ...
   🔥  Creating docker container (CPUs=8, Memory=16000MB) ...
   🐳  Preparing Kubernetes v1.21.2 on Docker 20.10.7 ...
       ▪ Generating certificates and keys ...
       ▪ Booting up control plane ...
       ▪ Configuring RBAC rules ...
   🔎  Verifying Kubernetes components...
       ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
   🌟  Enabled addons: storage-provisioner, default-storageclass
   🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
   ```
1. Validate connection to Kubernetes cluster by running a `kubectl` command
   ```
   kubectl get nodes
   
   NAME       STATUS   ROLES                  AGE   VERSION
   minikube   Ready    control-plane,master   45s   v1.21.2
   ```

## Install Kubeflow
The installation process for Kubeflow is the same for all environments.
1. Create a directory `workspace` and clone the `kubeflow/manifest` repo.
    ```
    mkdir -p ~/workspace && cd ~/workspace;
    git clone https://github.com/kubeflow/manifests.git && cd manifests;
    ```
1. Modify `manifests/common/dex/base/deployment.yaml` file to include the following as a workaround for current problem
   with [1.21 Kubernetes cluster and Dex](https://github.com/dexidp/dex/issues/2082). This should not be necessary
   when [workaround](https://github.com/kubeflow/manifests/pull/1883)
   PR merges.
    ```yaml
    env:
    - name: KUBERNETES_POD_NAMESPACE
      valueFrom:
        fieldRef:
          fieldPath: metadata.namespace
    ```

   The content of the `~/workspace/manifests/common/dex/base/deployment.yaml` file should match the content below.
    <details>
        <summary>Dex Deployment File Content</summary>

         apiVersion: apps/v1
         kind: Deployment
         metadata:
           labels:
             app: dex
           name: dex
         spec:
           replicas: 1
           selector:
             matchLabels:
                 app: dex
           template:
             metadata:
               labels:
                 app: dex
             spec:
               serviceAccountName: dex
               containers:
               - image: quay.io/dexidp/dex:v2.22.0
                 name: dex
                 command: ["dex", "serve", "/etc/dex/cfg/config.yaml"]
                 ports:
                 - name: http
                   containerPort: 5556
                 volumeMounts:
                 - name: config
                   mountPath: /etc/dex/cfg
                 envFrom:
                   - secretRef:
                       name: dex-oidc-client
                 env:
                   - name: KUBERNETES_POD_NAMESPACE
                     valueFrom:
                       fieldRef:
                         fieldPath: metadata.namespace
               volumes:
               - name: config
                 configMap:
                   name: dex
                   items:
                   - key: config.yaml
                     path: config.yaml
    </details>
1. Install Kubeflow using `kustomize`.
    ```
    while ! kustomize build example | kubectl apply -f -; do echo "Retrying to apply resources"; sleep 10; done
    ```
1. Validate all Kubeflow resources are available in the following namespaces
    - `auth`
    - `cert-manager`
    - `istio-system`
    - `knative-eventing`
    - `knative-serving`
    - `kubeflow`
    - `kubeflow-user-example-com`

   It could take more than 10mins for all pods to have status `Running`. Please wait for all pods to show
   status `Running` before continuing with validation.
    ```
    # Run the following to check status of all pods in kubeflow namespace
    kubectl get pod --all-namespaces
    ```

   Once all pods are running, the output of should look similar to the example provided.
    <details>
        <summary>Output Example</summary>

        auth                        dex-5ddf47d88d-ztwtn                                        1/1     Running   1          12m
        cert-manager                cert-manager-7dd5854bb4-sqb84                               1/1     Running   0          12m
        cert-manager                cert-manager-cainjector-64c949654c-z5lqn                    1/1     Running   0          12m
        cert-manager                cert-manager-webhook-6b57b9b886-xj8fn                       1/1     Running   0          12m
        istio-system                authservice-0                                               1/1     Running   0          12m
        istio-system                cluster-local-gateway-75cb7c6c88-9h7fr                      1/1     Running   0          12m
        istio-system                istio-ingressgateway-79b665c95-65dmp                        1/1     Running   0          12m
        istio-system                istiod-86457659bb-p26cm                                     1/1     Running   0          12m
        knative-eventing            eventing-controller-575584745f-6td4n                        1/1     Running   0          12m
        knative-eventing            eventing-webhook-6d6f75c565-jpnsh                           1/1     Running   0          12m
        knative-eventing            imc-controller-c8d86c869-fr9x2                              1/1     Running   0          12m
        knative-eventing            imc-dispatcher-7bf75b8999-sjwb5                             1/1     Running   0          12m
        knative-eventing            mt-broker-controller-7778d47797-rj9g7                       1/1     Running   0          12m
        knative-eventing            mt-broker-filter-857c746446-mmv5h                           1/1     Running   0          12m
        knative-eventing            mt-broker-ingress-685cd6b57-v8fb5                           1/1     Running   0          12m
        knative-serving             activator-859796b66c-dj97n                                  2/2     Running   0          12m
        knative-serving             autoscaler-565454fb69-9xfm7                                 2/2     Running   0          12m
        knative-serving             controller-dd58865b5-cm2th                                  2/2     Running   0          12m
        knative-serving             istio-webhook-68fddcc567-48qmx                              2/2     Running   0          12m
        knative-serving             networking-istio-5664b9fb9c-6jbwq                           2/2     Running   1          12m
        knative-serving             webhook-6c8b54d9-jqfc4                                      2/2     Running   1          12m
        kube-system                 coredns-558bd4d5db-7spkm                                    1/1     Running   0          13m
        kube-system                 coredns-558bd4d5db-vqlp5                                    1/1     Running   0          13m
        kube-system                 etcd-docker-desktop                                         1/1     Running   0          13m
        kube-system                 kube-apiserver-docker-desktop                               1/1     Running   0          13m
        kube-system                 kube-controller-manager-docker-desktop                      1/1     Running   0          13m
        kube-system                 kube-proxy-nmcmh                                            1/1     Running   0          13m
        kube-system                 kube-scheduler-docker-desktop                               1/1     Running   0          13m
        kube-system                 storage-provisioner                                         1/1     Running   0          13m
        kube-system                 vpnkit-controller                                           1/1     Running   2          13m
        kubeflow-user-example-com   ml-pipeline-ui-artifact-767659f9df-rftfz                    2/2     Running   0          11m
        kubeflow-user-example-com   ml-pipeline-visualizationserver-6ff9f47c6b-nlsmg            2/2     Running   0          11m
        kubeflow                    admission-webhook-deployment-f5d8f47f8-pgf5k                1/1     Running   0          12m
        kubeflow                    cache-deployer-deployment-6dbb64ddcd-p5n8d                  2/2     Running   1          12m
        kubeflow                    cache-server-f84f6bdcc-kznxj                                2/2     Running   0          12m
        kubeflow                    centraldashboard-9846cbb75-2w8vb                            1/1     Running   0          12m
        kubeflow                    jupyter-web-app-deployment-bdfb5d69f-vp89j                  1/1     Running   0          12m
        kubeflow                    katib-controller-7b98cd6865-m88z2                           1/1     Running   0          12m
        kubeflow                    katib-db-manager-7f5f684dd5-5zc2k                           1/1     Running   0          12m
        kubeflow                    katib-mysql-85fc9c74b8-gl47p                                1/1     Running   0          12m
        kubeflow                    katib-ui-64fbdf4d94-l4dc7                                   1/1     Running   0          12m
        kubeflow                    kfserving-controller-manager-0                              2/2     Running   0          12m
        kubeflow                    kubeflow-pipelines-profile-controller-6cfd6bf9bd-r4bf6      1/1     Running   0          12m
        kubeflow                    metacontroller-0                                            1/1     Running   0          12m
        kubeflow                    metadata-envoy-deployment-95b58bbbb-89pql                   1/1     Running   0          12m
        kubeflow                    metadata-grpc-deployment-c8f784fdf-q52cv                    2/2     Running   3          12m
        kubeflow                    metadata-writer-76b6b98985-7hzqx                            2/2     Running   0          12m
        kubeflow                    minio-5b65df66c9-8j4c4                                      2/2     Running   0          12m
        kubeflow                    ml-pipeline-bdc789b68-df9mq                                 2/2     Running   3          12m
        kubeflow                    ml-pipeline-persistenceagent-6ff46967ff-s6w8l               2/2     Running   0          12m
        kubeflow                    ml-pipeline-scheduledworkflow-66bdf9948d-tx2xr              2/2     Running   0          12m
        kubeflow                    ml-pipeline-ui-57fdfc58cc-2h7zn                             2/2     Running   0          12m
        kubeflow                    ml-pipeline-viewer-crd-64dddf4597-xd8fx                     2/2     Running   1          12m
        kubeflow                    ml-pipeline-visualizationserver-77b748f8fd-xxddl            2/2     Running   0          12m
        kubeflow                    mpi-operator-d5bfb8489-5tg78                                1/1     Running   0          12m
        kubeflow                    mxnet-operator-6cffc568b7-ffq4m                             1/1     Running   0          12m
        kubeflow                    mysql-f7b9b7dd4-cqmsg                                       2/2     Running   0          12m
        kubeflow                    notebook-controller-deployment-68666bf45b-k7548             1/1     Running   0          12m
        kubeflow                    profiles-deployment-85cdbd8dd5-l42tj                        2/2     Running   0          12m
        kubeflow                    pytorch-operator-56bffbbd86-zqx9x                           2/2     Running   0          12m
        kubeflow                    tensorboard-controller-controller-manager-d7c68d6df-cxbg5   3/3     Running   1          12m
        kubeflow                    tensorboards-web-app-deployment-59ff4c7bd8-2c8zq            1/1     Running   0          12m
        kubeflow                    tf-job-operator-859885c8c4-dkf7b                            1/1     Running   0          12m
        kubeflow                    volumes-web-app-deployment-6457c9bcfc-bgvpt                 1/1     Running   0          12m
        kubeflow                    workflow-controller-67bf6d848b-wnk2h                        2/2     Running   1          12m
        kubeflow                    xgboost-operator-deployment-c6ddb584-22qml                  2/2     Running   1          12m
    </details>

1. Validate Kubeflow installation by accessing Kubeflow via `port-forward`.
    ```
    kubectl port-forward svc/istio-ingressgateway -n istio-system 8080:80
    ```
   After running the command, navigate to [http://localhost:8080](http://localhost:8080)
   and login with the default credential:
    - email address: `user@example.com`
    - password: `12341234`

   Once successfully logged in, Kubeflow Dashboard should be available for use.

### Clean up
 - Run the following command to uninstall Kubeflow
 ```
 cd ~/workspace/manifests;
 kustomize build example | kubectl delete -f -;
 ```
Validate the resource deletion by running `kubectl get pod --all-namespaces`

 - To stop running Kubernetes follow the instructions for each options
     - kind
         - Run the following to delete the cluster
         ```
         kind delete cluster
         ```
     - Docker Desktop for Mac
         - Navigate to Docker for Mac preferences -> kubernetes to disable Kubernetes
     - Minikube
         - Run the following to stop and delete the cluster
         ```
         minikube stop
         minikube delete --all
         ```
