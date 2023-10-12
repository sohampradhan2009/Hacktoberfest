import tkinter as tk

# Function to update the display
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + number)

# Function to perform the calculation
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Entry widget to display the input and results
entry = tk.Entry(window, width=20, font=('Helvetica', 20))
entry.grid(row=0, column=0, columnspan=4)

# Define the button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create and position the buttons
row = 1
col = 0
for button_text in buttons:
    button = tk.Button(window, text=button_text, width=5, height=2, font=('Helvetica', 20),
                       command=lambda text=button_text: button_click(text) if text != '=' else calculate())
    button.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the main loop
window.mainloop()
