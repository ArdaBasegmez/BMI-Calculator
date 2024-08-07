from tkinter import *

FONT = ("consolas", 15, "bold")

window = Tk()
window.title("tkinter python")
window.minsize(width=600, height=600)
window.config(bg="midnight blue")
window.config(padx=100, pady=100)

label_one = Label(text="BMI CALCULATOR", font=FONT)
label_one.place(x=20, y=0)
label_one.config(bg="navy", fg="snow", padx=40, pady=16)

label_two = Label(text="Length", font=FONT)
label_two.place(x=20, y=80)
label_two.config(bg="dark olive green", fg="snow", padx=7, pady=7)

label_three = Label(text="Height", font=FONT)
label_three.place(x=20, y=160)
label_three.config(bg="dark olive green", fg="snow", padx=7, pady=7)

length_entry = Entry(width=20)
length_entry.place(x=150, y=90)

weight_entry = Entry(width=20)
weight_entry.place(x=150, y=170)


def ClickButton():
    user_length = length_entry.get()
    user_weight = weight_entry.get()
    print(float(user_length)**2/float(user_weight))

CalculationButton = Button(text="button", font=FONT, command=ClickButton)
CalculationButton.config(padx=10, pady=10)
CalculationButton.config(bg="dark olive green", fg="snow")
CalculationButton.place(x=270, y=0)

window.mainloop()