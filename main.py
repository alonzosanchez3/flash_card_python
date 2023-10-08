import tkinter
import pandas
import random

BACKGROUND_COLOR = '#B1DDC6'
data = pandas.read_csv('./data/french_words.csv')
to_learn = data.to_dict(orient='records')

def next_card():
  current_card = random.choice(to_learn)
  canvas.itemconfig(card_title, text="French")
  canvas.itemconfig(card_word, text=current_card['French'])



window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

checkmark_image = tkinter.PhotoImage(file="./images/right.png")
x_image = tkinter.PhotoImage(file="./images/wrong.png")
card_front_image = tkinter.PhotoImage(file="./images/card_front.png")
card_back_image = tkinter.PhotoImage(file="./images/card_back.png")

canvas = tkinter.Canvas(width=800, height=526)
canvas.create_image(400,263,image=card_front_image)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, 'italic'), fill='black')
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, 'bold'), fill='black')
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

unknown_button = tkinter.Button(image=x_image, highlightthickness=0, bd=0, command=next_card)
unknown_button.grid(row=1, column=0)

known_button = tkinter.Button(image=checkmark_image, highlightthickness=0, bd=0, command=next_card)
known_button.grid(row=1, column=1)

next_card()






window.mainloop()