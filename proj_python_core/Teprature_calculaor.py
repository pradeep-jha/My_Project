import requests
from pprint import pprint
#city_name=input("Enter city name:")
def get_weather(city):

    api_key="8b683c130179b9ccf36437390ed5fd1b"
    url=f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    #  "&units=metric" --for geting the tem in degree celcious
    #print(url)
    res=requests.get(url)

    #print(res.text)
    json_data=res.json()
    #pprint(json_data) # pprint for more readable json"
    city=json_data['name']
    temp=json_data['main']['temp']
    weather=json_data['weather'][0]['description']
    wind_speed=json_data['wind']['speed']
    latitude=json_data['coord']['lat']
    longitude=json_data['coord']['lon']

    print("temp= ",temp)
    print("weather= ",weather)
    print("wind_speed= ",wind_speed)
    print("latitude= ",latitude)
    print("longitude= ",longitude)
    weather_details=f" The temprature of {city} is {temp} degree celsius and the weather is {weather}"
    return weather_details

#weather=get_weather(city_name)
#print(weather)