import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
import joblib
music_data = pd.read_csv('music.csv')
# music_data

# X = music_data.drop(columns=['genre'])
# y = music_data['genre']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# X_train

# model = DecisionTreeClassifier()
# model.fit(X_train, y_train)
# music_data

# joblib.dump(model, 'music-recommender.joblib')
# predictions = model.predict(X_test)
# predictions

trained_model = joblib.load('music-recommender.joblib')
predictions_trained = trained_model.predict(X_test)
predictions_trained

# y_test

score = accuracy_score(y_test, predictions_trained)
# score
