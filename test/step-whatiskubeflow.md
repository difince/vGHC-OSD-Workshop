The Kubeflow project is dedicated to making Machine Learning easy to set up with Kubernetes, portable and scalable. The goal is not to recreate other services, but to provide a straightforward way for spinning up best of breed OSS solutions. Kubernetes is an open-source platform for automating deployment, scaling, and management of containerised applications.

Because Kubeflow relies on Kubernetes, it runs wherever Kubernetes runs such as bare-metal servers, or cloud providers such as Google. Details of the project can be found at https://github.com/kubeflow/kubeflow

### Kubeflow Components

Kubeflow has three core components.

__TF Job Operator and Controller__: Extension to Kubernetes to simplify deployment of distributed TensorFlow workloads. By using an Operator, Kubeflow is capable of automatically configuring the master, worker and parameterized server configuration. Workloads can be deployed with a TFJob.

__TF Hub__: Running instances of JupyterHub, enabling you to work with Jupyter Notebooks.

__Model Server__: Deploying a trained TensorFlow models for clients to access and use for future predictions.

These three models will be used to deploy different workloads in the following steps.
