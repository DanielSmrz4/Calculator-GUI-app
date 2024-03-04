from customtkinter import *
import re
import math

# Appereance
set_appearance_mode("Dark")
set_default_color_theme("blue")

# Window
window = CTk()
window.geometry("240x380+800+400")
window.resizable(False, False)
window.title("Quick Math")
window.iconbitmap("calculator3.ico")

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)


# FUNCTIONS -------------------------------------/
# Number buttons
def click_1():
    value = my_var.get()
    button_value = "1"
    if value == "0":
        my_var.set(button_value)
    else:
        my_var.set(value + button_value)


def click_2():
    value = my_var.get()
    button_value = "2"
    if value == "0":
        my_var.set(button_value)
    else:
        my_var.set(value + button_value)


def click_3():
    value = my_var.get()
    button_value = "3"
    if value == "0":
        my_var.set(button_value)
    else:
        my_var.set(value + button_value)


def click_4():
    value = my_var.get()
    button_value = "4"
    if value == "0":
        my_var.set(button_value)
    else:
        my_var.set(value + button_value)


def click_5():
    value = my_var.get()
    button_value = "5"
    if value == "0":
        my_var.set(button_value)
    else:
        my_var.set(value + button_value)


def click_6():
    value = my_var.get()
    button_value = "6"
    if value == "0":
        my_var.set(button_value)
    else:
        my_var.set(value + button_value)


def click_7():
    value = my_var.get()
    button_value = "7"
    if value == "0":
        my_var.set(button_value)
    else:
        my_var.set(value + button_value)


def click_8():
    value = my_var.get()
    button_value = "8"
    if value == "0":
        my_var.set(button_value)
    else:
        my_var.set(value + button_value)


def click_9():
    value = my_var.get()
    button_value = "9"
    if value == "0":
        my_var.set(button_value)
    else:
        my_var.set(value + button_value)


def click_0():
    value = my_var.get()
    button_value = "0"
    if value == "0":
        my_var.set(button_value)
    else:
        my_var.set(value + button_value)


def click_point_number():
    value = my_var.get()
    button_value = "."
    if "." not in value:
        my_var.set(value + button_value)


# MATH OPERATIONS -----------------------------------/
def division():
    value1 = my_var.get()
    num1.set(value1)
    num2.set("")
    special_char.set("/")
    my_var.set("")


def multiply():
    value1 = my_var.get()
    num1.set(value1)
    num2.set("")
    special_char.set("*")
    my_var.set("")


def plus():
    value1 = my_var.get()
    num1.set(value1)
    num2.set("")
    special_char.set("+")
    my_var.set("")


def minus():
    value1 = my_var.get()
    num1.set(value1)
    num2.set("")
    special_char.set("-")
    my_var.set("")


# Equals
def equals():
    num2.set(my_var.get())
    try:
        first = float(num1.get())
        second = float(num2.get())
        if special_char.get() == "/":
            try:
                result = first / second
                if first % second == 0:
                    my_var.set(str(int(result)))
                else:
                    my_var.set(str(round(result, 4)))
            except ZeroDivisionError:
                my_var.set("0")
        elif special_char.get() == "*":
            result = first * second
            if int(result) / second == first:
                result = int(result)
                my_var.set(str(result))
            else:
                my_var.set(str(round(result, 4)))
        elif special_char.get() == "+":
            result = first + second
            if int(result) - second == first:
                result = int(result)
                my_var.set(str(result))
            else:
                my_var.set(str(round(result, 4)))
        elif special_char.get() == "-":
            result = first - second
            if int(result) + second == first:
                result = int(result)
                my_var.set(str(result))
            else:
                my_var.set(str(round(result, 4)))
    except ValueError:
        pass


def reset():
    my_var.set(value="0")
    num1.set("")
    special_char.set("")
    num2.set("")


# ----------------------------------------------------/
my_var = StringVar()
my_var.set(value="0")

num1 = StringVar()
special_char = StringVar()
num2 = StringVar()

# SIDE COUNTING --------------------------------------/
# Frame for side counting
frame_side_counting = CTkFrame(window, height=10, bg_color="transparent")
frame_side_counting.pack(fill=BOTH, expand=False, padx=10, pady=10)

# Label num1
label_num1 = CTkLabel(frame_side_counting, textvariable=num1, font=("Helvetica", 13, "italic"))
label_num1.grid(row=0, column=0, padx=5)

# Label specials
label_specials = CTkLabel(frame_side_counting, textvariable=special_char, font=("Helvetica", 14))
label_specials.grid(row=0, column=1, padx=5)

