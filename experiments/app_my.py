import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
timer = None
ENGLISH_RAN_WORD = ""
timer = None


# -------------------------------------------- READ DATA --------------------------------------------

def generate_french_word():
    global ENGLISH_RAN_WORD
    global SIDE_FLAG
    global timer

    canvas.itemconfig(canvas_image, image=card_front_image)
    data = pandas.read_csv("../data/french_words.csv")
    data_list = data.to_dict(orient="records")
    # print(data_list)
    ran_word = random.choice(data_list)
    french_ran_word = ran_word["French"]
    ENGLISH_RAN_WORD = ran_word["English"]
    canvas.itemconfig(language_t, text="French")
    canvas.itemconfig(word_t, text=french_ran_word)
    window.after_cancel(timer)
    SIDE_FLAG = "back"
    timer = window.after(3000, flip_card)


def change_card():
    global ENGLISH_RAN_WORD

    data = pandas.read_csv("../data/french_words.csv")
    data_list = data.to_dict(orient="records")
    # print(data_list)
    ran_word = random.choice(data_list)
    french_ran_word = ran_word["French"]
    ENGLISH_RAN_WORD = ran_word["English"]
    if SIDE_FLAG == "front":
        canvas.itemconfig(language_t, text="French")
        canvas.itemconfig(word_t, text=french_ran_word)


# def generate_english_word():
#     data = pandas.read_csv("./data/french_words.csv")
#     data_list = data.to_dict(orient="records")
#     ran_word = random.choice(data_list)
#     ENGLISH_RAN_WORD = ran_word["English"]
#     canvas.itemconfig(language_t, text="English", fill="white")
#     canvas.itemconfig(word_t, text=ENGLISH_RAN_WORD, fill="white")


# -------------------------------------------- FLIP CARD --------------------------------------------


# -------------------------------------------- UI --------------------------------------------

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# If PhotoImage objects created inside a function, it will not work.
# Front is french and back is english.
card_front_image = PhotoImage(file="../images/card_front.png")
card_back_image = PhotoImage(file="../images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR)

language_t = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word_t = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))

# Here column span represents the number of columns to which we want to place our canvas.
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="../images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=generate_french_word)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="../images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=generate_french_word)
wrong_button.grid(row=1, column=0)

# generate_french_word()

SIDE_FLAG = "front"


def flip_card():
    global timer
    timer = window.after(3000, flip_card)

    # fornt is French
    # back is English
    global SIDE_FLAG
    if SIDE_FLAG == "back":
        canvas.itemconfig(canvas_image, image=card_back_image)
        canvas.itemconfig(language_t, text="English")
        canvas.itemconfig(word_t, text=ENGLISH_RAN_WORD)

        SIDE_FLAG = "front"
    elif SIDE_FLAG == "front":
        canvas.itemconfig(canvas_image, image=card_front_image)
        change_card()
        SIDE_FLAG = "back"


flip_card()

window.mainloop()
