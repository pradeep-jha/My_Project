# print("hello")
# import pandas as pd
#
# list=[1,'pradeep',2344,'Bangalore']
# df=pd.DataFrame(list)
#
# print(df)
# df.to_csv("C:\\Users\\PRADEEP\\PycharmProjects\\pySparkProject\\outputs\\out.csv")


import requests
import dotenv
import sys
import os

from pprint import pprint
#city_name=input("Enter city name:")
def get_weather(city):
    dotenv.load_dotenv()
    api_key=os.getenv("8b683c130179b9ccf36437390ed5fd1b") # taking apikey from .env file
    api_key="8b683c130179b9ccf36437390ed5fd1b"
    url=f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    #  "&units=metric" --for geting the tem in degree celcious
    print(url)
    res=requests.get(url)
    print(res)

    #print(res.text)

get_weather("bangalore")