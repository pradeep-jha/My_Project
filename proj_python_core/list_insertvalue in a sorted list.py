list1=[2,3,4,8,10,12]
n=7
#insert n such that list remains sorted.

for i in list1:
    if i>n:
        index=list1.index(i)
        list1.insert(index,n)
        break
print(list1)