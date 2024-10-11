from anemos.weather import AnemosObjectTypes, v2get

weather_informations = v2get("5320011", AnemosObjectTypes.WeatherForecast)
print(weather_informations)