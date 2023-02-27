import pandas
from pandas import read_csv

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

df_diseases = pandas.DataFrame(columns=diseases)
df_symptoms = pandas.DataFrame(columns=symptoms)

for i in range(0, 20):
    disease = df['Disease'][i]
    rawSymptoms = []
    for j in range(1, 18):
        symptom = df['Symptom_' + str(j)][i]
        # append if not nan
        if not pandas.isnull(symptom):
            rawSymptoms.append(symptom)
    # append the raw data, putting the disease and symptom raw to 1 if it is present, else 0
    df_diseases.loc[i] = [1 if disease == d else 0 for d in diseases]
    df_symptoms.loc[i] = [1 if symptom in rawSymptoms else 0 for symptom in symptoms]

print(df_diseases)
print(df_symptoms)

# %%
