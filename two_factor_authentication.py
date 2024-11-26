#DONT NEED THIS FILE ANYMORE

import pyotp
import time
import pyqrcode

#secret key for generating otp
secret_key = "OILKYMRCXNK7NHD32TXMDIH6CCWGDMNS"

#url_qr = pyotp.totp.TOTP(secret_key).provisioning_uri("andrew.swartz.cs@gmail.com", issuer_name="Facial Recognition")

#saves .svg image to working directory
#dont uncomment, just use screenshot in the directory
#url = pyqrcode.create(url_qr)
#url.svg('C:/Users/yourb/PycharmProjects/Facial-Recognition/Face Recognition/uca-url.svg', scale=8)

#install authy or some other 2fa hosting site. add with the screenshot of the url in uca-url.svg. you can run this code with everything commented out
#and the code generated should be the same one on your 2FA app. The secret key was generated using some random 32-bit thing i generated using pyotp
#if you change the secret key, things go to shit. dont do that

totp = pyotp.TOTP(secret_key)
print(totp.now())

#otp = totp.now()

#print(totp.verify(otp))
#time.sleep(30)
#print(totp.verify(otp))
