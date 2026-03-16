import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Customer_Churn_origin.csv')
print(df.head())
print(df.info())

#replacing blank values with 0 because tenure is 0 so there are not records
df["TotalCharges"] = df["TotalCharges"].replace(" ", "0")
df["TotalCharges"] = df["TotalCharges"].astype("float")

#There is no null values in table
print(df.isnull().sum().sum())