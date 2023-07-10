import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://github.com/lincolnloop/python-qrcode')
qr.make(fit=True)

img = qr.make_image(fill_color=(255, 0, 0), back_color="white")
img.save('test.png')