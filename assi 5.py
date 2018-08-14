import pandas as pan
#a
data=pan.read_csv('assi5raw.csv')
print(data.isnull().sum())
#b
data=data.dropna() #drop the missing values
print(data.isnull().sum())
#c
data1=pan.read_csv('assi5raw.csv')#to fill missing with mean
print(data1.fillna(data1.mean()))
#d
print(data1.dtypes)
data3=pan.Series(data1=data.MaxTemp)
print(data3)