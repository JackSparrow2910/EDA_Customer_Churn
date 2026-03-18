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

# plt.figure(figsize=(4,4))
# plt.title("Churn by Genders")
# ax=sns.countplot(x='gender', data=df, hue='Churn')
# ax.bar_label(ax.containers[0])

# plt.figure(figsize=(4,4))
# plt.title("Churn by Senior Citizen")
# ax=sns.countplot(x='SeniorCitizen', data=df, hue='Churn')
# ax.bar_label(ax.containers[0])
# plt.show()

# total_counts = df.groupby('SeniorCitizen')['Churn'].value_counts(normalize=True).unstack()*100
#
# fig, ax = plt.subplots(figsize=(6,6))
#
# total_counts.plot(kind='bar', stacked=True, ax=ax, color=['#1f77b4', '#ff7f0e'])
#
# for p in ax.patches:
#     width, height = p.get_width(), p.get_height()
#     x,y = p.get_xy()
#     ax.text(x + width/2,y + height/2,f'{height:.1f}%', ha='center',va='center')

# plt.title("Churn by Senior Citizen (Stacked Bar Chart)")
# plt.xlabel("SeniorCitizen")
# plt.ylabel("Churn (%)")
# plt.xticks(rotation=0)
# plt.legend(title='Churn', loc='upper right', bbox_to_anchor=(1.05, 1))

sns.histplot(x='tenure', data=df, bins=72, hue='Churn')
plt.show()
