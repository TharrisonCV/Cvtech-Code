import qrcode
from pyexpat import features

features = qrcode.QRCode(version=1, box_size=40, border=3)

features.add_data('https://cvtech.instructure.com/login/canvas')
features.make(fit=True)
image = features.make_image(fill_color="black", back_color="white")
image.save('image.png')