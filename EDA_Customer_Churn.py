import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Customer_Churn_origin.csv')

#replacing blank values with 0 because tenure is 0 so there are not records
df["TotalCharges"] = df["TotalCharges"].replace(" ", "0")
df["TotalCharges"] = df["TotalCharges"].astype("float")

print(df)
print()
print(df.head())
print()
print(df.info())
print()

#There is no null values in table
print(f"Count of null values: {df.isnull().sum().sum()}")
print()

print(df.describe())
print()

#There are no duplicates in whole table
print(f"Count duplicates of whole table: {df.duplicated().sum()}\n")

def conv(value):
    return 'Yes' if value==1 else 'No'

#convert bool values 0/1 to Yes/No to make it easier to understand
df['SeniorCitizen']=df['SeniorCitizen'].apply(conv)
print(df.head())


# ax=sns.countplot(x='Churn', data=df)
# ax.bar_label(ax.containers[0])
# plt.title('Count of customers by Churn')



#gb = df.groupby('Churn').agg({'Churn':'count'})
#plt.pie(gb['Churn'], labels=gb.index, autopct='%1.2f%%')
#plt.title('Percentage of churned customers', fontsize=20)

plt.figure(figsize=(4,4))
plt.title("Churn by Genders")
ax=sns.countplot(x='gender', data=df, hue='Churn')
ax.bar_label(ax.containers[0])
plt.show()