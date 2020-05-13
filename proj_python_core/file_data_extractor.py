import os

dirpath = os.getcwd()
foldername = os.path.basename(dirpath)
print("Directory name is : " + foldername)
scriptpath = os.path.realpath(__file__)
print("Script path is : " + scriptpath)
file_name=os.path.basename(__file__)
print("file_name is: "+file_name)

files=os.listdir(dirpath)
pyfiles=[]
for file in files:
    list1=file.split(".")
    if(len(list1)>=2):
        if (list1[1]=='py'):
            pyfiles.append(file)
print("py files are: #########")
print(pyfiles)

my_dict = {}
file1 = open(dirpath+"/"+"python_practice_prog.txt", "w+")
for file in pyfiles:
        with open(file) as f:
            #items = [i.strip() for i in f.read().split(",")]
            key=file.replace(".py", "")
            my_dict[key] = f.read()
            #print(my_dict[key])

            #print(f.read())
            #print(type(file))
            print("############ Writing the content of file :"+file +" #############\n")
            file1.writelines("############ Writing the content of file :"+file +" #############\n")
            file1.writelines((my_dict[key]) +"\n")

file1.close()

