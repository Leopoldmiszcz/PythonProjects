#  TODO: Zrobić dziennik z kolorami, aby użytkownik mógł wybierać z niego kolory.

import qrcode
print("Available colors: red, orange, yellow, green,\n light-blue, blue, purple, pink, magenta")
qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

colors = {'red': '225, 225, 225',
          'orange': '255, 128, 0',
          'yellow': '255, 255, 0',
          'green': '0, 255, 0',
          'light-blue': '0, 255, 255',
          'blue': '0, 0, 255',
          'purple': '128, 0, 255',
          'pink': '255, 0, 255',
          'magenta': '255, 0, 191'}

print(colors['red'])

print("Hello! Welcome to qrcode generator!!!")
link = input("Please insert a link: ")
print("Thank you!")
print("Do you want to change qrcode color? (by default it is white and black)")
colorchange = input("Y/n: ")


if colorchange == "Y":
    print("Available colors: red, orange, yellow, green, light-blue,\nblue, purple, pink, magenta")
    color = input("Pick a color: ")
    qrcode = qr.make_image(back_color=(255, 255, 255), fill_color=(0, 0, 0))

qrcode = qr.make(link)
qrcode.save('test.png')