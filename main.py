import pandas
import random
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

#Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#Get images
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")

#------------------CSV Read and Word change-------------------------#

#------------------UI configuration-------------------------#
#Canvas for the images
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400,263, image=card_front)
language = canvas.create_text(400,150, text="title", fill="black" ,font=("arial", 40, "italic"))
word = canvas.create_text(400,263, text="word",fill="black" , font=("arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_button = Button(image=wrong, highlightthickness=0, bg=BACKGROUND_COLOR)
wrong_button.grid(column=0,row=1)

right_button = Button(image=right, highlightthickness=0, bg=BACKGROUND_COLOR)
right_button.grid(column=1,row=1)

window.mainloop()
