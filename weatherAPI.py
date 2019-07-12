import pyowm

city1 = input("Enter the First City in " " with a comma: ")
country1=input ("Enter the First Country in " ": ")
name1=city1+country1


city2 = input("Enter the Second City in " " with a comma: ")
country2=input ("Enter the Second Country in " ": ")
name2=city2+country2


apiKey='3c9eaf32882bfec545d09bbaaf1e59e8'
owm = pyowm.OWM(apiKey) 

observation = owm.weather_at_place (name1)
w = observation.get_weather()

a=w.get_wind ()
b=w.get_humidity ()
c=w.get_pressure ()
d=w.get_temperature()
print ('Data for', name1)
print ('The Wind: ', a)
print ('The Humidity: ', b)
print ('The Pressure: ' , c)
print ('The Temperature: ', d)


observation = owm.weather_at_place (name2)
w = observation.get_weather()

e=w.get_wind ()
f=w.get_humidity ()
g=w.get_pressure ()
h=w.get_temperature()

print ('Data for', name2)
print ('The Wind: ', e)
print ('The Humidity: ', f)
print ('The Pressure: ' , g)
print ('The Temperature: ', h)


