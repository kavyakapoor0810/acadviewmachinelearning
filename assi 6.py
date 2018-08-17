import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("https://raw.githubusercontent.com/Shreyas3108/Weather/master/weather.csv ")
data = data.dropna()
sns.distplot(data['Rainfall'], bins= 20)
sns.kdeplot(data['Sunshine'], shade=True)
sns.distplot(data['WindGustSpeed'], hist=False)
sns.countplot(data['RainToday'])
sns.boxplot(data['MaxTemp'])