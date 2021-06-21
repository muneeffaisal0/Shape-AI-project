import requests
from datetime import datetime

get_city=input("Enter the city name: ")
api_link="http://api.openweathermap.org/data/2.5/weather?q="+get_city+"&appid=8f5ac8450ca64db5a3672209aafdbbed"
req=requests.get(api_link)
data=req.json()


weather="Present weather     = "+data['weather'][0]['description']+"\n"
temp="Present Temperature = "+str("{:.2f} C".format(data['main']['temp']-273.15))+"\n"
humidity="Present Humidity    = "+str(data['main']['humidity'])+"%\n"
speed="Present Wind Speed  = "+str(data['wind']['speed'])+"kmph\n"
date_city="Weather condition in {} -- {} \n".format(get_city.upper(),datetime.now())

print(date_city+"\n\n"+weather+temp+speed+humidity)


file1=open("weather.txt","w")
file1.write(date_city)
file1.write("\n \n")
file1.write(weather)
file1.write(temp)
file1.write(speed)
file1.write(humidity)

file1.close()