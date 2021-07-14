The second key component of Kubeflow is the ability to run Jupyter Notebooks via JupyterHub. [Jupyter Notebook](http://jupyter.org/) is the classic data science tool to run inline scripts and code snippets while documenting the process in the browser.

With Kubeflow the JupyterHub is deployed onto the Kubernetes cluster. You can find there the Load Balancer IP address using `kubectl get svc`{{execute}}

## Open Jupyter Hub

Via Katacoda, you can access the browser interface at the following link https://[[HOST_SUBDOMAIN]]-80-[[KATACODA_HOST]].environments.katacoda.com or using the terminal *Jupyterhub* tab. To access the JupyterHub use the username **`admin`{{copy}}** and a blank password in the login form.

To deploy a notebook, a new server has to be started. Kubeflow is using internally the **`gcr.io/kubeflow-images-public/tensorflow-1.8.0-notebook-cpu:v0.2.1`{{copy}}** Docker Image as default. After accessing the JupyterHub, you can click **Start My server** button.

The server launcher allows you to configure additional options, such as resource requirements. In this case, accept the defaults and click **Spawn** to start the server. Now you can see the contents of the Docker image that you can navigate, extend and work with Jupyter Notebooks.

Under the covers, this will Spawn a new Kubernetes Pod called *jupyter-admin* for managing the server. View this using `kubectl get pods jupyter-admin`{{execute}}

### Working with Jupyter Notebook

JupyterHub can now be accessed via the pod. You can now work with the environment seamlessly. For example to create a new notebook, select the New dropdown, and select the Python 3 kernel as shown below.

<img src="/kubeflow/scenarios/deploying-kubeflow/assets/jupyterhub-create-notebook.png" alt="Create New Jupyter Notebook">

It's now possible to create code snippets. To start working with TensorFlow, paste the code below to the first cell and run it.

<pre class="file" data-target="clipboard">
from __future__ import print_function

import tensorflow as tf

hello = tf.constant('Hello TensorFlow!')
s = tf.Session()
print(s.run(hello))
</pre>
