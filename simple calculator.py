import tkinter as tk
from tkinter import messagebox

def click_button(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def clear_screen():
    global expression
    expression = ""
    input_text.set("")

def calculate():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        messagebox.showerror("Error", "Invalid Input")
        expression = ""

# Initialize the window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x500")

# Global variables
expression = ""
input_text = tk.StringVar()

# Create the input field
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

input_field = tk.Entry(input_frame, textvariable=input_text, font=('arial', 18, 'bold'), width=50, bd=5, insertwidth=4, bg="powder blue", justify='right')
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Create the buttons frame
btns_frame = tk.Frame(root)
btns_frame.pack()

# First row
clear = tk.Button(btns_frame, text="C", width=32, height=3, command=clear_screen).grid(row=0, column=0, columnspan=3)
divide = tk.Button(btns_frame, text="/", width=10, height=3, command=lambda: click_button("/")).grid(row=0, column=3)

# Second row
seven = tk.Button(btns_frame, text="7", width=10, height=3, command=lambda: click_button("7")).grid(row=1, column=0)
eight = tk.Button(btns_frame, text="8", width=10, height=3, command=lambda: click_button("8")).grid(row=1, column=1)
nine = tk.Button(btns_frame, text="9", width=10, height=3, command=lambda: click_button("9")).grid(row=1, column=2)
multiply = tk.Button(btns_frame, text="*", width=10, height=3, command=lambda: click_button("*")).grid(row=1, column=3)

# Third row
four = tk.Button(btns_frame, text="4", width=10, height=3, command=lambda: click_button("4")).grid(row=2, column=0)
five = tk.Button(btns_frame, text="5", width=10, height=3, command=lambda: click_button("5")).grid(row=2, column=1)
six = tk.Button(btns_frame, text="6", width=10, height=3, command=lambda: click_button("6")).grid(row=2, column=2)
minus = tk.Button(btns_frame, text="-", width=10, height=3, command=lambda: click_button("-")).grid(row=2, column=3)

# Fourth row
one = tk.Button(btns_frame, text="1", width=10, height=3, command=lambda: click_button("1")).grid(row=3, column=0)
two = tk.Button(btns_frame, text="2", width=10, height=3, command=lambda: click_button("2")).grid(row=3, column=1)
three = tk.Button(btns_frame, text="3", width=10, height=3, command=lambda: click_button("3")).grid(row=3, column=2)
plus = tk.Button(btns_frame, text="+", width=10, height=3, command=lambda: click_button("+")).grid(row=3, column=3)

# Fifth row
zero = tk.Button(btns_frame, text="0", width=21, height=3, command=lambda: click_button("0")).grid(row=4, column=0, columnspan=2)
decimal = tk.Button(btns_frame, text=".", width=10, height=3, command=lambda: click_button(".")).grid(row=4, column=2)
equals = tk.Button(btns_frame, text="=", width=10, height=3, command=calculate).grid(row=4, column=3)

# Run the main loop
root.mainloop()
