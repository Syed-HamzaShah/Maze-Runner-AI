import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

def train_and_save_model():
    df = pd.read_csv('data/danger_data.csv')
    X = df.drop('danger', axis=1)
    y = df['danger']
    model = DecisionTreeClassifier()
    model.fit(X, y)

    with open('models/decision_tree.pkl', 'wb') as f:
        pickle.dump(model, f)

def load_model():
    with open('models/decision_tree.pkl', 'rb') as f:
        return pickle.load(f)

if __name__ == "__main__":
    train_and_save_model()