from tkinter import *
from tkinter import messagebox
from pandas import *
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
df={}

def end():
    messagebox.showinfo(
        "🎉 مبروك! 🎉",
        "تهانينا!\n\n"
        "لقد أتممت تعلم جميع الـ 1000 كلمة!\n\n"
        "🌟 إنجاز رائع! 🌟\n\n"
        "استمر في الممارسة!"
    )
try:
    df = read_csv("data/words_to_learn.csv")
except:
    df = read_csv("data/Arabic_words.csv")
finally:
    if len(df) == 0:
        end()
    data = df.to_dict(orient="records")



def right_word():
    global data
    if len(data) != 0:
        data.remove(current_card)
        df = DataFrame(data)
        df.to_csv("data/words_to_learn.csv", index=False)
        next_card()
    else:
        root.destroy()
        end()

def next_card():
    card.itemconfig(card_img, image=front_img)

    global current_card , timer
    root.after_cancel(timer)
    current_card = random.choice(data)
    card.itemconfig(language, text="English", fill= "black")
    card.itemconfig(word, text=current_card["English"], fill= "black")
    timer = root.after(3000, func=flip_card)


def flip_card():
    card.itemconfig(card_img,image=back_img)
    card.itemconfig(language, text="Arabic" , fill= "white")
    card.itemconfig(word, text=current_card["Arabic"] ,fill= "white")

root = Tk()
root.title("Flashy")
root.config(padx=50, pady=50)
root.config(bg=BACKGROUND_COLOR)
timer = root.after(3000, func=flip_card)

front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_img = card.create_image(400, 263, image= front_img)
language = card.create_text(400,150,text="", font=("Ariel",40,"italic"))
word = card.create_text(400,263,text="", font=("Ariel",60,"bold"))
card.grid(column=0,row=0,columnspan=2)


right_image = PhotoImage(file="images/right.png")
right = Button(image=right_image, highlightthickness=0,command=right_word)
right.grid(column=1,row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_image, highlightthickness=0,command=next_card)
wrong.grid(column=0,row=1)

next_card()




root.mainloop()