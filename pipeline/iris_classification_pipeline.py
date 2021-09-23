import kfp
from kfp import dsl


@dsl.pipeline(
    name='iris-classification',
    description='A basic pipeline example for iris classification'
)
def iris_classification_pipeline(n_neighbors=2, splitter="random"):
    tree = dsl.ContainerOp(
        name="Train using Decision Tree",
        image="annajung/iris:latest",
        command=["sh", "-c"],
        arguments=["python iris_classification.py build_model tree " + str(splitter)],
        file_outputs={'output': '/tmp/accuracy_tree.txt'}
    )

    knn = dsl.ContainerOp(
        name="Train using K Nearest Neighbors",
        image="annajung/iris:latest",
        command=["sh", "-c"],
        arguments=["python iris_classification.py build_model knn " + str(n_neighbors)],
        file_outputs={'output': '/tmp/accuracy_knn.txt'}
    )

    with dsl.Condition(tree.output >= knn.output):
        dsl.ContainerOp(
            name='Train Tree',
            image="annajung/iris:latest",
            command=['sh', '-c'],
            arguments=["python3  iris_classification.py save_final_model tree " + str(splitter)],
            file_outputs={'output': '/tmp/tree.pkl'},
        )

    with dsl.Condition(knn.output > tree.output):
        dsl.ContainerOp(
            name='Train KNN',
            image="annajung/iris:latest",
            command=['sh', '-c'],
            arguments=["python3  iris_classification.py save_final_model knn " + str(n_neighbors)],
            file_outputs={'output': '/tmp/knn.pkl'},
        )

    dsl.get_pipeline_conf().set_ttl_seconds_after_finished(500)


if __name__ == '__main__':
    kfp.compiler.Compiler().compile(iris_classification_pipeline, __file__ + '.yaml')
