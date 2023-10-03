import tkinter as tk
from tkinter import filedialog


def file_loading():
    file_path = filedialog.askopenfilename(filetypes=[("XML files", "*.xml"), ("CSV files", "*.csv"), ("JSON files", "*.json")])
    if file_path:
        with open(file_path, 'r') as file:
            file_contents = file.read()

myapp_title = tk.Tk()
myapp_title.title("Assignment 2")

appBox = tk.Frame(myapp_title, padx=20, pady=20)
appBox.pack()

title_box = tk.Label(appBox, text="Select a file to load:")
title_box.pack(pady=10)

load_button = tk.Button(appBox, text="Load File", command=file_loading)
load_button.pack()
myapp_title.mainloop()
