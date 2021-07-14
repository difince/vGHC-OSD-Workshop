With Kubeflow being an extension to Kubernetes, all the components need to be deployed to the platform. 

The team have provided an installation script which uses Ksonnet to deploy Kubeflow to an existing Kubernetes cluster. Ksonnet requires a valid Github token. The following can be used within Katacoda. Run the command to set the required environment variable.

`
export PIPELINE_VERSION=1.6.0
`{{execute}}

Once installed, you can run the installation script:


`
kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/cluster-scoped-resources?ref=$PIPELINE_VERSION"
`{{execute}}

`
kubectl wait --for condition=established --timeout=60s crd/applications.app.k8s.io
`{{execute}}

`kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/env/platform-agnostic-pns?ref=$PIPELINE_VERSION"
`{{execute}}

The Kubeflow Pipelines deployment may take several minutes to complete.
You should see the Kubeflow pods starting.

`kubectl get pods`{{execute}}

Verify that the Kubeflow Pipelines UI is accessible by port-forwarding:
`kubectl port-forward --address 0.0.0.0 -n kubeflow svc/ml-pipeline-ui 8080:80"
`{{execute}}

## Create Persistent Volume and Services for Katacoda
##To ensure Kubeflow runs successfully on Katacoda, deploy the following extensions.

##`kubectl apply -f ~/kubeflow/katacoda.yaml`{{execute}}

##This will create the LoadBalancer and Persistent Volume required by Kubeflow. This will vary based on your environment.