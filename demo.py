import pandas as pd
import numpy as np

training_data = pd.read_csv('Data/clean_data/training_data.csv')
testing_data = pd.read_csv('Data/clean_data/testing_data.csv')

print(training_data['sex'].mode())
training_data.sex = training_data['sex'].fillna(training_data['sex'].mode()[0])
print(training_data.isnull().sum())