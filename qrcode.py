'''
Create your own QR Code with Python
Author: Niharika
'''
#import the module
import pyqrcode

#define the data
data = "https://github.com/niharika142308-ops"
#create qrcode
img = pyqrcode.create(data)
#save the qrcode in png format with proper scaling
img.png('githubwebsite.png',scale=10)