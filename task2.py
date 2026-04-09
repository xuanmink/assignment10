import requests
city = input("Enter a municipality: ")
api_key = "f8166921bd5b2ea21a06c4836b1f5782"
url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key
res = requests.get(url).json()
kelvin = res["main"]["temp"]
celsius = kelvin - 273.15
desc = res["weather"][0]["description"]
print("Condition:", desc)
print("Temperature in Celsius:", celsius)