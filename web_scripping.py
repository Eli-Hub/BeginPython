#import requests library from python
import requests
#import BeautifulSoup library and rename it as bs to use in code
from bs4 import BeautifulSoup as bs

#prompt user for username used on GitHub
github_user= input("Input Github User: ")

#concartinate username with url of github
url = 'https://github.com/'+ github_user

#get the url of the account profile image into a variable
r = requests.get(url)

#pass the content of the url to a variable
soup = bs(r.content, 'html.parser')

#from the data retrieved, select specific parameters
profile_img = soup.find('img',{'alt': 'Avatar'})['src']

#output the profile image
print(profile_img)