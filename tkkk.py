from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox

window=Tk()
window.title=("tkinter image")
window.geometry("600x600")
uplaod=Image.open('wal.jpeg')


image=ImageTk.PhotoImage(uplaod)


Label=Label(image=image,width=300,height=300)
Label.place(x=100,y=100)


def msg():

    messagebox.showwarning("alert! data is not safe")
btn=Button(text="click me",command=msg)

btn.place(y="200",x="200")
window.mainloop()