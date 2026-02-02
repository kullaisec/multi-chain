import pickle

def process_image(path):
    if path.endswith(".pkl"):
        with open(path, "rb") as f:
            pickle.load(f)