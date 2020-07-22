import sys
import subprocess
from win32com.client import Dispatch
import os


# from decouple import config

def speak(str):
    speak = Dispatch("SAPI.spVoice")
    speak.Speak(str)


IP_NETWORK = ['192.168.0.101', '192.168.0.102', '192.168.0.103']
# IP_DEVICE = '192.168.0.103'
for ip in IP_NETWORK:

    proc = subprocess.Popen(["ping", ip], stdout=subprocess.PIPE)
    print(proc.pid)
    line = proc.stdout.readline()
    print(line.split())
    print(proc.stdout.readline())
    #
    # print(proc.stdout.readline().split(''))
    while True:
        line = proc.stdout.readline()
        print(line)
        if not line:
            break
        # the real code does filtering here
        # print(line.decode('utf-8').lower())
        connected_ip1 = line.decode('utf-8').__contains__("Reply from 192.168.0.101")
        connected_ip2 = line.decode('utf-8').__contains__("Reply from 192.168.0.102")
        connected_ip3 = line.decode('utf-8').__contains__("Reply from 192.168.0.103")
        print("connected_ip1 :" , connected_ip1)
        print("connected_ip2 :" , connected_ip2)
        print("connected_ip3 :" , connected_ip3)
        # print(IP_DEVICE)
        if connected_ip1 is True:
            speak("you have a alert  !! Anupama mobile is connected to the network")
        if connected_ip2 is True:
            speak("you have a alert  !! pradeep Computer is connected to the network")
        if connected_ip3 is True:
            speak("you have a alert  !! pradeep mobile is connected to the network")
            # subprocess.Popen(["say", "Linnea just connected to the network"])
