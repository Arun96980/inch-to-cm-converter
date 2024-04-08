import tkinter as t
window = t.Tk()
window.title("window")
window.minsize(width=500,height=300)







window.mainloop()


def add(*arg):
    n1=5
    n2=4
    x1 = 2
    x = n1 + n2
    y =x1 + x
    print(y)

add()
i=1
while i < 10:
    add()
    i = i+1


def mul(*args):
    k = 3
    for i in args:
        k = k*i
    return(k)

print(mul(5,6,3,9,8,8,9,6,66,66,5,9,9,54,9,5,94))


