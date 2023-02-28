from sklearn import linear_model
import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt
import pickle

df=pd.read_csv("inputs/home.csv")
print(df.columns)
print(df)
plt.xlabel('area')
plt.ylabel('price')
plt.scatter(df.area,df.price)
plt.show()

reg=linear_model.LinearRegression()
reg.fit(df[['area']],df.price)
print(reg.predict([[3600]]))
print(reg.predict([[3600]])[0])
m=reg.coef_
print(m)
c=reg.intercept_
print(c)

# calculation for predicted value
#y=mx+c
#m=coef or slope or gradient decent,c=intecept
value=m*3600+c
print("calulated value",value)

#### to save the model####
# with open('model_pickle','wb') as f:
#     pickle.dump(reg,f)

with open('model_pickle','rb') as f:
    mp=pickle.load(f)

print(mp.predict([[5000]]))
