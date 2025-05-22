import customtkinter
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

class Game(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Schnick Schnack Schnuck")
        self.geometry("800x600")

        # Create a label
        self.label = customtkinter.CTkLabel(self, text="Schnick Schnack Schnuck", font=("Arial", 24))
        self.label.pack(pady=20)

        self.btn = customtkinter.CTkButton(self, text="Click Me", command=self.on_button_click)
        self.btn.pack(pady=20)

    def on_button_click(self):
        self.label.configure(text="Button Clicked!")


if __name__ == "__main__":
    app = Game()
    app.mainloop()