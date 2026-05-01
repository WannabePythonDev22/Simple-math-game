import tkinter as tk
from tkinter import messagebox
from tkinter import Entry
import random

def hi():
    global answer
    user_input = E.get()
    if int(user_input) == answer:
        label.config(text="answer is correct")
    else:
        label.config(text="Answer is wrong")
def delete():
    global answer
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    answer = num1 + num2
    label.config(text=f"What is {num1} + {num2}")
    E.delete(0, "end")
def QUIT():
    root.destroy()

root = tk.Tk()
num1 = random.randint(1,100)
num2 = random.randint(1,100)
answer = num1 + num2

label = tk.Label(root, text=f"What is {num1} + {num2}", font=("Italic", 25))
label.pack()
E = tk.Entry(root, font=("Italic", 25))
E.pack()
Button = tk.Button(root, text=f"Enter", command=hi, font=("Italic", 25))
Button.pack()
Button2 = tk.Button(root, text=f"Reset", command=delete)
Button2.pack()
Button3 = tk.Button(root, text=f"Quit", command=QUIT).pack(pady=100)





root.mainloop()
