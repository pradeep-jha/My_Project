'''*****diactionalr********'''
data = {
    "Bob": 23,
    "Charlie": 36,
    "Alice": 72,
    "Eric": 18,
    "David": 9
}
''' long way'''
print("original dictionar")
print(data)
l=[]
for x in data:
    print(x)
    l.append(x)
print(l)
l.sort()
print(l)
sorted_dict={}
for i in l:
    print(i,data[i])
    sorted_dict.update({i:data[i]})
    print(sorted_dict)

print("final sorted dictionary---")
print(sorted_dict)
print(type(data))
print(data)
''' *******sort way*******'''
sort_by_key=sorted(data.items(),key=lambda x:x[0],reverse=True)
print(sort_by_key)
new_dict_sorted={}
for i in sort_by_key:
    print(i)
    new_dict_sorted.update({i[0]:i[1]})

print("Original Dictionary.......")
print(data)
print("Sorted Dictioanr in decending order.......")
print(new_dict_sorted)

'''*****List sorting*******'''

list1=['*','+','(','^','-','/']
list2=list1.copy()
print("Original List...")
print(list2)
print("Sorted List...")
list2.sort(reverse=True)
print(list2)
list3=[1,'pradeep',45,'A',333,'Rochel',3.5]
print(list3)
str_list3=[str(i) for i in list3] #list comprehension

l4=sorted(list3,key=str)
print("printing L4")
print(l4)
print(str_list3)
str_list3.sort()
print(str_list3)
''' Work oround for BODMAS sorting
n=len(list)
a='('
b='^'
c='/'
d='*'
e='+'
f='-'
print(list)
l2=[a,b,c,d,e,f]
print(l2)
dct2={}
for j in l2:
        dct2.update({l2.index(j):j})
        # print(dct2)
print(dct2)
new_dct2=sorted(dct2.items(),key=lambda y:y[0],reverse=True)
print(new_dct2)
dict3={}
for x in new_dct2:
    dict3.update({x[0]:x[1]})
print(dict3)

# print("a..",ord('a'))
# print("A..",ord('A'))
# for i in list:
#     print(i,"....",ord(i))
# list.sort()
# print(list)
********'''

'''****Touple sorting'''
touple1=(1,1,'pradeep',45,'A',333,'Rochel',3.5,False,'',True)
print(type(touple1))
print(touple1)
print(len(touple1))
print(touple1.count(1))
list_touple=list(touple1)
print(list_touple)
'''convering list to string'''
str_list_touples=[str(x) for x in list_touple]
# str_list_touples.sort()
# out_list=sorted(str_list_touples,key=lambda e: (0,int(e)) if str.isdigit(e) else(1,e))

'''****** Working solution to sort mixed type of python list****'''
out_list=sorted(list_touple,key=lambda v: (isinstance(v, str), v.lower()) if isinstance(v, str) else (isinstance(v, str), v) )
print("sorted list using string comprehension...")
print(out_list)
print(str_list_touples)
a=False

