import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])
#
# plt.plot(xpoints, ypoints)
# plt.show()

df=pd.read_csv("C:\\Users\\PRADEEP\\PycharmProjects\\First_Project\\pySparkProject\\inputs\\nba.csv")
df2=df.head(1000)
df2.dropna(inplace=True)
df2.astype({'SCORE':int})
print(df2.count())
print(df2.dtypes)
df2.plot(x='GAME_ID',y='SCORE',kind='bar')
plt.show()