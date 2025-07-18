# -*- coding: utf-8 -*-
"""Mental Health Mood Tracker with Insights.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zN1oBPu988FlgWsuHjcT7cFrxiHSQCwl
"""

import pandas as pd
import numpy as np

data=pd.read_csv("/content/Mental Health Dataset.csv")
data.head(10)

data.info()

data.isna().mean()*100

data.dropna(subset=["self_employed"],inplace=True)

print("duplicated",data.duplicated().mean()*100)
data.drop_duplicates(inplace=True)

print("duplicated",data.duplicated().mean()*100)
data.drop_duplicates(inplace=True)

data.head(10).T

data["Timestamp"]=pd.to_datetime(data.Timestamp)
data["Years"]=data["Timestamp"].dt.year

data["month"]=data["Timestamp"].dt.month
data["day"]=data["Timestamp"].dt.day_name

data.dtypes

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

sns.countplot(data=data,x="Gender",)
plt.title('Distribution of Gender in Mental Health Data')
plt.show

sns.countplot(data=data,x="Country",)
plt.xticks(rotation=90)
plt.title('Distribution of Countries in Mental Health Data')
plt.show()

sns.countplot(data=data,x="Occupation")
plt.title('Distribution of Occupation in Mental Health Data')
plt.show()

sns.countplot(data=data,x="self_employed")
plt.title('Distribution of Occupation in Mental Health Data')
plt.show()

data.columns

genderBycountery=data.groupby("Country")["Gender"].value_counts().unstack(fill_value=0)
genderBycountery

genderBycountery["Total"]=genderBycountery.sum(axis=1)

genderBycountery

gender_stress_counts=data.Gender.value_counts()
print(f"gender_stress_counts {gender_stress_counts} \n")

genderBy_stress=data.groupby("Gender")["Growing_Stress"].value_counts().unstack()
genderBy_stress

data.columns

OccupationBy_stress=data.groupby("Occupation")["Growing_Stress"].value_counts().unstack()
OccupationBy_stress

OccupationBy_gender_stress=data.groupby(["Occupation","Gender"])["Growing_Stress"].value_counts().unstack()
OccupationBy_gender_stress

OccupationBy_gender_stress["Total"]=OccupationBy_gender_stress.sum(axis=1)
OccupationBy_gender_stress

occupation_gender_stress_prop = OccupationBy_gender_stress.div(OccupationBy_gender_stress['Total'], axis=0)
occupation_gender_stress_prop = occupation_gender_stress_prop.drop('Total', axis=1)
occupation_gender_stress_prop

sns.heatmap(occupation_gender_stress_prop,annot=True,cmap="YlGnBu")
plt.xlabel("Growing Stress")
plt.ylabel("Occupation-Gender")
plt.title("Proportion of Growing Stress by Occupation and Gender")
plt.show()

treatment_by_gender = data.groupby('Gender')['treatment'].value_counts(normalize=True).unstack() * 100
print(treatment_by_gender)

treatment_by_gender.plot(kind='bar', stacked=True, colormap='viridis')
plt.ylabel('Percentage')
plt.title('Mental Health Treatment by Gender')
plt.show()

treatment_by_country = data.groupby('Country')['treatment'].value_counts(normalize=True).unstack() * 100
treatment_by_country.plot(kind='bar', stacked=True, colormap='Set2', figsize=(12,6))
plt.ylabel('Percentage')
plt.title('Mental Health Treatment by Country (Top 10)')
plt.xticks(rotation=45)
plt.show()

crosstab = pd.crosstab(data['self_employed'], data['treatment'], normalize='index') * 100
print(crosstab)

crosstab.plot(kind='bar', stacked=True, )
plt.ylabel('Percentage')
plt.title('Self-employed vs. Mental Health Treatment')
plt.show()