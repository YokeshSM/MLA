import pandas as pd
import numpy as np







l=[10,12,13,14,15,16,17,18,19]
d=pd.Series(l)
print(d)

t=(34,35,36)
#dt=pd.Series(t)
#print(dt)

arr=np.array([1,2,3,4,5,6,7,8])
d1=pd.Series(arr)
print(d1)

print(d[0:10:2])

dict_var={'a':1,'b':2,'c':3,'d':4}
d2=pd.Series(dict_var)
print(d2)

d3=pd.Series(np.arange(10,100,10))
print(d3)
print(d3[0:5])
print(d3[2:9:2])
print(d3[0:5])
print(d3[::5])
print(d3[7])


data=[['abc',1],['def',2],['ghi',3],['hij'],['klm','5']]
df1=pd.DataFrame(data)
print(df1)

df2=pd.DataFrame(data,columns=['A Grp','B Grp'],index=['A','B','C','D','E']) # changing the index & column name
print(df2)

df3={'name':['Math','Sci','Eng'],'marks':[80,80,80]}
df3=(pd.DataFrame(df3))
print(df3)
df3.columns=['Candidate','Age_in_years'] # change column name using attruute columns
df3=df3.rename({'Age_in_years':"Age_years"},axis=1,inplace=False)
print(type(df3))
#print(df4,'========')



dt=pd.read_csv("train.csv")
print(dt)

print(dt.head())
print(dt.columns)
dt['Pclass']
print(dt['Pclass'].unique())
print(dt.columns)
print(dt.shape)
print(dt.describe())
print(dt['Sex'].unique())
print(dt.describe(include='O'))
print(dt.info())

print(dt.loc[10:20,["Name","Age","Cabin"]])
print(dt.loc[[12,17,18],["Name","Age","Cabin"]])
print(dt.loc[dt["Age"]==80])
print(dt.loc[(dt["Age"]>40) & (dt["Sex"]=='male')])
print(dt.loc[(dt['Sex']=='female')& (dt['Pclass']==1) & (dt['Survived']==1)])
print(dt.iloc[1:6,1:6])
print(dt.iloc[1:6,1:6])
print('=========')
print(dt.iloc[::2,:])
print(dt.iloc[:,::2])
print(dt.Sex.value_counts())
print(dt.isnull().sum())