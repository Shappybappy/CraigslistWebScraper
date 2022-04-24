#GUI.py
import tkinter as tk

from Results import results

root = tk.Tk()
root.title("Craigslist scraper")

canvas = tk.Canvas(root, height=700, width=1200, bg="#263d42")

frame1 = tk.Frame(root, bg="gray")
frame1.place(relwidth=0.5, relheight=0.7, relx=0.25, rely=0.05)

entryTK = tk.Entry(frame1, width=30)

def myClick():
    return results(entryTK.get())

def displayOutput():
    display_label = tk.Label(root, text=myClick()) 
    display_label.pack()

    textVar = tk.StringVar()
    textVar.set(' '.join(link for link in myClick().split(' ') if link.startswith('https')))
    output_entry = tk.Entry(root, state="readonly", textvariable=textVar, width=100)
    output_entry.pack()

def close():
    root.destroy()

button1 = tk.Button(frame1, text="Specify", command=displayOutput)
button2 = tk.Button(frame1, text="done", command=close)

canvas.pack()
button1.pack()
entryTK.pack()
button2.pack()

root.mainloop()
