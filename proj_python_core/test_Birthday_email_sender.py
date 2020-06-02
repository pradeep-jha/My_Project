import pytest
from proj_python_core import Birthday_email_sender as b
def test_send_email():
     str=b.sendEmail('a','b','c')
     print("111xxxxxxxxxxxxxxxxxxxxxxxxxxxxx123 \n")
     print(str)
     assert str ==f"*********\nTo: a\nSubject: b\nMessage: c \n--------"
