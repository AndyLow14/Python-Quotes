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
i_quote = 0

# Tkinter Window
window = tk.Tk()
window.geometry('625x270+1980+50')
window.title("PyQuote")
window.configure(background='black')
window.overrideredirect(1)

# Functions
def load_quotes():
    global quotes
    global i_quote
    for i in range(10):
        random_quote = requests.get(api).json()
        content = random_quote["content"]
        # Skip quote if more than 120 characters (4 lines)
        if len(content) > 120:
            continue
        author = random_quote["author"]
        quote = "- #" + str(i_quote) + " " + author + " -" + "\n\n" + content
        i_quote += 1

        quotes.append(quote)

load_quotes()

# UI
quote_label = tk.Label(window, font=("Minecraftia", 18), background="black", foreground="white", wraplength=590)
quote_label.pack(padx=35, pady=10)
quote_label.place(relx=.5, rely=.5, anchor="c")

def get_random_quote():
    global quote_label
    global quotes

    quote_label.config(text=quotes.pop(0))

    if len(quotes) == 1:
        thread = Thread(target=load_quotes)
        thread.start()


get_random_quote()

def change():
    # Update every 10 minutes
    quote_label.after(600000, change)
    get_random_quote()


# Quote timer
change()

# Keep program alive
tk.mainloop()

