import pyowm

print ('Hello')
apiKey='1ea01e1793668b987f4cca91e435248b'
owm = pyowm.OWM (apiKey)
observation = owm.weather_at_place ('London, UK')
w = observation.get_weather()

w.get_wind ()
w.get_humidity ()