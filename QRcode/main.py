import qrcode

qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)


colors = ['red', 'orange', 'yellow', 'green', 'light-blue', 'blue', 'purple', 'pink', 'magenta']


print("Hello! Welcome to qrcode generator!!!")

link = ""

while len(link) == 0:
    link = input("Please insert a link: ")

name = ""

while len(name) == 0:
    name = input("Please name your qr code: ")

print("Do you want to change qrcode color? (by default it is white and black)")

color_change = input("Y/n: ")
color_change = color_change.upper()

color = None


if color_change == "Y":
    while color not in colors:  # ta pentla każe wybrać kolor, jak ktoś nie wybierze to zapentla
        print("Available colors: red, orange, yellow, green, light-blue,\nblue, purple, pink, magenta")
        color = input("Pick a color: ").lower()

    if color == "red":  # red
        qrcode = qr.make_image(back_color=(255, 255, 255), fill_color=(255, 0, 0))
        qr.add_data(link)
        qrcode.save(name + '.png')

    elif color == "orange":  # orange
        qr.add_data(link)
        qr.make(fit=True)
        qrcode = qr.make_image(back_color=(255, 255, 255), fill_color=(255, 128, 0))
        qrcode.save(name + '.png')

    elif color == "yellow":  # yellow
        qr.add_data(link)
        qr.make(fit=True)
        qrcode = qr.make_image(back_color=(255, 255, 255), fill_color=(255, 255, 0))
        qrcode.save(name + '.png')

    elif color == "green":  # green
        qr.add_data(link)
        qr.make(fit=True)
        qrcode = qr.make_image(back_color=(255, 255, 255), fill_color=(0, 255, 0))
        qrcode.save(name + '.png')

    elif color == "light-blue":  # light-blue
        qr.add_data(link)
        qr.make(fit=True)
        qrcode = qr.make_image(back_color=(255, 255, 255), fill_color=(0, 255, 255))
        qrcode.save(name + '.png')

    elif color == "blue":  # blue
        qr.add_data(link)
        qr.make(fit=True)
        qrcode = qr.make_image(back_color=(255, 255, 255), fill_color=(0, 0, 255))
        qrcode.save(name + '.png')

    elif color == "purple":  # purple
        qr.add_data(link)
        qr.make(fit=True)
        qrcode = qr.make_image(back_color=(255, 255, 255), fill_color=(128, 0, 255))
        qrcode.save(name + '.png')

    elif color == "pink":  # pink
        qr.add_data(link)
        qr.make(fit=True)
        qrcode = qr.make_image(back_color=(255, 255, 255), fill_color=(255, 0, 255))
        qrcode.save(name + '.png')

    elif color == "magenta":  # magenta
        qr.add_data(link)
        qr.make(fit=True)
        qrcode = qr.make_image(back_color=(255, 255, 255), fill_color=(255, 0, 191))
        qrcode.save(name + '.png')

else:  # basic
    qr.add_data(link)
    qr.make(fit=True)
    qrcode = qr.make_image(back_color=(255, 255, 255), fill_color=(0, 0, 0))
    qrcode.save(name + '.png')

print("Thank you for using our qrcode generator!")
