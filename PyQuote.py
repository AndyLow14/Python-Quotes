# Obtain Inspirational Quotes by using Python, "https://quotes.rest/qod"
from concurrent.futures import thread
from ctypes import alignment, sizeof
from textwrap import wrap
import requests
import tkinter as tk
import datetime as dt
from threading import Thread

api = "http://api.quotable.io/random"
quotes = []
i_quote = 0
curr_quote = ""

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

def save():
    global curr_quote

    f = open("archive.txt", "a")
    f.write(curr_quote + "\n\n")
    f.close()
    # Disable button after one click
    save_button.config(state="disabled")

# UI
quote_label = tk.Label(window, font=("Minecraftia", 18), background="black", foreground="white", wraplength=590)
quote_label.pack(padx=35, pady=10)
quote_label.place(relx=.5, rely=.5, anchor="c")
save_button = tk.Button(window, text="SAVE", font=("Minecraftia", 12), background="black", foreground="white", activebackground="black", relief="solid", anchor="c", command=save)
save_button.tkraise()
save_button.pack(side="top", anchor="ne", padx=10, pady=10)

def get_random_quote():
    global quote_label
    global quotes
    global curr_quote

    curr_quote = quotes.pop(0)
    quote_label.config(text=curr_quote)
    # Re-enable button
    save_button.config(state="normal")

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

