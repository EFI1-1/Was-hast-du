import customtkinter
import random
import time
from PIL import Image
customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("light")

class Game(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Schnick Schnack Schnuck")
        self.geometry("800x500")
        self.resizable(False, False)

        # Grid configuration
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        # Rahmen für Content
        self.main_frame = customtkinter.CTkFrame(self)
        self.main_frame.grid(row=1, column=1, sticky="nsew", padx=40, pady=40)
        self.main_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.main_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.label = customtkinter.CTkLabel(self.main_frame, text="Schnick Schnack Schnuck", font=("Arial", 28, "bold"))
        self.label.grid(row=0, column=0, columnspan=3, pady=(10, 20), sticky="n")

        self.label3 = customtkinter.CTkLabel(self.main_frame, text="", font=("Arial", 16))
        self.label3.grid(row=2, column=0, columnspan=3, pady=10, sticky="n")

        self.img_scissors = customtkinter.CTkImage(light_image=Image.open("images/scissors.png"), size=(32, 32))
        self.img_rock = customtkinter.CTkImage(light_image=Image.open("images/hand.png"), size=(32, 32))
        self.img_paper = customtkinter.CTkImage(light_image=Image.open("images/hand-paper.png"), size=(32, 32))

        self.scissorsBtn = customtkinter.CTkButton(
            self.main_frame, text="", image=self.img_scissors, width=100, height=100, font=("Arial", 16),
            command=lambda: self.on_button_click("Schere")
        )
        self.rockBtn = customtkinter.CTkButton(
            self.main_frame, text="", image=self.img_rock, width=100, height=100, font=("Arial", 16),
            command=lambda: self.on_button_click("Stein")
        )
        self.paperBtn = customtkinter.CTkButton(
            self.main_frame, text="", image=self.img_paper, width=100, height=100, font=("Arial", 16),
            command=lambda: self.on_button_click("Papier")
        )

        self.scissorsBtn.grid(row=3, column=0, padx=10, pady=20)
        self.rockBtn.grid(row=3, column=1, padx=10, pady=20)
        self.paperBtn.grid(row=3, column=2, padx=10, pady=20)

    def on_button_click(self, choice):
        self.show_choice(choice)
        self.after(500, lambda: self.ai_choice(choice))

    def show_choice(self, choice):
        if choice == "Schere":
            img = self.img_scissors
        elif choice == "Stein":
            img = self.img_rock
        else:
            img = self.img_paper
        self.label3.configure(text="", image=img)

    def ai_choice(self, choice):
        options = ["Schere", "Stein", "Papier"]
        ai_choice = random.choice(options)
        if ai_choice == "Schere":
            ai_img = self.img_scissors
        elif ai_choice == "Stein":
            ai_img = self.img_rock
        else:
            ai_img = self.img_paper

        if hasattr(self, "ai_label"):
            self.ai_label.destroy()
        self.ai_label = customtkinter.CTkLabel(self.main_frame, text="", image=ai_img)
        self.ai_label.grid(row=2, column=2, pady=10, sticky="n")

        self.label3.grid(row=2, column=0, pady=10, sticky="n")
        self.label3.configure(image=self.label3.cget("image"))

        if (choice == "Schere" and ai_choice == "Papier") or \
           (choice == "Stein" and ai_choice == "Schere") or \
           (choice == "Papier" and ai_choice == "Stein"):
            self.show_result("win")
        elif choice == ai_choice:
            self.show_result("draw")
        else:
            self.show_result("lose")

    def show_result(self, result):
        color = {"win": "#aaffaa", "draw": "#ffffaa", "lose": "#ffaaaa"}[result]
        self.main_frame.configure(fg_color=color)
        self.after(800, lambda: self.main_frame.configure(fg_color="#ffffff"))
        if hasattr(self, "result_label"):
            self.result_label.destroy()
        text = {"win": "🎉 Sieg!", "draw": "🤝 Unentschieden!", "lose": "😢 Verloren!"}[result]
        self.result_label = customtkinter.CTkLabel(self.main_frame, text=text, font=("Arial", 22, "bold"))
        self.result_label.grid(row=1, column=0, columnspan=3, pady=(10, 20), sticky="n")
        self.after(1200, self.result_label.destroy)

if __name__ == "__main__":
    app = Game()
    app.mainloop()