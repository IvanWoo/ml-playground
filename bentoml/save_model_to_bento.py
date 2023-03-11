import pickle
import bentoml

with open("iris-model.pickle", "rb") as handle:
    clf = pickle.load(handle)

# Save model to the BentoML local model store
saved_model = bentoml.sklearn.save_model("iris_clf", clf)
print(f"Model saved: {saved_model}")
