The final Component is the [model server](https://www.tensorflow.org/serving/). Once trained, the model can be used to perform predictions for the new data when it's published. By using Kubeflow, it's possible to access the server by deploying jobs to the Kubernetes infrastructure.

### Deploy Trained Model Server

The Kubeflow tf-serving provides the template for serving a TensorFlow model. This can be customised and deployed by using Ksonnet and defining the parameters based on your model.

Using environment variables, we're defining the names and path of where our trained model is located.

```
MODEL_COMPONENT=model-server
MODEL_NAME=inception
MODEL_PATH=/serving/inception-export
```{{execute}}

Using Ksonnet, it's possible to extend the Kubeflow _tf-serving_ component to match the requirements for the model.

```
cd ~/kubeflow_ks_app
ks generate tf-serving ${MODEL_COMPONENT} --name=${MODEL_NAME}
ks param set ${MODEL_COMPONENT} modelPath $MODEL_PATH

ks param set ${MODEL_COMPONENT} modelServerImage katacoda/tensorflow_serving
```{{execute}}

The parameters defined can be viewed via `ks param list`{{execute}}

This provides a script that can be deployed to the environment and make our model available to clients.

You can deploy the template to the defined Kubernetes cluster.

`ks apply default -c ${MODEL_COMPONENT}`{{execute}}

Clients will now be able to connect and access the trained data, see the pod running via `kubectl get pods`{{execute}}

### Image Classification

In this example, we use the pre-trained [Inception V3](https://github.com/tensorflow/models/tree/master/research/inception) model. It's the architecture trained on [ImageNet](http://www.image-net.org/) dataset. The ML task is image classification while the model server and its clients being handled by Kubernetes.

To use the published model, you need to set up the client. This can be achieved the same way as other jobs. The YAML file for deploying the client is `cat ~/model-client-job.yaml`{{execute}}. To deploy it use the following command:

`kubectl apply -f ~/model-client-job.yaml`{{execute}}

To see the status of the __model-client-job__ run:

`kubectl get pods`{{execute}}

The command below will output the classification results for the [Katacoda logo](https://katacoda.com/kubeflow/scenarios/deploying-kubeflow/assets/katacoda.jpg).

`kubectl logs $(kubectl get pods | grep Completed | tail -n1 |  tr -s ' ' | cut -d ' ' -f 1)`{{execute}}

More information on serving models via Kubernetes can be found at https://github.com/kubeflow/kubeflow/tree/master/components/k8s-model-server
