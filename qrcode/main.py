#  TODO:

import qrcode

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
name = input("Please name your qr code: ")
print("Thank you!")
print("Do you want to change qrcode color? (by default it is white and black)")
colorchange = input("Y/n: ")
colorchange = colorchange.upper()

color = None


if colorchange == "Y":
    while color not in colors:  # ta pentla każe wybrać kolor, jak ktoś nie wybierze to zapentla
        print("Available colors: red, orange, yellow, green, light-blue,\nblue, purple, pink, magenta")
        color = input("Pick a color: ").lower()
        rgb_value = None

    if color == "red":
        rgb_value == 255, 255, 255

    # match color:
    #     case "red":
    #         rgb_value = 255, 255, 255
    #     case "orange":
    #         rgb_value = 255, 128, 0
    #     case "yellow":
    #         rgb_value = 255, 255, 0
    #     case "green":
    #         rgb_value = 0, 255, 0
    #     case "light-blue":
    #         rgb_value = 0, 255, 255
    #     case "blue":
    #         rgb_value = 0, 0, 255
    #     case "purple":
    #         rgb_value = 128, 0, 255
    #     case "pink":
    #         rgb_value = 255, 0, 255
    #     case "magenta":
    #         rgb_value = 255, 0, 191
    #

    qrcode = qr.make_image(back_color=(rgb_value), fill_color=(rgb_value))
    qrcode.save(name + '.png')
else:
    qrcode = qr.make(link)
    qrcode.save(name + '.png')