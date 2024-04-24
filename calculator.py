from tkinter import *

expression = ''
def press(num):
    global expression
    expression = expression+str(num)
    equation.set(expression)

def pressequal():
    try:
        global expression
        result = str(eval(expression))
        equation.set(result)
        expression=''
    except:
        equation.set("Invalid")
        expression=''

def ac():
    global expression
    equation.set("")
    expression = ''

if __name__=="__main__":
    root = Tk()
    root.geometry("460x380")
    root.configure(background="white")
    root.title("Simple Calculator")

    equation = StringVar()
    values_entry = Entry(root, textvariable=equation, justify="center", width=60, borderwidth=2, relief="solid")
    values_entry.grid(columnspan=80, column=2, row=2, ipady=10, pady=15, padx=40)

    btn1 = Button(root, text=" 1 ", bg="grey", fg="black", command=lambda: press(1), height=2, width=10)
    btn1.grid(row= 3, column=30, padx=10, pady=10)

    btn2 = Button(root, text=" 2 ", bg="grey", fg="black", command=lambda: press(2), height=2, width=10)
    btn2.grid(row= 3, column=40)

    btn3 = Button(root, text=" 3 ", bg="grey", fg="black", command=lambda: press(3), height=2, width=10)
    btn3.grid(row= 3, column=50)

    btn4 = Button(root, text=" 4 ", bg="grey", fg="black", command=lambda: press(4), height=2, width=10)
    btn4.grid(row= 5, column=30, padx=10, pady=10)

    btn5 = Button(root, text=" 5 ", bg="grey", fg="black", command=lambda: press(5), height=2, width=10)
    btn5.grid(row= 5, column=40)

    btn6 = Button(root, text=" 6 ", bg="grey", fg="black", command=lambda: press(6), height=2, width=10)
    btn6.grid(row= 5, column=50)

    btn7 = Button(root, text=" 7 ", bg="grey", fg="black", command=lambda: press(7), height=2, width=10)
    btn7.grid(row= 7, column=30, padx=10, pady=10)

    btn8 = Button(root, text=" 8 ", bg="grey", fg="black", command=lambda: press(8), height=2, width=10)
    btn8.grid(row= 7, column=40)

    btn9 = Button(root, text=" 9 ", bg="grey", fg="black", command=lambda: press(9), height=2, width=10)
    btn9.grid(row= 7, column=50)

    btn0 = Button(root, text=" 0 ", bg="grey", fg="black", command=lambda: press(0), height=2, width=10)
    btn0.grid(row= 9, column=30, padx=10, pady=10)

    btn_dec = Button(root, text=" . ", bg="grey", fg="black", command=lambda: press('.'), height=2, width=10)
    btn_dec.grid(row= 9, column=40)

    equ = Button(root, text=" = ", bg="grey", fg="black", command=pressequal, height=2, width=10)
    equ.grid(row= 9, column=50)

    add = Button(root, text=" + ", bg="grey", fg="black", command=lambda: press('+'), height=2, width=10)
    add.grid(row= 3, column=60)

    sub = Button(root, text=" - ", bg="grey", fg="black", command=lambda: press('-'), height=2, width=10)
    sub.grid(row= 5, column=60)

    mul= Button(root, text=" * ", bg="grey", fg="black", command=lambda: press('*'), height=2, width=10)
    mul.grid(row= 7, column=60)

    div = Button(root, text=" / ", bg="grey", fg="black", command=lambda: press('/'), height=2, width=10)
    div.grid(row= 9, column=60)

    clear = Button(root, text=" AC ", bg="grey", fg="black", command=ac, height=2, width=10)
    clear.grid(row= 10, column=30, columnspan=60)

    root.mainloop()
