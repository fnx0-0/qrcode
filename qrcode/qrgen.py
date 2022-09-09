import qrcode
data=input('input')
img=qrcode.make(data)
img.save("img.png")