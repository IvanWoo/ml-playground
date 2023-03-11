import pickle
from sklearn import svm
from sklearn import datasets

# Load training data set
iris = datasets.load_iris()
X, y = iris.data, iris.target

# Train the model
clf = svm.SVC(gamma="scale")
clf.fit(X, y)

with open("iris-model.pickle", "wb") as f:
    pickle.dump(clf, f, protocol=pickle.HIGHEST_PROTOCOL)
