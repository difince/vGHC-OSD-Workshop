import kfp
from kfp import dsl


@dsl.pipeline(
    name='iris-classification',
    description='A basic pipeline example for iris classification'
)
def iris_classification_pipeline():
    tree = dsl.ContainerOp(
        name="Train using Decision Tree",
        image="annajung/iris:latest",
        command=["sh", "-c"],
        arguments=["python iris_classification.py build_model tree"],
        file_outputs={'output': '/tmp/accuracy_tree.txt'}
    )

    knn = dsl.ContainerOp(
        name="Train using K Nearest Neighbors",
        image="annajung/iris:latest",
        command=["sh", "-c"],
        arguments=["python iris_classification.py build_model knn"],
        file_outputs={'output': '/tmp/accuracy_knn.txt'}
    )

    svm = dsl.ContainerOp(
        name="Train using Support Vector Machine",
        image="annajung/iris:latest",
        command=["sh", "-c"],
        arguments=["python iris_classification.py build_model svm"],
        file_outputs={'output': '/tmp/accuracy_svm.txt'}
    )

    # outputs = {"tree": tree.output, "knn": knn.output, "svm": svm.output}
    # best_model = max(outputs, key=outputs.get)

    with dsl.Condition(tree.output >= knn.output and tree.output >= svm.output):
        c = dsl.ContainerOp(
            name='Train Tree',
            image="annajung/iris:latest",
            command=['sh', '-c'],
            arguments=['python3  iris_classification.py save_final_model tree'],
            file_outputs={'output': '/tmp/tree.pkl'},
        )

    with dsl.Condition(knn.output >= tree.output and knn.output >= svm.output):
        c = dsl.ContainerOp(
            name='Train KNN',
            image="annajung/iris:latest",
            command=['sh', '-c'],
            arguments=['python3  iris_classification.py save_final_model knn'],
            file_outputs={'output': '/tmp/knn.pkl'},
        )

    with dsl.Condition(svm.output >= tree.output and svm.output >= knn.output):
        c = dsl.ContainerOp(
            name='Train SVM',
            image="annajung/iris:latest",
            command=['sh', '-c'],
            arguments=['python3  iris_classification.py save_final_model svm'],
            file_outputs={'output': '/tmp/svm.pkl'},
        )

    dsl.get_pipeline_conf().set_ttl_seconds_after_finished(500)


if __name__ == '__main__':
    kfp.compiler.Compiler().compile(iris_classification_pipeline, __file__ + '.yaml')