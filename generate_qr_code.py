import qrcode
from datetime import datetime 

now = datetime.now()
current_time = now.strftime("%d-%m-%Y-%H.%M.%S")  ##Ext 20-05-2025-15.38.50

img = qrcode.make('Some data here')  #input data here
type(img)  
img.save("./qr-code/"+current_time+".png")