import qrcode
from datetime import datetime 

now = datetime.now()
current_time = now.strftime("%m-%d-%Y-%H.%M.%S")

img = qrcode.make('Some data here')
type(img)  # qrcode.image.pil.PilImage
img.save("./qr-code/"+current_time+".png")