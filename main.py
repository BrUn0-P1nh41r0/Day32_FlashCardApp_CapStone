import pandas
import random
import time
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
current_card= {}
data_dict={}

try:
    data = pandas.read_csv("./data/Words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    data_dict = original_data.to_dict(orient = "records")
else:
    data_dict = data.to_dict(orient="records")

#------------------CSV Read and Word change-------------------------#
def update_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(back_image, image=card_front)
    canvas.itemconfig(language, text="French", fill= "black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=show_english)

def show_english():
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(back_image, image=card_back)

#------------------Right and Wrong scenarios-------------------------#
def is_known():
    data_dict.remove(current_card)
    to_learn = pandas.DataFrame(data_dict)
    to_learn.to_csv("./data/Words_to_learn.csv", index=False)
    update_card()
#------------------UI configuration-------------------------#

#Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=show_english)

#Get images
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")

#Canvas for the images
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
back_image =canvas.create_image(400,263, image=card_front)
language = canvas.create_text(400,150, text="title", fill="black" ,font=("arial", 40, "italic"))
word = canvas.create_text(400,263, text="word",fill="black" , font=("arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_button = Button(image=wrong, highlightthickness=0, bg=BACKGROUND_COLOR, command=update_card)
wrong_button.grid(column=0,row=1)

right_button = Button(image=right, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(column=1,row=1)

update_card()

window.mainloop()
