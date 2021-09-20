import joblib
from sklearn import datasets
from sklearn import neighbors
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def build_model(model="", parameter=""):
    iris_dataset = datasets.load_iris()
    X = iris_dataset.data
    y = iris_dataset.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

    if model == "knn":
        classifier = neighbors.KNeighborsClassifier(n_neighbors=int(parameter))
    else:
        model = "tree"
        classifier = tree.DecisionTreeClassifier(splitter=parameter)

    classifier.fit(X_train, y_train)

    predictions = classifier.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print("Accuracy for {}: {}".format(model, accuracy))

    text_file = open("/tmp/accuracy_{}.txt".format(model), "w")
    text_file.write("{}".format(accuracy))
    text_file.close()

    return classifier


def save_final_model(model="", parameter=""):
    classifier = build_model(model, parameter)
    joblib.dump(classifier, "/tmp/{}.pkl".format(model))


if __name__ == '__main__':
    import sys

    globals()[sys.argv[1]](sys.argv[2], sys.argv[3])
