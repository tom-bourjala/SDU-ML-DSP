import pandas
from pandas import read_csv
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
import numpy as np

df = read_csv('resources/dataset.csv')

symptoms = []

for i in range(1, 18):
    for symptom in df['Symptom_' + str(i)]:
        if symptom not in symptoms:
            symptoms.append(symptom)

diseases = []

for disease in df['Disease']:
    if disease not in diseases:
        diseases.append(disease)

df_diseases = pandas.DataFrame(columns=['Disease'])
df_symptoms = pandas.DataFrame(columns=symptoms)

for i in range(0, len(df)-1):
    disease = df['Disease'][i]
    rawSymptoms = []
    for j in range(1, 18):
        symptom = df['Symptom_' + str(j)][i]
        if not pandas.isnull(symptom):
            rawSymptoms.append(symptom)
    df_diseases.loc[i] = diseases.index(disease)
    df_symptoms.loc[i] = [1 if symptom in rawSymptoms else 0 for symptom in symptoms]

# Remove all columns names
df_diseases_without_columns = df_diseases.iloc[:, 0]
df_symptoms_without_columns = df_symptoms.iloc[:, 0:]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df_symptoms_without_columns, df_diseases_without_columns, test_size=0.9, random_state=42)

# Convert feature names to strings
X_train.columns = X_train.columns.astype(str)
X_test.columns = X_test.columns.astype(str)

# Set up the parameter grid to search
param_grid = {'n_neighbors': [3, 5, 7, 9, 11]}

# Create a K-NN classifier object
knn = KNeighborsClassifier()

# Set up the grid search
grid_search = GridSearchCV(knn, param_grid, cv=5)

# Fit the grid search to the training data
grid_search.fit(X_train, y_train)

# Print the best parameters and the corresponding score
print("Best parameters: ", grid_search.best_params_)
print("Best score: ", grid_search.best_score_)

# Use the best model to make predictions on the test data
y_pred = grid_search.predict(X_test)

# Print the classification report
target_names = [str(disease) for disease in diseases]
print(classification_report(y_test, y_pred, target_names=target_names))