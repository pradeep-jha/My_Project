import sys
import subprocess
from win32com.client import Dispatch
import os
#from decouple import config

def speak(str):
    speak = Dispatch("SAPI.spVoice")
    speak.Speak(str)

IP_NETWORK = '192.168.0.103'
IP_DEVICE = '192.168.0.103'
proc = subprocess.Popen(["ping", IP_NETWORK],stdout=subprocess.PIPE)
print(proc.pid)
line = proc.stdout.readline()
print(line.split())
print(proc.stdout.readline())
#
#print(proc.stdout.readline().split(''))
while True:
  line = proc.stdout.readline()
  print(line)
  if not line:
    break
  #the real code does filtering here
  #print(line.decode('utf-8').lower())
  connected_ip = line.decode('utf-8').__contains__("Reply")
  #print(connected_ip)
  #print(IP_DEVICE)
  if connected_ip :
	  speak("you have a alert  !! pradeep mobile just connected to the network")
	  #subprocess.Popen(["say", "Linnea just connected to the network"])