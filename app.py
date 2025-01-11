import random
from tkinter import *
from tkinter import messagebox
import pandas
from functions import *
import os

"""
21
01 Jan 2025
"""

BACKGROUND_COLOR = "#B1DDC6"
timer = None
ENGLISH_RAN_CARD = ""
FRENCH_RAN_CARD = ""
timer = None
RAN_CARD = {}
DATA_LIST = []
count_down = 4


# -------------------------------------------- READ DATA --------------------------------------------

def right_button_func():
    global ENGLISH_RAN_CARD, RAN_CARD, DATA_LIST
    global SIDE_FLAG
    global timer

    # canvas.itemconfig(canvas_image, image=card_front_image)
    # data = pandas.read_csv("./data/french_words.csv")
    # DATA_LIST = data.to_dict(orient="records")
    # print(type(DATA_LIST))
    # RAN_CARD = random.choice(DATA_LIST)
    # FRENCH_RAN_CARD = RAN_CARD["French"]
    # ENGLISH_RAN_CARD = RAN_CARD["English"]
    # canvas.itemconfig(language_t, text="French")
    # canvas.itemconfig(word_t, text=FRENCH_RAN_CARD)

    print(RAN_CARD)
    print(type(RAN_CARD))
    DATA_LIST.remove(RAN_CARD)
    want_to_learn_data = pandas.DataFrame.from_records(DATA_LIST)
    want_to_learn_data.to_csv("./data/wants_to_learn.csv", index=False)
    print(len(want_to_learn_data))

    window.after_cancel(timer)
    SIDE_FLAG = "front"
    # timer = window.after(3000, flip_card)
    flip_card()


def change_card():
    global ENGLISH_RAN_CARD, RAN_CARD, DATA_LIST, FRENCH_RAN_CARD, count_down, timer

    try:
        data = pandas.read_csv("./data/wants_to_learn.csv")
        DATA_LIST = data.to_dict(orient="records")

    except FileNotFoundError:
        data = pandas.read_csv("./data/french_words.csv")
        DATA_LIST = data.to_dict(orient="records")

    except pandas.errors.EmptyDataError:
        window.after_cancel(timer)
        want_to_play = messagebox.askokcancel(title="Game Completed", message="Do you want to play again ?")
        if want_to_play:
            os.remove("./data/wants_to_learn.csv")
            flip_card()
        else:
            exit()

    except IndexError:
        window.after_cancel(timer)
        want_to_play = messagebox.askokcancel(title="Game Completed", message="Do you want to play again ?")
        if want_to_play:
            os.remove("./data/wants_to_learn.csv")
            flip_card()
        else:
            exit()

    # print(DATA_LIST)
    RAN_CARD = random.choice(DATA_LIST)
    FRENCH_RAN_CARD = RAN_CARD["French"]
    ENGLISH_RAN_CARD = RAN_CARD["English"]
    if SIDE_FLAG == "front":
        canvas.itemconfig(language_t, fill="black", text="French")
        canvas.itemconfig(word_t, fill="black", text=FRENCH_RAN_CARD)
        canvas.itemconfig(author_name_t, fill="black")


def wrong_button_func():
    global SIDE_FLAG

    window.after_cancel(timer)
    SIDE_FLAG = "front"
    flip_card()


def flip_card():
    global timer, count_down
    timer = window.after(3000, flip_card)
    count_down -= 1

    # front is French
    # back is English
    global SIDE_FLAG
    if SIDE_FLAG == "back":
        canvas.itemconfig(canvas_image, image=card_back_image)
        canvas.itemconfig(language_t, fill="white", text="English")
        canvas.itemconfig(word_t, fill="white", text=ENGLISH_RAN_CARD)
        canvas.itemconfig(author_name_t, fill="white")

        SIDE_FLAG = "front"
    elif SIDE_FLAG == "front":
        canvas.itemconfig(canvas_image, image=card_front_image)
        change_card()
        SIDE_FLAG = "back"


# -------------------------------------------- UI --------------------------------------------

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# If PhotoImage objects created inside a function, it will not work.
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR)

language_t = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word_t = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
author_name_t = canvas.create_text(400, 450, text=an, font=("Arial", 16, "bold"))
# time_text = canvas.create_text(400, 380, text="3", font=("Arial", 60, "bold"))
# Her column span represents the number of columns to which we want to place our canvas
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=right_button_func)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=wrong_button_func)
wrong_button.grid(row=1, column=0)

SIDE_FLAG = "front"
flip_card()

window.mainloop()
