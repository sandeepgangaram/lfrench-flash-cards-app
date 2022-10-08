BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *

window = Tk()
window.title("French Flash Cards")
window.config(width=800, height=526, background=BACKGROUND_COLOR, pady=50, padx=50)

card_back = PhotoImage(file='images/card_back.png')
card_front = PhotoImage(file='images/card_front.png')
right = PhotoImage(file='images/right.png')
wrong = PhotoImage(file='images/wrong.png')

canvas = Canvas()
canvas.insert()







window.mainloop()