# Setup Guide

This is a setup guide to install Kubeflow on a local machine. Follow the instructions based on local operating 
 system to get Kubeflow up and running before joining the vGHC OSD workshop **An Illustrated Guide to MLOps using Kubeflow**
 on October 1st 2021.

- [Linux](#linux)
    - [Ubuntu](#ubuntu)
- [MacOS](#macos)
- [Windows](#windows)

## Linux

### Ubuntu

1. **Install Docker**
   
   [Docker](https://www.docker.com/) is an open platform for developing, shipping, and running applications.
   
    - <details>
         <summary>Install using the Docker repository</summary>
      
         Follow the [official instruction from Docker](https://docs.docker.com/engine/install/ubuntu/) to verify prerequisites.
         Then, following the [steps outlined in the documentation](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)
         to install docker using the repository.

         - Validate successful installation by running `docker`. Output should look similar to below.
            ```
            Usage:  docker [OPTIONS] COMMAND

            A self-sufficient runtime for containers
            
            Options:
                  --config string      Location of client config files (default "/Users/antheaj/.docker")
              -c, --context string     Name of the context to use to connect to the daemon (overrides DOCKER_HOST env var and default context set with
                                       "docker context use")
              -D, --debug              Enable debug mode
              -H, --host list          Daemon socket(s) to connect to
              -l, --log-level string   Set the logging level ("debug"|"info"|"warn"|"error"|"fatal") (default "info")
                  --tls                Use TLS; implied by --tlsverify
                  --tlscacert string   Trust certs signed only by this CA (default "/Users/antheaj/.docker/ca.pem")
                  --tlscert string     Path to TLS certificate file (default "/Users/antheaj/.docker/cert.pem")
                  --tlskey string      Path to TLS key file (default "/Users/antheaj/.docker/key.pem")
                  --tlsverify          Use TLS and verify the remote
              -v, --version            Print version information and quit
            
            Run 'docker COMMAND --help' for more information on a command.
            
            To get more help with docker, check out our guides at https://docs.docker.com/go/guides/
           ```
      </details>

1. **Install Kustomize**
   
   [Kustomize](https://kustomize.io/) is a tool for customizing Kubernetes resource configuration free from templates and DSLs.

   To install [Kustomize version 3.2.0](https://github.com/kubernetes-sigs/kustomize/releases/tag/v3.2.0),
   - Download `kustomize_3.2.0_linux_amd64` by executing the command below
      ```
      wget https://github.com/kubernetes-sigs/kustomize/releases/download/v3.2.0/kustomize_3.2.0_linux_amd64
      ```
   - Make `kustomize` executable and move it to `/usr/local/bin` directory
      ```
      chmod +x kustomize_3.2.0_linux_amd64 && sudo mv kustomize_3.2.0_linux_amd64 /usr/local/bin/kustomize
      ```
   - Validate successful installation by running `kustomize`
      Output should look similar to below
      ```
      Manages declarative configuration of Kubernetes.
      See https://sigs.k8s.io/kustomize
      
      Usage:
        kustomize [command]
      
      Available Commands:
        build       Print configuration per contents of kustomization.yaml
        config      Config Kustomize transformers
        create      Create a new kustomization in the current directory
        edit        Edits a kustomization file
        help        Help about any command
        version     Prints the kustomize version
      
      Flags:
        -h, --help   help for kustomize
      
      Use "kustomize [command] --help" for more information about a command.
      ```

1. **Install kubectl**

   [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) is a Kubernetes command-line tool that
   allows you to run commands against Kubernetes clusters.
   
   To install kubectl,
   - Download the latest release with the command
      ```
      curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
      ```
   - Install [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/#install-kubectl-binary-with-curl-on-linux)
      ```
      sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
      ```
   - Validate successful installation by running `kubectl version`. Output should look similar to below.
      ```
      Client Version: version.Info{Major:"1", Minor:"21", GitVersion:"x.xx.x", GitCommit:"xxxxx", GitTreeState:"clean", BuildDate:"xxxx-xx-xxTxx:xx:xxx", GoVersion:"gx.xx.x", Compiler:"gc", Platform:"linux/amd64"}
      ```

1. **Install Kubernetes locally** </br>
   Choose **one** of the following options to install Kubernetes
    - <details>
         <summary>Kind</summary>

         [Kind](https://kind.sigs.k8s.io/) is a tool for running local Kubernetes clusters using Docker container “nodes”.
         
         1. Download kind
            ```
            curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.11.1/kind-linux-amd64
            chmod +x ./kind && sudo mv ./kind /usr/local/bin/kind
            ```
         1. Start Kubernetes Cluster
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
         1. Validate connection to Kubernetes cluster by running a `kubectl` command
            ```
            kubectl get nodes
            
            NAME                 STATUS   ROLES                  AGE   VERSION
            kind-control-plane   Ready    control-plane,master   57s   v1.21.1
            ```
         </details>

    - <details>
         <summary>Minikube</summary>
         
         [Minikube](https://minikube.sigs.k8s.io/) is a tool for running local Kubernetes clusters using a Hypervisor.

         1. Install [VMware Fusion](https://www.vmware.com/products/fusion.html)
            or [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
            or other hypervisors.

         1. Download minikube
            ```
            curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
            sudo install minikube-linux-amd64 /usr/local/bin/minikube
            ```
         1. Start Kubernetes Cluster
            ```
            minikube start --cpus 8 --memory 8000 --disk-size=128g
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
1. [Install Kubeflow](#install-kubeflow)
1. **Install Jupyter Notebook**
   
   **Note**: Jupyter Notebook installation is required only in case of standalone Kubeflow Pipelines installation.
   
   - Upgrade pip to the latest version
   
     ```pip install --upgrade pip```
   
   - Install the Jupyter Notebook:
   
     ```pip install jupyter```
   - Start the notebook server:
   
     ```jupyter notebook```
   - You should see the notebook open in your browser.

1. [Clean up](#clean-up)


## MacOS
1. **Install Docker**
   
   [Docker](https://www.docker.com/) is an open platform for developing, shipping, and running applications.
   
   Choose **one** of the following options to install docker
    - <details>
         <summary>Docker Desktop for Mac</summary>
      
         [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop) is a tool that enables you to build and share containerized applications and microservices.
      
         - Follow the [instructions](https://docs.docker.com/docker-for-mac/install/) to download the docker desktop.
         - Validate successful installation by running `docker`. Output should look similar to below.
            ```
            Usage:  docker [OPTIONS] COMMAND

            A self-sufficient runtime for containers
            
            Options:
                  --config string      Location of client config files (default "/Users/antheaj/.docker")
              -c, --context string     Name of the context to use to connect to the daemon (overrides DOCKER_HOST env var and default context set with
                                       "docker context use")
              -D, --debug              Enable debug mode
              -H, --host list          Daemon socket(s) to connect to
              -l, --log-level string   Set the logging level ("debug"|"info"|"warn"|"error"|"fatal") (default "info")
                  --tls                Use TLS; implied by --tlsverify
                  --tlscacert string   Trust certs signed only by this CA (default "/Users/antheaj/.docker/ca.pem")
                  --tlscert string     Path to TLS certificate file (default "/Users/antheaj/.docker/cert.pem")
                  --tlskey string      Path to TLS key file (default "/Users/antheaj/.docker/key.pem")
                  --tlsverify          Use TLS and verify the remote
              -v, --version            Print version information and quit
            
            Run 'docker COMMAND --help' for more information on a command.
            
            To get more help with docker, check out our guides at https://docs.docker.com/go/guides/
           ```
      </details>
    - <details>
         <summary>Homebrew</summary>
      
         [Homebrew](https://brew.sh/) is a software package manager that makes it easier to install software on macOS.
      
         - Download docker using brew
            ```
            brew install --cask docker
            ```
         - Validate successful installation by running `docker`. Output should look similar to below.
            ```
            Usage:  docker [OPTIONS] COMMAND

            A self-sufficient runtime for containers
            
            Options:
                  --config string      Location of client config files (default "/Users/antheaj/.docker")
              -c, --context string     Name of the context to use to connect to the daemon (overrides DOCKER_HOST env var and default context set with
                                       "docker context use")
              -D, --debug              Enable debug mode
              -H, --host list          Daemon socket(s) to connect to
              -l, --log-level string   Set the logging level ("debug"|"info"|"warn"|"error"|"fatal") (default "info")
                  --tls                Use TLS; implied by --tlsverify
                  --tlscacert string   Trust certs signed only by this CA (default "/Users/antheaj/.docker/ca.pem")
                  --tlscert string     Path to TLS certificate file (default "/Users/antheaj/.docker/cert.pem")
                  --tlskey string      Path to TLS key file (default "/Users/antheaj/.docker/key.pem")
                  --tlsverify          Use TLS and verify the remote
              -v, --version            Print version information and quit
            
            Run 'docker COMMAND --help' for more information on a command.
            
            To get more help with docker, check out our guides at https://docs.docker.com/go/guides/
           ```
      </details>
   
1. **Install Kustomize**
   
   [Kustomize](https://kustomize.io/) is a tool for customizing Kubernetes resource configuration free from templates and DSLs.
   
   To install Kustomize version 3.2.0,
    - Navigate [Kustomize release page](https://github.com/kubernetes-sigs/kustomize/releases/tag/v3.2.0) assets
      and download `kustomize_3.2.0_darwin_amd64`
    - Make `kustomize` executable and move it to `/usr/local/bin` directory
      ```
      chmod +x kustomize_3.2.0_darwin_amd64 && mv kustomize_3.2.0_darwin_amd64 /usr/local/bin/kustomize
      ```
   - Validate successful installation by running `kustomize`. Output should look similar to below.
      ```
      Manages declarative configuration of Kubernetes.
      See https://sigs.k8s.io/kustomize
      
      Usage:
        kustomize [command]
      
      Available Commands:
        build       Print configuration per contents of kustomization.yaml
        config      Config Kustomize transformers
        create      Create a new kustomization in the current directory
        edit        Edits a kustomization file
        help        Help about any command
        version     Prints the kustomize version
      
      Flags:
        -h, --help   help for kustomize
      
      Use "kustomize [command] --help" for more information about a command.
      ```
1. **Install kubectl**

   [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) is a Kubernetes command-line tool that
   allows you to run commands against Kubernetes clusters.
   
   - Install kubectl
      ```
      brew install kubectl 
      ```
   - Validate successful installation by running `kubectl version`. Output should look similar to below.
      ```
      Client Version: version.Info{Major:"1", Minor:"21", GitVersion:"x.xx.x", GitCommit:"xxxxx", GitTreeState:"clean", BuildDate:"xxxx-xx-xxTxx:xx:xxx", GoVersion:"x.xx.x", Compiler:"gc", Platform:"darwin/amd64"}
      ```
1. **Install [Kubernetes](https://kubernetes.io/) locally** </br>
   Choose **one** of the following options to install Kubernetes
    - <details>
         <summary>Kind</summary>
         
         [Kind](https://kind.sigs.k8s.io/) is a tool for running local Kubernetes clusters using Docker container “nodes”.

         1. Download kind using brew
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
      </details>
    - <details>
         <summary>Docker Desktop for Mac</summary>
         
         [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop) is a tool that enables you to build and share containerized applications and microservices.

         1. Download the [latest version of Docker Desktop for Mac](https://docs.docker.com/docker-for-mac/install/)
            and follow the [instructions to install and run Docker Desktop](https://docs.docker.com/docker-for-mac/install/#install-and-run-docker-desktop-on-mac)
         1. Navigate to [preferences -> resources](https://docs.docker.com/docker-for-mac/#resources)
            to modify the resource limit to (recommended) 8 CPU, 8 GB RAM, and 128GB Disk
         1. Navigate to [preferences to enable Kubernetes](https://docs.docker.com/desktop/kubernetes/#enable-kubernetes)
         1. Validate connection to Kubernetes cluster by running a `kubectl` command
            ```
            kubectl get nodes
            
            NAME             STATUS   ROLES                  AGE   VERSION
            docker-desktop   Ready    control-plane,master   1m    v1.21.2
            ```
      </details>
    - <details>
         <summary>Minikube</summary>
         
         [Minikube](https://minikube.sigs.k8s.io/) is a tool for running local Kubernetes clusters using a Hypervisor.
         
         1. Install [VMware Fusion](https://www.vmware.com/products/fusion.html)
            or [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
            or other hypervisors.
         
         1. Download minikube using brew
            ```
            brew install minikube
            ```
            or
            ```
            brew install --cask minikube
            ```
         1. Start Kubernetes Cluster
            ```
            minikube start --cpus 8 --memory 8000 --disk-size=128g
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
   </details>

## Windows

Coming Soon

## Install Kubeflow

The installation process for Kubeflow is the same for all operating systems.
Deploying the entire Kubeflow could be too heavy task for computers with 16 GB RAM or less. Depending on the hardware
resources, there are two ways to proceed. First to install the entire Kubeflow. Second, in case no enough resources, to
deploy just the Pipeline Component of the Kubeflow.

<details>
   <summary>Deploy Kubeflow</summary>

1. Create a directory `workspace` and clone the `kubeflow/manifest` repo.
    ```
    mkdir -p ~/workspace && cd ~/workspace;
    git clone https://github.com/kubeflow/manifests.git && cd manifests;
    ```
1. Modify `common/dex/base/deployment.yaml` file to include the following as a workaround for current problem
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

   It could take more than 20 mins for all pods to have status `Running`. Please wait for all pods to show
   status `Running` before continuing with validation.
    ```
    # Run the following to check status of all pods in kubeflow namespace
    kubectl get pod --all-namespaces
    ```

   Once all pods are running, the output of the above command should look similar to the example provided.
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
</details>

<details>
   <summary>Deploy Kubeflow Pipelines</summary>
   
1. Deploy the Kubeflow Pipelines by running the following commands:
   ```
   export PIPELINE_VERSION=1.6.0
   kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/cluster-scoped-resources?ref=$PIPELINE_VERSION"
   kubectl wait --for condition=established --timeout=60s crd/applications.app.k8s.io
   kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/env/platform-agnostic-pns?ref=$PIPELINE_VERSION"
   ```

2. Please wait for all pods to show status `Running` before continuing with validation. This could take a few minutes.
   ```
   # Run the following to check status of all pods in kubeflow namespace
   kubectl get pod --all-namespaces
   ```

   Once all pods are running, the output of the above command should look similar to the example provided.
   <details>
   <summary>Output Example</summary>
   
      ```
         NAMESPACE            NAME                                               READY   STATUS    RESTARTS   AGE
      kube-system          coredns-558bd4d5db-469wk                           1/1     Running   0          62m
      kube-system          coredns-558bd4d5db-fgzsb                           1/1     Running   0          62m
      kube-system          etcd-stendalone-control-plane                      1/1     Running   0          62m
      kube-system          kindnet-qsxdr                                      1/1     Running   0          62m
      kube-system          kube-apiserver-stendalone-control-plane            1/1     Running   0          62m
      kube-system          kube-controller-manager-stendalone-control-plane   1/1     Running   0          62m
      kube-system          kube-proxy-fk5sj                                   1/1     Running   0          62m
      kube-system          kube-scheduler-stendalone-control-plane            1/1     Running   0          62m
      kubeflow             cache-deployer-deployment-7d87b9bcdc-6fgvg         1/1     Running   0          61m
      kubeflow             cache-server-856bdbdbc4-ppbdg                      1/1     Running   0          61m
      kubeflow             metadata-envoy-deployment-6d85d9f7bd-zngkp         1/1     Running   0          61m
      kubeflow             metadata-grpc-deployment-bd844c9d8-qz68p           1/1     Running   8          61m
      kubeflow             metadata-writer-7c6b78494f-drcgc                   1/1     Running   3          61m
      kubeflow             minio-5b65df66c9-wzgz4                             1/1     Running   0          61m
      kubeflow             ml-pipeline-76d499ffcd-5k25g                       1/1     Running   8          61m
      kubeflow             ml-pipeline-persistenceagent-77b45fbc7-s4n2p       1/1     Running   5          61m
      kubeflow             ml-pipeline-scheduledworkflow-78d689554b-twm98     1/1     Running   0          61m
      kubeflow             ml-pipeline-ui-5d467774b8-kjfjr                    1/1     Running   0          61m
      kubeflow             ml-pipeline-viewer-crd-7b8c6657bd-wnr65            1/1     Running   0          61m
      kubeflow             ml-pipeline-visualizationserver-746bd47fd5-gzb74   1/1     Running   0          61m
      kubeflow             mysql-f7b9b7dd4-n45bx                              1/1     Running   0          61m
      kubeflow             workflow-controller-7d7d46cf8f-x5gt5               1/1     Running   0          61m
      local-path-storage   local-path-provisioner-547f784dff-7c9gt            1/1     Running   0          62m
      ```
   </details>


3. Verify that the Kubeflow Pipelines UI is accessible by port-forwarding:
   ```
   kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80
   ```
   After running the command, navigate to ```http://localhost:8080``` to login.
</details>

## Clean up
- [Kubeflow Resources](#kubeflow-resources)
- [Kubernetes Cluster](#kubernetes-cluster)

### Kubeflow Resources
1. Run the following commands to uninstall Kubeflow or Kubeflow Pipelines
   - Uninstall Kubeflow installation
   ```
   cd ~/workspace/manifests;
   kustomize build example | kubectl delete -f -;
   ```

   - Uninstall Kubeflow Pipelines
   
   ```
   export PIPELINE_VERSION=1.6.0
   kubectl delete -k "github.com/kubeflow/pipelines/manifests/kustomize/env/platform-agnostic-pns?ref=$PIPELINE_VERSION"
   kubectl delete -k "github.com/kubeflow/pipelines/manifests/kustomize/cluster-scoped-resources?ref=$PIPELINE_VERSION"
   ```
2. Validate the resource deletion by running `kubectl get pod --all-namespaces`
### Kubernetes Cluster
To stop running Kubernetes follow the instructions below based on how Kubernetes cluster was installed
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
