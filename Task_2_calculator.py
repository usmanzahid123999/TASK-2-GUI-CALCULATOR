import tkinter as tk

def add_text(text):
    current_text = input_text.get()
    input_text.set(current_text + text)

def clear_text():
    input_text.set("")

def calculate():
    try:
        expression = input_text.get()
        result = eval(expression)
        input_text.set(result)
    except:
        input_text.set("Error")

root = tk.Tk()
root.title("Simple Calculator")

input_text = tk.StringVar()

text_box = tk.Entry(root, textvariable=input_text, font=("Helvetica", 18))
text_box.pack(padx=10, pady=10, ipadx=20, ipady=10, fill=tk.BOTH, expand=True)

button_frame = tk.Frame(root)
button_frame.pack(fill=tk.BOTH, expand=True)

button_text = ["7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "-", "0", ".", "=", "+"]
for i in range(4):
    for j in range(4):
        index = i * 4 + j
        text = button_text[index]
        if text == "=":
            button = tk.Button(button_frame, text=text, command=calculate, font=("Helvetica", 18))
        else:
            button = tk.Button(button_frame, text=text, command=lambda t=text: add_text(t), font=("Helvetica", 18))
        button.grid(row=i, column=j, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")
        button_frame.columnconfigure(j, weight=1)
        button_frame.rowconfigure(i, weight=1)

clear_button = tk.Button(root, text="Clear", command=clear_text, font=("Helvetica", 18))
clear_button.pack(padx=10, pady=10, ipadx=20, ipady=10, fill=tk.BOTH, expand=True)

root.mainloop()
