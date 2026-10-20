import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("Unemployment.csv")
print(df.head())
print(df.info())
print(df.isnull().sum())
df.columns=df.columns.str.strip()
df["Date"]=pd.to_datetime(df["Date"],dayfirst=True)
df.dropna(inplace=True)
print(df.isnull().sum())

print("covid data cleaning")
df1=pd.read_csv("Unemployment_Rate_upto_11_2020.csv")
print(df1.head())
print(df1.info())
print(df1.isnull().sum())
df1.columns=df1.columns.str.strip()
df1["Date"]=pd.to_datetime(df1["Date"],dayfirst=True)
df1.dropna(inplace=True)
print(df1.isnull().sum())
df1['Month'] = df1['Date'].dt.month_name()
df1['Year'] = df1['Date'].dt.year
df1[['Date', 'Month', 'Year']].head()
#visualization the data
plt.figure(figsize=(10, 5))
sns.lineplot(data=df1, x='Date', y='Estimated Unemployment Rate (%)', marker='o', color='red')
plt.title('Unemployment Rate Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)
plt.show()
# Separate data before and during Covid lockdown
pre_covid = df1[df1['Date'] < '2020-03-01']['Estimated Unemployment Rate (%)'].mean()
covid_peak = df1[(df1['Date'] >= '2020-03-01') & (df1['Date'] <= '2020-06-30')]['Estimated Unemployment Rate (%)'].mean()
print(f"Average Unemployment Before Covid: {pre_covid:.2f}%")
print(f"Average Unemployment During Covid Peak: {covid_peak:.2f}%")
plt.figure(figsize=(12, 6))
# Sort states by highest average unemployment rate
state_order = df1.groupby('Region')['Estimated Unemployment Rate (%)'].mean().sort_values(ascending=False).index
sns.barplot(data=df1, x='Region', y='Estimated Unemployment Rate (%)', order=state_order,hue='Region', palette='viridis')
plt.xticks(rotation=90)
plt.title('Average Unemployment Rate by Region/State')
plt.xlabel('Region')
plt.ylabel('Unemployment Rate (%)')
plt.show()
plt.figure(figsize=(10, 5))
sns.barplot(data=df1, x='Month', y='Estimated Unemployment Rate (%)', hue='Month', palette='mako')
plt.title('Monthly / Seasonal Unemployment Trends')
plt.show()
if 'Area' in df.columns:
    plt.figure(figsize=(6, 4))
    sns.barplot(data=df, x='Area', y='Estimated Unemployment Rate (%)', hue='Area',palette='Set2')
    plt.title('Rural vs Urban Unemployment Rate')
    plt.show()
print("\n=== KEY ECONOMIC & POLICY INSIGHTS ===")
print("1. Covid Spike: Unemployment jumped significantly during peak lockdowns (April-May 2020).")
print("2. Regional Impact: Certain states consistently faced higher joblessness than others.")
print("3. Policy Advice: Emergency funds and economic relief programs should prioritize heavily impacted sectors and regions.")


