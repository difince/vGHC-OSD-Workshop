The main Kubeflow capability is to easily deploy TensorFlow code that had been packaged as a Docker Image.

In this step, we'll deploy our first TensorFlow workload that performs a matrix multiplication across the defined workers and parameter servers.

You can see the main execution code-snippet below:

<pre class="file">
for job_name in cluster_spec.keys():
  for i in range(len(cluster_spec[job_name])):
    d = "/job:{0}/task:{1}".format(job_name, i)
    with tf.device(d):
      a = tf.constant(range(width * height), shape=[height, width])
      b = tf.constant(range(width * height), shape=[height, width])
      c = tf.multiply(a, b)
      results.append(c)
</pre>

The complete example can be viewed at https://github.com/tensorflow/k8s/tree/master/examples/tf_sample
