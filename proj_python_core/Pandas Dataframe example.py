import pandas as pd
tuple1=[(1,2,3,4,5),(1,2,3,4,5),(1,2,3,4,5)]
set1={1,2,4,3,4,5}
list1=[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
print("set1 \n",set1)
print("tuple1 \n",tuple1)
print("list1 \n",list1)

df1=pd.DataFrame(tuple1,columns=['A','B','C','D','E'],index=['x','Y','Z'])
df2=pd.DataFrame(set1)
df3=pd.DataFrame(list1)

print(df1)
print(df2)
print(df3)
