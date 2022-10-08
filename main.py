from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- DATA ------------------------------- #

words_data = pd.read_csv('data/french_words.csv')
words_data_list = pd.DataFrame.to_dict(words_data, orient="records")


def next_card():
    word = random.choice(words_data_list)
    canvas.itemconfig(canvas_title, text='French')
    canvas.itemconfig(canvas_word, text=word['French'])
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("French Flash Cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# Images
card_back = PhotoImage(file='images/card_back.png').subsample(2, 2)
card_front = PhotoImage(file='images/card_front.png').subsample(2, 2)
right = PhotoImage(file='images/right.png').subsample(2, 2)
wrong = PhotoImage(file='images/wrong.png').subsample(2, 2)

# Canvas
canvas = Canvas(width=400, height=263)
canvas.create_image(200, 131, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_title = canvas.create_text(200, 75, text='', font=('Ariel', 20, 'italic'))
canvas_word = canvas.create_text(200, 131, text='', font=('Ariel', 30, 'bold'))

# Buttons
right_button = Button(image=right, command=next_card, highlightthickness=0, borderwidth=0)
unknown_button = Button(image=wrong, command=next_card, highlightthickness=0, borderwidth=0)

# Layout
canvas.grid(row=0, column=0, columnspan=2)
unknown_button.grid(row=1, column=0, pady=20)
right_button.grid(row=1, column=1, pady=20)

next_card()

window.mainloop()
