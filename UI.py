import tkinter
import Main as size
from tkinter import *

mainWindow = Tk()
mainWindow.title("Sizing App")

jacketSize = ""
pantSize = ""

mb = IntVar()
mb_state = IntVar()

nb = IntVar()
nb_state = IntVar()

ltg = IntVar()
ltg_state = IntVar()

c = IntVar()
c_state = IntVar()

b = IntVar()
b_state = IntVar()

# jacket measurements
chestLabel = Label(mainWindow, text="Chest: ")
coatWaistLabel = Label(mainWindow, text="Coat Waist: ")

chestUI_Temp = tkinter.StringVar()
chestEntry = Entry(mainWindow, textvariable=chestUI_Temp)
coatWaistUI_Temp = tkinter.StringVar()
coatWaistEntry = Entry(mainWindow, textvariable=coatWaistUI_Temp)

# Pant Measurements
waistLabel = Label(mainWindow, text="Waist: ")
seatLabel = Label(mainWindow, text="Seat: ")

waistUI_Temp = tkinter.StringVar()
waistEntry = Entry(mainWindow, textvariable=waistUI_Temp)
seatUI_Temp = tkinter.StringVar()
seatEntry = Entry(mainWindow, textvariable=seatUI_Temp)

# Shirt Measurements
neckLabel = Label(mainWindow, text="Neck: ")
sleeveLabel = Label(mainWindow, text="Sleeve: ")

neckUI_Temp = tkinter.StringVar()
neckEntry = Entry(mainWindow, textvariable=neckUI_Temp)
sleeveUI_Temp = tkinter.StringVar()
sleeveEntry = Entry(mainWindow, textvariable=sleeveUI_Temp)

# Height (Feet/Inches)
feetLabel = Label(mainWindow, text="Feet: ")
inchesLabel = Label(mainWindow, text="Inches: ")

feetUI_temp = tkinter.StringVar()
feetEntry = Entry(mainWindow, textvariable=feetUI_temp)
inchesUI_Temp = tkinter.StringVar()
inchesEntry = Entry(mainWindow, textvariable=inchesUI_Temp)

# Weight
weightLabel = Label(mainWindow, text="Weight: ")

weightUI_Temp = tkinter.StringVar()
weightEntry = Entry(mainWindow, textvariable=weightUI_Temp)

chestLabel.grid(row=0, sticky=E)
coatWaistLabel.grid(row=1, sticky=E)
waistLabel.grid(row=2, sticky=E)
seatLabel.grid(row=3, sticky=E)
neckLabel.grid(row=4, sticky=E)
sleeveLabel.grid(row=5, sticky=E)
feetLabel.grid(row=6, sticky=E)
inchesLabel.grid(row=6, column=3, sticky=E)
weightLabel.grid(row=8, sticky=E)

chestEntry.grid(row=0, column=1)
coatWaistEntry.grid(row=1, column=1)
waistEntry.grid(row=2, column=1)
seatEntry.grid(row=3, column=1)
neckEntry.grid(row=4, column=1)
sleeveEntry.grid(row=5, column=1)
feetEntry.grid(row=6, column=1)
inchesEntry.grid(row=6, column=4)
weightEntry.grid(row=8, column=1)


def set_mb_box():
    mb_state.set(mb.get())


def set_nb_box():
    nb_state.set(nb.get())


def set_ltg_box():
    ltg_state.set(ltg.get())


def set_c_box():
    c_state.set(c.get())


def set_b_box():
    b_state.set(b.get())


# Suit Color
mb_box = Checkbutton(mainWindow, text="Midnight Blue", variable=mb, offvalue=0, onvalue=1, command=set_mb_box)
mb_box.grid(row=9)

nb_box = Checkbutton(mainWindow, text="Nicks Blue", variable=nb, offvalue=0, onvalue=1, command=set_nb_box)
nb_box.grid(row=9, column=1)

ltg_box = Checkbutton(mainWindow, text="Light Grey", variable=ltg, offvalue=0, onvalue=1, command=set_ltg_box)
ltg_box.grid(row=9, column=2)

c_box = Checkbutton(mainWindow, text="Charcoal", variable=c,  offvalue=0, onvalue=1, command=set_c_box)
c_box.grid(row=9, column=3)

b_box = Checkbutton(mainWindow, text="Black", variable=b, offvalue=0, onvalue=1, command=set_b_box)
b_box.grid(row=9, column=4)


# Set Suit Color
def set_suit_color(suit_color):
    if ltg_state.get() == 1:
        suit_color = "Light Grey"
        return suit_color
    if mb_state.get() == 1:
        suit_color = "Midnight Blue"
        return suit_color
    if nb_state.get() == 1:
        suit_color = "Nicks Blue"
        return suit_color
    if c_state.get() == 1:
        suit_color = "Charcoal"
        return suit_color
    if b_state.get() == 1:
        suit_color = "Black"
        return suit_color
    return suit_color


def run():
    jacketSize = ""
    pantSize = ""
    jacketLength = ""
    shirt_size = ""
    sleeve_length = ""
    suit_color = ""
    jacketFit = ""

    feet = float(str(feetUI_temp.get()))
    inches = round(float(str(inchesUI_Temp.get())))
    weight = float(str(weightUI_Temp.get()))
    chest_input = float(chestUI_Temp.get())
    chest = round(float(str(chestUI_Temp.get())))
    coat_waist = float(str(coatWaistUI_Temp.get()))
    waist_input = float(str(waistUI_Temp.get()))
    waist = round(float(str(waistUI_Temp.get())))
    seat = float(str(seatUI_Temp.get()))
    neck = round(float(str(neckUI_Temp.get())), 1)
    sleeve = round(float(str(sleeveUI_Temp.get())))

    if (chest % 2) == 0:
        chest = chest
    else:
        chest = chest + 1
    if (waist % 2) == 0:
        waist = waist
    else:
        waist = waist + 1

    suit_color = set_suit_color(suit_color)
    jacketSize = size.find_jacket_size_and_fit(chest, coat_waist, chest_input, suit_color)
    jacketLabel = Label(mainWindow, text="Jacket Size: " + str(jacketSize))

    jacketLength = str(size.find_jacket_length(feet, inches))
    jacketLengthLabel = Label(mainWindow, text=jacketLength)

    jacketFit = jacketSize[1]
    jacketSize2 = jacketSize[0]
    firstPantSize = size.find_pant_size_and_fit(jacketSize2, jacketFit, waist, seat)
    finalPantSize = size.is_it_ok_to_split(firstPantSize, jacketSize2, seat, jacketFit)
    pantLabel = Label(mainWindow, text="Pant Size: " + str(finalPantSize))

    shirt_size = size.find_shirt_size(neck, chest, coat_waist)
    shirt_size_and_sleeve = size.find_shirt_sleeve_Length(shirt_size, sleeve)
    shirt_label = Label(mainWindow, text="Shirt Size: " + str(shirt_size_and_sleeve))

    size.red_flags(feet, inches, weight, chest_input, chest, coat_waist, waist, seat, shirt_size, sleeve, finalPantSize, jacketSize2, waist_input)

    jacketLabel.grid(row=0, column=3)
    jacketLengthLabel.grid(row=0, column=4)
    pantLabel.grid(row=2, column=3)
    shirt_label.grid(row=4, column=3)


test = Button(mainWindow, text="Try Me", command=run)
test.grid(row=10, column=2)

mainWindow.mainloop()
