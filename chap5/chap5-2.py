import requests
import json

# 現在の天気を取得する
url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=ja$units=metric"
url = url.format(city="Tokyo,JP", key="c649a76bc4431b260edb4b21a56a3068")

jsondate = requests.get(url).json()
print(jsondate)

# 
