import pyqrcode 
from pyqrcode import QRCode 

link=input("Enter The Link: ")

name=input("Name of the wepsite: ")

Qr = pyqrcode.create(link)

Qr.svg(f"{name}.svg", scale = 12)

