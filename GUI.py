#GUI.py
import tkinter as tk

from Results import results

root = tk.Tk()
root.title("Craigslist scraper")

canvas = tk.Canvas(root, height=450, width=790, bg="#5cbfd6")
canvas.pack()

frame1 = tk.Frame(canvas, bg="gray")
frame1.place(relwidth=0.3, relheight=0.3, relx=0.25, rely=0.05)

frame2 = tk.Frame(canvas, bg="gray")
frame2.place(relwidth=0.2, relheight=0.8, relx=0.001, rely=0.005)

rules = tk.Label(frame2, text='1.\n before every new search press\n "Restart Labels". \n 2. when the programming \n is searching for listings \n do not drag the page \n or else the program \n will cease to work')

p1 = tk.PhotoImage(file = 'Untitled-1.png')
root.iconphoto(False, p1)

entryTK = tk.Entry(frame1, width=30)

def myClick():
    return results(entryTK.get())

def displayOutput():
    global display_label
    global output_entry

    display_label = tk.Label(root, text=myClick(), font=("Helvetica", 9))
    display_label.pack()

    textVar = tk.StringVar()
    textVar.set(' '.join(link for link in myClick().split(' ') if link.startswith('https')))
    output_entry = tk.Entry(root, state="readonly", textvariable=textVar, width=100)
    output_entry.pack()

def killLabel():
    output_entry.destroy()
    display_label.destroy()    

def close():
    root.destroy()

button1 = tk.Button(frame1, text="Specify", command=displayOutput)
button2 = tk.Button(frame1, text="Close Program", command=close)
button3 = tk.Button(frame1, text="Restart Labels", command=killLabel)

button1.pack()
entryTK.pack()
button2.pack()
button3.pack()
rules.pack()


root.mainloop()
