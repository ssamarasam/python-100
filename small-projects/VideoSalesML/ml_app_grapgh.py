import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz
# from sklearn.tree import plot_tree

music_data = pd.read_csv('music.csv')
X = music_data.drop(columns=['genre'])
y = music_data['genre']

model = DecisionTreeClassifier()
model.fit(X, y)

export_graphviz(model, out_file='music-recommender.dot',
                feature_names=['age', 'gender'],
                class_names=sorted(y.unique()),
                label='all',
                rounded=True,
                      filled=True)
