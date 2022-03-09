#import requests library to make request to openweather
import requests
#import prettyprint to restyle the data requested
from pprint import pprint

#pass the api key copied from open weather to a variable
API_KEY ='1ea01e1793668b987f4cca91e435248b'

#prompt user to enter city
city = input("Enter a city: ")

#pass user input to the url of open weather api
base_url = "http://api.openweathermap.org/data/2.5/weather?q="+ city + "&appid=" + API_KEY

#pass data retrieved in json form to a variable
weather_data = requests.get(base_url).json()

#use prettyprint to format the output
pprint(weather_data)