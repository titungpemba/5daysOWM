import requests

app_id = "d1f7f1d42ce9fe62fafc2798e6747635"
name_of_the_place = input('Name of the place: ')
base_url = "http://api.openweathermap.org/data/2.5/forecast"
complete_url = base_url + "?q=" + name_of_the_place + "&appid=" + app_id 
#print(complete_url)
json_data = requests.get(complete_url).json()
print(json_data)