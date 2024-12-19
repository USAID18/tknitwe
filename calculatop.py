from tkinter import*

window=Tk()

window.geometry("600x600")

mainlabel=Label(text="enter you number")
mainlabel.place(x="260",y="150")
mainentry=Entry()
mainentry.place(x="255",y="180")
mainbutton=Button(text="calculate",bg="black",fg="white")
mainbutton.place(x="270",y="210")

secondlabel=Label(text="Here is your dominataion")
secondlabel.place(x="230",y="250")

l1=Label(text="2000")
l1.place(x="230",y="270")
l2=Label(text="3000")
l2.place(x="230",y="300")
l3=Label(text="4000")
l3.place(x="230",y="330")

el=Entry()
el.place(x="260",y="270")
e2=Entry()
e2.place(x="260",y="300")
e3=Entry()
e3.place(x="260",y="330")

def calculator():

    global amount
    amount=int(mainentry.get())
    note2000 =amount // 2000
    amount%=2000

    note400 = amount // 4000
    amount%=4000


    note3000 = amount // 3000
    amount%=3000



window.mainloop()
