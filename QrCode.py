import qrcode
url ="https://github.com/sanjayswaminathan666"
qr=qrcode.QRCode(version=1,box_size=10,border=5)
qr.add_data(url)
qr.make(fit=True)
img=qr.make_image(fill='black',black_colour='white')
img.save("portfolio_qr.png")
img.show()