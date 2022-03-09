#import decode library from pyzbar
from pyzbar.pyzbar import decode
from PIL import Image

#store location of qrcode file to decode in a variable 
img = Image.open('C:/Users/C842233/OneDrive - Standard Bank/Desktop/files/myqrcode1.png')

#use decode method to get data from the qrcode and store it in a variable
result = decode(img)

#output the decoded data
print (result)