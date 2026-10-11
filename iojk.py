import customtkinter as ctk

# Налаштування світлої теми для гарного рожевого вигляду
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

class PinkCalculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Налаштування вікна
        self.title("Pink Calculator")
        self.geometry("340x520")
        self.configure(fg_color="#FCE4EC")  # Ніжно-рожевий корпус
        self.resizable(False, False)

        self.expression = ""

        # --- Дисплей ---
        self.display_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=20, border_width=0)
        self.display_frame.pack(padx=15, pady=15, fill="x")

        self.display = ctk.CTkEntry(
            self.display_frame,
            font=("Arial", 32, "bold"),
            justify="right",
            height=80,
            fg_color="transparent",
            border_width=0,
            text_color="black"
        )
        self.display.pack(padx=10, pady=5, fill="x")

        # --- Сітка кнопок ---
        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons_frame.pack(padx=10, pady=10, fill="both", expand=True)

        for i in range(4):
            self.buttons_frame.grid_columnconfigure(i, weight=1, pad=5)
        for i in range(5):
            self.buttons_frame.grid_rowconfigure(i, weight=1, pad=5)

        # Розкладка кнопок
        button_spec = [
            ('C', 0, 0, 1), ('**', 0, 1, 1), ('%', 0, 2, 1), ('/', 0, 3, 1),
            ('7', 1, 0, 1), ('8', 1, 1, 1), ('9', 1, 2, 1), ('*', 1, 3, 1),
            ('4', 2, 0, 1), ('5', 2, 1, 1), ('6', 2, 2, 1), ('-', 2, 3, 1),
            ('1', 3, 0, 1), ('2', 3, 1, 1), ('3', 3, 2, 1), ('+', 3, 3, 1),
            ('0', 4, 0, 2), ('.', 4, 2, 1), ('=', 4, 3, 1)
        ]

        color_num = "#F8BBD0"   # Світло-рожеві кнопки для цифр
        color_op = "#F48FB1"    # Насиченіші рожеві для знаків
        text_color_main = "#880E4F" # Темно-бордовий текст

        for btn_text, row, col, colspan in button_spec:
            bg_color = color_op if btn_text in ['C', '**', '%', '/', '*', '-', '+', '='] else color_num

            btn = ctk.CTkButton(
                self.buttons_frame,
                text=btn_text,
                font=("Arial", 20, "bold"),
                fg_color=bg_color,
                text_color=text_color_main,
                height=60,
                corner_radius=15,
                hover_color="#F06292" if bg_color == color_op else "#F48FB1",
                command=lambda t=btn_text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky="nsew")

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.update_display()
        elif char == '=':
            self.calculate()
        else:
            self.expression += str(char)
            self.update_display()

    def update_display(self):
        self.display.delete(0, 'end')
        self.display.insert(0, self.expression)

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.display.delete(0, 'end')
            self.display.insert(0, result)
            self.expression = result
        except ZeroDivisionError:
            self.display.delete(0, 'end')
            self.display.insert(0, "Помилка: на нуль ділити не можна!")
            self.expression = ""
        except Exception:
            self.display.delete(0, 'end')
            self.display.insert(0, "Помилка")
            self.expression = ""

if __name__ == "__main__":
    app = PinkCalculator()
    app.mainloop()