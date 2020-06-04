import time
from functools import reduce
import pandas as pd


def test():
    """this is my func # """
    print("this is my func")


print(time.time())
print(test.__doc__)

# reduce example
list1 = [4, 3, 2, 1, 10]
red = reduce(lambda x, y: x - y, list1)
print(red)


############
def sendEmail(to, sub, msg):
    # print(f"*********\nTo: {to}\nSubject: {sub}\nMessage: {msg} \n--------")
    # str=f"{to},{sub},{msg}"
    str = f"*********\nTo: {to}\nSubject: {sub}\nMessage: {msg} \n--------"
    return str


inp = pd.read_csv("C:/Users/pradeep/Desktop/pycharm_spark/input/email_details1.csv", skiprows=0)
inp.to_html('temp.html')
# in_df=pd.DataFrame(inp).("1","2","3")
print(inp)

for index, item in inp.iterrows():
    email = item['email']
    DOB = item['dob']
    name = item['name']
    sub = item['message']
    msg = f"Haapy Birthday {name} !!\n \t\t Wish you a successful year ahead"
    # print(f"Email To: {email},DOB:{DOB},Subject{sub},Message{msg},Name:{name}")
    email_details = sendEmail(email, sub, msg)
    print(email_details)
