import requests
import json
from win32com.client import Dispatch


def speak(str):
    speak = Dispatch("SAPI.spVoice")
    speak.Speak(str)


r = requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=85944fc974d54ac5987ddd364c784dff")
print(r.text)
text = r.text
print(type(text))
text_json = json.loads(text)
print((text_json))
article_list = text_json["articles"]

print("***  Here is top " + str(len(article_list)) + " news of the hour: ****")
speak("***  Here is top " + str(len(article_list)) + " news of the hour: ****")
# for i in range(1,len(article_list)+1):
i = 1
for l in article_list:
    print("Headline:" + str(i) + ". " + l['title'])
    speak("Headline:" + str(i) + ". " + l['title'])
    i += 1
