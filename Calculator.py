import tkinter as tk
import math
import cmath

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x600")
        self.expression = ""
        self.input_text = tk.StringVar()

        # Input field
        input_frame = tk.Frame(self.root, bd=10, relief=tk.RIDGE)
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, bd=5, insertwidth=4, bg="powder blue", justify='right')
        input_field.grid(columnspan=4)

        # Buttons frame
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack()

        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('/', 4, 3),
            ('C', 5, 0), ('(', 5, 1), (')', 5, 2), ('sqrt', 5, 3),
            ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('log', 6, 3),
            ('exp', 7, 0), ('pi', 7, 1), ('e', 7, 2), ('^', 7, 3),
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col, buttons_frame)

    def create_button(self, text, row, col, frame):
        button = tk.Button(frame, text=text, width=10, height=3, bd=5, font=('arial', 18, 'bold'),
                           command=lambda: self.button_click(text))
        button.grid(row=row, column=col, padx=1, pady=1)

    def button_click(self, item):
        if item == "=":
            self.calculate()
        elif item == "C":
            self.clear()
        elif item == "sqrt":
            self.expression += "math.sqrt("
            self.input_text.set(self.expression)
        elif item == "sin":
            self.expression += "math.sin(math.radians("
            self.input_text.set(self.expression)
        elif item == "cos":
            self.expression += "math.cos(math.radians("
            self.input_text.set(self.expression)
        elif item == "tan":
            self.expression += "math.tan(math.radians("
            self.input_text.set(self.expression)
        elif item == "log":
            self.expression += "math.log10("
            self.input_text.set(self.expression)
        elif item == "exp":
            self.expression += "math.exp("
            self.input_text.set(self.expression)
        elif item == "pi":
            self.expression += "math.pi"
            self.input_text.set(self.expression)
        elif item == "e":
            self.expression += "math.e"
            self.input_text.set(self.expression)
        elif item == "^":
            self.expression += "**"
            self.input_text.set(self.expression)
        else:
            self.expression += str(item)
            self.input_text.set(self.expression)

    def calculate(self):
        try:
            self.expression = str(eval(self.expression))
            self.input_text.set(self.expression)
        except Exception as e:
            self.input_text.set("Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.input_text.set("")

# Running the calculator
if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()
