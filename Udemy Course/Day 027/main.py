from tkinter import *

MILE_KM = 1.60934

def miles_to_km():
        miles = int(input_miles.get())
        km = round(miles * MILE_KM, 2)
        output_km.config(text = f"{km}")

#Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.minsize()
window.config(padx = 25, pady = 25)

label_miles = Label(text="Miles")
label_miles.grid(row = 0, column = 2)

label_km = Label(text="km")
label_km.grid(row = 1, column = 2)

label_is_equal_to = Label(text="is equal to")
label_is_equal_to.grid(row = 1, column = 0)

button = Button(text="Calcutale", command=miles_to_km)
button.grid(row = 2, column = 1)

input_miles = Entry(width=10)
input_miles.grid(row =0, column = 1)

output_km = Label(text="0")
output_km.grid(row =1, column = 1)

window.mainloop()