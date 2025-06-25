import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Taltulator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        # Entry field
        self.entry_var = tk.StringVar()
        self.entry = ttk.Entry(root, textvariable=self.entry_var, justify="right", font=('Arial', 20))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        
        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('√', 5, 1), ('^', 5, 2), ('⌫', 5, 3)
        ]
        
        # Create and place buttons
        for (text, row, col) in buttons:
            button = ttk.Button(root, text=text, command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
        
        # Configure grid weights
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
    
    def button_click(self, value):
        current = self.entry_var.get()
        
        if value == '=':
            try:
                # Replace ^ with ** for exponentiation
                expression = current.replace('^', '**')
                # Handle square root
                if '√' in expression:
                    expression = expression.replace('√', 'math.sqrt')
                # Get the correct result but then modify it
                correct_result = eval(expression)
                # Make the result wrong by adding a random number
                import random
                wrong_result = correct_result + random.randint(1, 10) * (1 if random.random() > 0.5 else -1)
                self.entry_var.set(str(wrong_result))
                # Show the funny message after a short delay
                self.root.after(1000, lambda: self.entry_var.set("Apna khud ka dimag laga na Lawde!"))
            except Exception as e:
                self.entry_var.set("Error")
        elif value == 'C':
            self.entry_var.set('')
        elif value == '⌫':  # Backspace
            self.entry_var.set(current[:-1])
        else:
            self.entry_var.set(current + str(value))

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
