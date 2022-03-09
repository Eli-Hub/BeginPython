#import qrcode library from python 
import qrcode

#store data to encode in a variable
data = "Buadu Rita Gifty"

#customize the qrcode
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.make(fit=True)

#assign data to customized qrcode
qr.add_data(data)

#convert to image
img = qr.make_image(fill_color = 'red', back_color = 'white')

#save image to a specific location
img.save("Address of Folder")