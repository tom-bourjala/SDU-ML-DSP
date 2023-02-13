import pandas
from pandas import read_csv

df = read_csv('resources/dataset.csv')

# count every iteration of a symptom (all columns are named from Symptom_1 to Symptom_17)
count = dict()

for i in range(1, 18):
    for symptom in df['Symptom_' + str(i)]:
        if symptom in count:
            count[symptom] += 1
        else:
            count[symptom] = 1

for key, value in count.items():
    print(key, value)
