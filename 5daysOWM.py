import requests

app_id = "d1f7f1d42ce9fe62fafc2798e6747635"
name_of_the_place = input('Name of the place: ')

base_url = "http://api.openweathermap.org/data/2.5/forecast"
complete_url = base_url + "?q=" + name_of_the_place + "&appid=" + app_id 
#print(complete_url)
json_data = requests.get(complete_url).json()
#print(json_data)
name_of_the_city = json_data['city']['name']
print(name_of_the_city)
city_lat = json_data['city']['coord']['lat']
city_lon = json_data['city']['coord']['lon']
print("latitude : " + str(city_lat) + ", Longitude : " + str(city_lon))
for item in json_data['list']:
    time_forecasted = item['dt_txt']
    print("\n" + time_forecasted)
    temp = str(int(item['main']['temp']-273.15))
    print("temp: " + temp)
    feels_like = str(item['main']['feels_like'])
    print("feels_like: " + feels_like)
    temp_min = str(int(item['main']['temp_min']-273.15))
    print("min: " + temp_min)
    temp_max = str(int(item['main']['temp_max']-273.15))
    print("max: " + temp_max)
    pressure = str(item['main']['pressure'])
    print("pressure: " + pressure)
    sea_level = str(item['main']['sea_level'])
    print("sea lvl: " + sea_level)
    grnd_level = str(item['main']['grnd_level'])
    print("grnd lvl: "+grnd_level)
    humidity = str(item['main']['humidity'])
    print("humidity: "+ humidity)
    weather_shrtDes = item['weather'][0]['main']
    print("Weather: "+ weather_shrtDes)
    weather_des = item['weather'][0]['description']
    print("Weather description: "+ weather_des)
    cloudiness = str(item['clouds']['all'])
    print("Cloudiness: " + cloudiness + "%")
    windSpd = str(item['wind']['speed'])
    print("Wind speed: \n\t in meter per second is " + windSpd)
    windSpd = str(float(item['wind']['speed']*3600/1000))
    print("\t in kilometer per second is " + windSpd)
    wind_degree = str(item['wind']['deg'])
    print("Wind degree: " + wind_degree + "°") 

