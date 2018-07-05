#! python3
# quickWeather.py - Print weather for a location from the command line

import json, requests, sys, os

def degreeKtoC(kelvin):
    return round(9*(int(kelvin) - 273)/5 + 32,2)

if len(sys.argv) < 2:
    print('Usage: python {} [location]'.format(os.path.basename(sys.argv[0])))
    sys.exit()

location = ' '.join(sys.argv[1:])

# Download Json weather data 
url = 'https://api.openweathermap.org/data/2.5/forecast?q={}&appid=8acb53156b86932a2bd42a6688aaae94'.format(location)
response = requests.get(url)
response.raise_for_status()

# Load Json in to python variable
weatherData = json.loads(response.text)

w = weatherData['list']
city = weatherData['city']
print('Current weather for: {}, {}'.format(city['name'], city['country']))
for weatherUnit in w:
    print('{}: {:>6} {:>6} {:>6}  {:<6} ({})'.format(weatherUnit['dt_txt'], degreeKtoC(weatherUnit['main']['temp']), 
            degreeKtoC(weatherUnit['main']['temp_min']), degreeKtoC(weatherUnit['main']['temp_max']), 
            weatherUnit['weather'][0]['main'], weatherUnit['weather'][0]['description']))