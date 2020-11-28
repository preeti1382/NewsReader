import pywin32_system32
import json
import requests

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == "__main__":
    url = ('http://newsapi.org/v2/top-headlines?'
       'sources=BBC-news&'
       'apiKey=41fbd983ba9e49c69af0da54d52801e8')
    response = requests.get(url)
    content = response.text
    speak_content = json.loads(content)
    speak("Good Morning!!")
    for i in range(1,11):
        speak(speak_content['articles'][i]['title'])
    speak('Thats it for today!Have a nice day!')
    


    