import random
from tkinter import *
from PIL import Image, ImageTk

ls_1 = ("rock", "paper", "scissor")
n = 0
m = 0

window = Tk()
window.geometry("1000x700")
window.resizable(height=0, width=0)
window.title("Rock-Paper-Scissor")
window["bg"] = "black"


def rps():
    global n
    global m
    global a
    global b
    if ls_2 in ls_1:
        if ls_2 == com_choice:
            a = "It's a draw..."
            n += 1
            m += 1
        elif com_choice == "rock":
            if ls_2 == "paper":
                a = "You won"
                n += 1
            if ls_2 == "scissor":
                a = "Computer won"
                m += 1
        elif com_choice == "paper":
            if ls_2 == "scissor":
                a = "You won"
                n += 1
            if ls_2 == "rock":
                a = "Computer won"
                m += 1
        elif com_choice == "scissor":
            if ls_2 == "rock":
                a = "You won"
                n += 1
            if ls_2 == "paper":
                a = "Computer won..."
                m += 1
        b = f"your response = {ls_2} and computer response = {com_choice}"

def score():
    if n == m:
        c = "it's draw"
    elif n > m:
        c = "You are in lead..! "
    else:
        c = "Computer is in lead...:("
    l4.config(text=c)


def b1():
    global ls_2
    global com_choice
    ls_2 = "rock"
    com_choice = random.choice(ls_1)
    rps()
    l1.config(text=a)
    l4.config(text="")


def b2():
    global ls_2
    global com_choice
    ls_2 = "paper"
    com_choice = random.choice(ls_1)
    rps()
    l1.config(text=a)
    l4.config(text="")


def b3():
    global ls_2
    global com_choice
    ls_2 = "scissor"
    com_choice = random.choice(ls_1)
    rps()
    l1.config(text=a)
    l4.config(text="")


# b1 image change
def b1change(e):
    r12 = Image.open("rock12.png")
    r21 = r12.resize((180, 180), Image.ANTIALIAS)
    ro2 = ImageTk.PhotoImage(r21)
    bu1.config(image=ro2)
    bu1.image = ro2


def b1change1(f):
    bu1.config(image=r)


# b2 image change
def b2change(e):
    r22 = Image.open("paper12.png")
    r22 = r22.resize((180, 180), Image.ANTIALIAS)
    ro3 = ImageTk.PhotoImage(r22)
    bu2.config(image=ro3)
    bu2.image = ro3


def b2change1(f):
    bu2.config(image=p)


# b3 image change
def b3change(e):
    r32 = Image.open("scissor12.png")
    r33 = r32.resize((180, 180), Image.ANTIALIAS)
    ro4 = ImageTk.PhotoImage(r33)
    bu3.config(image=ro4)
    bu3.image = ro4


def b3change1(f):
    bu3.config(image=s)


# label credits
lc = Label(window, text="Created by Shannu", bg="black", fg="green", font=("lucida handwriting", 10))
lc.place(x=800, y=670)
# label play
l3 = Label(window, text="To play select the following buttons...", bg="black", fg="mintcream", font=("consolas", 30))
l3.place(x=60, y=140)
# result
l4 = Label(window, text="", bg="black", fg="mintcream", font=("consolas", 32))
l4.place(x=60, y=570)
# rock
r1 = Image.open("rock11.png")
r2 = r1.resize((180, 180), Image.ANTIALIAS)
r = ImageTk.PhotoImage(r2)
# paper
p1 = Image.open("paper11.png")
p2 = p1.resize((180, 180), Image.ANTIALIAS)
p = ImageTk.PhotoImage(p2)
# scissors
s1 = Image.open("scissors11.png")
s2 = s1.resize((180, 180), Image.ANTIALIAS)
s = ImageTk.PhotoImage(s2)
# label
l1 = Label(window, text='', bg="black", fg="mintcream", font=("calibri", 30))
l1.place(x="60", y="420")
# headings
l2 = Label(window, text="Rock-Paper-Scissor", bg="black", fg="mintcream", font=("Segoe Print", 46))
l2.place(x="50", y="10")

# buttons
# rock button
fr = Frame(window)
fr.place(x=150, y=230)
bu1 = Button(fr, image=r, command=b1, borderwidth=0, bg="white")
bu1.pack()
# paper button
fb = Frame(window)
fb.place(x=350, y=230)
bu2 = Button(fb, image=p, command=b2, borderwidth=0)
bu2.pack()
# scissor button
fs = Frame(window)
fs.place(x=550, y=230)
bu3 = Button(fs, image=s, command=b3, borderwidth=0)
bu3.pack()
# result
result = Button(window, text="See Result", command=score, borderwidth=0, font=("MV Boli", 16))
result.place(x=150, y=500)
# hovering
# button 1
bu1.bind("<Enter>", b1change)
bu1.bind("<Leave>", b1change1)
# button 2
bu2.bind("<Enter>", b2change)
bu2.bind("<Leave>", b2change1)
# button 3
bu3.bind("<Enter>", b3change)
bu3.bind("<Leave>", b3change1)

window.mainloop()
