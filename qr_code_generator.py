import qrcode

data = input("Enter the text or URL: ").strip()
filename = input("Enter your Filename").strip()
qr = qrcode.qrcode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_colour="black", back_colour="white")
image.save(filename)
print(f'QR SAVED AS {filename}')