# import pandas as pd
#
# f1 = pd.read_csv("C:\\Users\\PRADEEP\\Desktop\\Python_Projects\\file_1.csv")
# f2 = pd.read_csv("C:\\Users\\PRADEEP\\Desktop\\Python_Projects\\file_2.csv")
# print(f1)
# print(f2)


with open("C:\\Users\\PRADEEP\\Desktop\\Python_Projects\\file_1.csv", 'r') as t1, open("C:\\Users\\PRADEEP\\Desktop\\Python_Projects\\file_2.csv", 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

    for line in filetwo:
        print("loop-1")
        print(line)
        if line not in fileone:
            print("loop-2")
            print(line)

# with open('update.csv', 'w') as outFile:
#     for line in filetwo:
#         print(line)
#         if line not in fileone:
#             outFile.write(line)