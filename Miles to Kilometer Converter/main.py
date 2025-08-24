from tkinter import *

def conversion():
    mile = float(in_miles.get())
    kms=mile*1.609
    in_kilo.config(text=f"{kms} ")
#creating the screen
window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=200,height=200)
window.configure(bg="lightblue",padx=20,pady=20)
# img = PhotoImage(file="car1.gif")
# label=Label(image=img)
# label.grid(column=5,row=5)
#creating labels
miles = Label(text="Miles",font=("Times New Roman",10))
miles.grid(column=3,rows=2)
equal = Label(text="is equal to",font=("Times New Roman",10,"bold normal"))
equal.grid(column=1,row=2)
km = Label(text="Km",font=("Times New Roman",10))
km.grid(column=3,row=2)
#creating entry
in_miles = Entry(width=8)
# in_miles.insert(END,string="enter miles")
print(in_miles.get())
in_miles.grid(column=2,row=1)
in_kilo=Label(width=8)
in_kilo.grid(column=2,row=2)
#button


cal = Button(text="Calculate",command=conversion)
cal.grid(column=2,row=4)

window.mainloop()