# Label num2
label_num2 = CTkLabel(frame_side_counting, textvariable=num2, font=("Helvetica", 13, "italic"))
label_num2.grid(row=0, column=2, padx=5)

# WIDGETS --------------------------------------------/
# Label main
label_main = CTkLabel(window, textvariable=my_var, height=25, font=("Helvetica", 35))
label_main.pack(fill="x")

# Frame for buttons
frame_text = CTkFrame(window, height=40)
frame_text.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Buttons 1, 2, 3, /
button_1 = CTkButton(frame_text, text="1", width=40, height=40, font=("Helvetica", 20, "bold"), command=click_1)
button_1.grid(row=0, column=0, pady=10, padx=7, sticky="we")
button_2 = CTkButton(frame_text, text="2", width=40, height=40, font=("Helvetica", 20, "bold"), command=click_2)
button_2.grid(row=0, column=1, pady=10, padx=7, sticky="we")
button_3 = CTkButton(frame_text, text="3", width=40, height=40, font=("Helvetica", 20, "bold"), command=click_3)
button_3.grid(row=0, column=2, pady=10, padx=7, sticky="we")
button_division = CTkButton(frame_text, text="/", width=40, height=40, font=("Helvetica", 20, "bold"),
                            fg_color="#ff9100", hover_color="#884d00", command=division)
button_division.grid(row=0, column=3, pady=10, padx=7, sticky="we")

# Buttons 4, 5, 6, *
button_4 = CTkButton(frame_text, text="4", width=40, height=40, font=("Helvetica", 20, "bold"), command=click_4)
button_4.grid(row=1, column=0, pady=5, padx=7, sticky="we")
button_5 = CTkButton(frame_text, text="5", width=40, height=40, font=("Helvetica", 20, "bold"), command=click_5)
button_5.grid(row=1, column=1, pady=5, padx=7, sticky="we")
button_6 = CTkButton(frame_text, text="6", width=40, height=40, font=("Helvetica", 20, "bold"), command=click_6)
button_6.grid(row=1, column=2, pady=5, padx=7, sticky="we")
button_multiply = CTkButton(frame_text, text="*", width=40, height=40, font=("Helvetica", 20, "bold"),
                            fg_color="#ff9100", hover_color="#884d00", command=multiply)
button_multiply.grid(row=1, column=3, pady=5, padx=7, sticky="we")

# Buttons 7, 8, 9, +
button_7 = CTkButton(frame_text, text="7", width=40, height=40, font=("Helvetica", 20, "bold"), command=click_7)
button_7.grid(row=2, column=0, pady=5, padx=7, sticky="we")
button_8 = CTkButton(frame_text, text="8", width=40, height=40, font=("Helvetica", 20, "bold"), command=click_8)
button_8.grid(row=2, column=1, pady=5, padx=7, sticky="we")
button_9 = CTkButton(frame_text, text="9", width=40, height=40, font=("Helvetica", 20, "bold"), command=click_9)
button_9.grid(row=2, column=2, pady=5, padx=7, sticky="we")
button_plus = CTkButton(frame_text, text="+", width=40, height=40, font=("Helvetica", 20, "bold"), fg_color="#ff9100",
                        hover_color="#884d00", command=plus)
button_plus.grid(row=2, column=3, pady=5, padx=7, sticky="we")

# Buttons CE, 0, . , -
button_reset = CTkButton(frame_text, text="CE", width=40, height=40, font=("Helvetica", 20,), command=reset)
button_reset.grid(row=3, column=0, pady=5, padx=7, sticky="we")
button_0 = CTkButton(frame_text, text="0", width=40, height=40, font=("Helvetica", 20, "bold"), command=click_0)
button_0.grid(row=3, column=1, pady=5, padx=7, sticky="we")
button_dot = CTkButton(frame_text, text=".", width=40, height=40, font=("Helvetica", 20, "bold"),
                       command=click_point_number)
button_dot.grid(row=3, column=2, pady=5, padx=7, sticky="we")
button_minus = CTkButton(frame_text, text="-", width=40, height=40, font=("Helvetica", 20, "bold"), fg_color="#ff9100",
                         hover_color="#884d00", command=minus)
button_minus.grid(row=3, column=3, pady=5, padx=7, sticky="we")

# Button =
button_equals = CTkButton(frame_text, text="=", width=40, height=40, font=("Helvetica", 20, "bold"), fg_color="#726777",
                          hover_color="#584f5c", command=equals)
button_equals.grid(row=4, column=0, columnspan=4, pady=(10, 0), padx=7, sticky="wes")

window.mainloop()
