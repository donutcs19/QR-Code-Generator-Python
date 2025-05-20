import qrcode

from datetime import datetime 

now = datetime.now()
current_time = now.strftime("%d-%m-%Y-%H.%M.%S")  ##Ext 20-05-2025-15.38.50
filename = current_time

data = input("Input your data : ")
name = input("Input your filename :")

if name != '':
    filename = name


qr = qrcode.QRCode(
    version=6,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=2,
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="white")
# img = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))

type(img)  
img.save("./qr-code/"+filename+".png")