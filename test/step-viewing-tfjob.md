The status of TensorFlow jobs can be viewed via `kubectl get tfjob`{{execute}}. Once the TensorFlow job has been completed, the master is marked as successful. Keep running the job command to see when it finishes.

The master is responsible for coordinating the execution and aggregating the results. Under the covers, the completed workloads can be listed using `kubectl get pods | grep Completed`{{execute}}

In this example, the results are outputted to STDOUT, viewable using `kubectl logs`.

The command below will output the results:

`kubectl logs $(kubectl get pods | grep Completed | tr -s ' ' | cut -d ' ' -f 1)`{{execute}}

You will see the results from the execution of the workload on the master, worker and parameter servers.
