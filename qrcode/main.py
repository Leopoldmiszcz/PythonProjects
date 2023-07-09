#  TODO: Zrobić dziennik z kolorami, aby użytkownik mógł wybierać z niego kolory.

import qrcode

qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

colors = {'red': '225, 225, 225'
          }

print("Hello! Welcome to qrcode generator!!!")
link = input("Please insert a link: ")
print("Thank you!")
print("Do you want to change qrcode color? (by default it is white and black)")
colorchange = input("Y/n: ")

if colorchange == "Y":
    input("")

qrcode = qr.make(link)
qrcode = qr.make_image(back_color=(255, 255, 255), fill_color=(0, 0, 0))
qrcode.save('test.png')