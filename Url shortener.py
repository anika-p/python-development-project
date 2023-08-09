import pyshorteners
from tkinter import *

win= Tk()
win.geometry("400x270")
win.configure(bg="pink")

#creating URL shortener function
def short():
    url=entry1.get()
    #shorten url
    s=pyshorteners.Shortener().tinyurl.short(url)
    #output it to screen
    entry2.insert(END,s)

#Creating the GUI  
#label1  
l1=Label(win,text="Enter your URL link",font="impack 17 bold",bg="black",fg="white")
l1.pack(fill="x")
#Entry box1
entry1=Entry(win,font="10",bd="3",width="40")
entry1.pack(pady=30)
#button
b1=Button(win,text="Submit URL",font="impack 12 bold",bg="blue",fg="white",width="14",command=short)
b1.pack()
#label2  
l2=Label(win,text="Your shorten URL",font="impack 17 bold",bg="black",fg="white")
l2.pack(fill="x",pady=30)
#Entry box2
entry2=Entry(win,font="impack 16 bold",bg="pink",width="24",bd=0)
entry2.pack(pady=10)

mainloop()