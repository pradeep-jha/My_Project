import string
import random
def paas_gen():
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    try:
        pass_lenghth = int(input("Enter password length: "))

        # for handling the error eith if..else *********************
        '''if(pass_lenghth.isdigit()):
           pass_lenghth=int(pass_lenghth)
        else:
            print("ERROR: Incorrect input! -Please enter an integer value !!")
            exit()'''
        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        # print(s)
        random.shuffle(s)
        password = "".join(s[0:pass_lenghth])
        print("Your Password is: " + password)
    except Exception as e:
        print(e)
    finally:
        print("Please rerun the program with correct integer input to generate new password !!")

paas_gen()