# Obtain Inspirational Quotes by using Python, "https://quotes.rest/qod"
from concurrent.futures import thread
from ctypes import sizeof
from textwrap import wrap
import requests
import tkinter as tk
import datetime as dt
from threading import Thread

api = "http://api.quotable.io/random"
quotes = []

# Tkinter Window
window = tk.Tk()
window.geometry('625x270+1980+50')
window.title("PyQuote")
window.configure(background='black')
window.overrideredirect(1)

# Functions
def load_quotes():
    global quotes
    for i in range(30):
        random_quote = requests.get(api).json()
        content = random_quote["content"]
        author = random_quote["author"]
        quote = content + "\n\n" + "~ " + author

        quotes.append(quote)

load_quotes()

# UI
quote_label = tk.Label(window, font=("Advent Pro Light", 20), background="black", foreground="white", wraplength=590)
quote_label.pack(padx=20, pady=10)
quote_label.place(relx=.5, rely=.5, anchor="c")

def get_random_quote():
    global quote_label
    global quotes

    quote_label.config(text=quotes.pop())

    if len(quotes) == 11:
        thread = Thread(target=load_quotes)
        thread.start()


get_random_quote()

def change():
    quote_label.after(1000, change)
    print(len(quotes))
    get_random_quote()


# Quote timer
change()

# Keep program alive
tk.mainloop()

