#GUI.py
import time
import tkinter as tk


root = tk.Tk()
root.title("Craigslist scraper")

canvas = tk.Canvas(root, height=700, width=1200, bg="#263d42")

frame1 = tk.Frame(root, bg="gray")
frame1.place(relwidth=0.5, relheight=0.7, relx=0.25, rely=0.05)

entryTK = tk.Entry(root, width=30)


def myClick():
    label= tk.Label(root, text=entryTK.get())
    label.pack()
    return label.cget("text")

def close():
    root.destroy()
    time.sleep(10)
    print("closed")    

button1 = tk.Button(frame1, text="button", command=myClick)
button2 = tk.Button(frame1, text="done", command=close)

canvas.pack()
button1.pack()
button2.pack()
entryTK.pack()

root.mainloop()

