from tkinter  import *


def inchtocm():
    inch = float(inch_input.get())
    cm = inch * 2.54
    cm_result_label.config(text=cm)


window = Tk()
window.title("Inches to centimeter calculator")
#window.minsize(width=500,height=300)
window.config(padx=20 , pady=20)


inch_input = Entry(width=7)
inch_input.grid(column=1 , row=0)



inch_label = Label(text="Inches")
inch_label.grid(column=2 , row=0)



is_eq = Label(text="is equal to")
is_eq.grid(column=0 , row=1)



cm_result_label = Label(text="0")
cm_result_label.grid(column=1 , row=1)



cm_label = Label(text="Cm")
cm_label.grid(column=2 , row=1)




calc_button = Button(text="calculate" , command=inchtocm)
calc_button.grid(column=1 , row=2)




window.mainloop()

