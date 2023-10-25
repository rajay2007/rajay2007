from customtkinter import *
from tkinter import colorchooser
from PIL import Image

set_appearance_mode('system')
set_default_color_theme('blue')

win = CTk()
win.title("Color Picker")
win.iconbitmap("res\\icon.ico")
win.geometry("300x325")
win.resizable(False, False)

def ColorPick():
    color = colorchooser.askcolor()
    color_frame.configure(fg_color=color[1])
    hex_entry.configure(state=NORMAL)
    rgb_entry.configure(state=NORMAL)
    hex_entry.delete(0, END)
    rgb_entry.delete(0, END)
    hex_entry.insert(0, color[1])
    rgb_entry.insert(0, color[0])

color_frame = CTkFrame(win, width=150, height=150)
color_frame.pack(pady=15)

CTkButton(win, text="Select Color", cursor='hand2', corner_radius=50, command=ColorPick).pack(pady=15)

CTkLabel(win, text="HEX : ", font=('calibri', 16, 'bold')).place(x=25, y=255)
CTkLabel(win, text="RGB : ", font=('calibri', 16, 'bold')).place(x=25, y=290)

hex_entry = CTkEntry(win, width=100, height=5, state=DISABLED)
rgb_entry = CTkEntry(win, width=100, height=5, state=DISABLED)
hex_entry.place(x=70, y=257)
rgb_entry.place(x=70, y=293)

win.mainloop()
