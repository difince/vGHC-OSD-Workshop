import joblib
from sklearn import datasets
from sklearn import neighbors
from sklearn import svm
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def download_data():
    iris_dataset = datasets.load_iris()
    X = iris_dataset.data
    y = iris_dataset.target
    return X, y


def split_data(X, y, test_size=0.25):
    return train_test_split(X, y, test_size=test_size)


def build_model(model=""):
    X, y = download_data()
    X_train, X_test, y_train, y_test = split_data(X, y)

    if model == "knn":
        classifier = neighbors.KNeighborsClassifier()
    elif model == "svm":
        classifier = svm.SVC()
    else:
        model = "tree"
        classifier = tree.DecisionTreeClassifier()

    classifier.fit(X_train, y_train)

    predictions = classifier.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print("Accuracy for {}: {}".format(model, accuracy))

    text_file = open("/tmp/accuracy_{}.txt".format(model), "w")
    text_file.write("{}".format(accuracy))
    text_file.close()

    return classifier


def save_final_model(model=""):
    classifier = build_model(model)
    joblib.dump(classifier, "/tmp/{}.pkl".format(model))


if __name__ == '__main__':
    import sys

    globals()[sys.argv[1]](sys.argv[2])