"""A simple QR code generator that takes a URL as input and saves the generated QR code as an image file.
1. pip install qrcode[pil]
2. change the file_path variable to your desired location"""

import qrcode

def qrcode_generator(url):
    file_path = "C:\\Users\\DELL\\Desktop\\Python-Mini-Project\\MyProject\\qrcode.png"
    qr = qrcode.QRCode()
    qr.add_data(url)
    img = qr.make_image()
    img.save(file_path)
    return f"QR code saved to {file_path}"
    


url = input("Enter the URL to generate QR code: ")
qrcode_generator(url)


