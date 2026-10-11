import customtkinter as ctk
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")
class PinkCalculator(ctk.CTk):
    def __init__(self):
        super().__init__()
self.title("Pink Calculator")
self.geometry("340x520")
self.configure(fg_color="#F37FA5")
self.resizable(False, False)
self.expression= ""
self.display_frame=ctk.CTkFrame(self, fg_color="white", corner_radius=20, border_width=0)
self.display_frame.pakc(padx=15, pady(25, 15), fill="x")
self.displey=ctk.CTkEntry(
    self.display_frame,
    font=("Arial", 32, "bold"),
    justify="right",
    height=80,
    fg_color="transparent",
    border_width=0,
    text_color="black"
)
self.display.pack(padx=10, pady=5, fill="x")
self.buttons_frame=ctk.CTkFrame(self, fg_color="transparent")
set.buttons_frame.pack(padx=10, pady=10, fill="both", expand=True)
for i in range(4):
    self.buttons_frame.grid_columnconfigure(i, weight=1, pad=5)
for i in range(5):
    self.buttons_frame.grid_rowconfigure(i, weight=1, pad=5)
    button_spec=[
        ('C', 0, 0, 1), ('**', 0, 1, 1), ('%', 0, 2, 1), ('/', 0, 3, 1),
        ('7', 1, 0, 1), ('8',1, 1, 1), ('9',1, 2, 1),('*',1, 3, 1),
        ('4', 2, 0, 1), ('5', 2, 1, 1), ('6', 2, 2, 1), ('-', 2, 3, 1),
        ('1', 3, 0, 1), ('2', 3, 1, 1), ('3',3, 2, 1), ('+', 3, 3, 1),
        ('0',4, 0, 2), ('.', 4, 2, 1), ('=', 4, 3, 1)
    ]
    color_