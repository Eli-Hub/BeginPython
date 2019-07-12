
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Group4_APP")
LocName=input ("Name the City of Town you want to Locate: ")
location = geolocator.geocode(LocName)



print ('\n ADDRESS OF', LocName, '\n')
print(location.address)
print ('\n GEOGRAPHICAL LOCATION \n')
print((location.latitude, location.longitude))
print ('\n DETAILED INFORMATION ABOUT THE LOCATION \n')
print(location.raw)