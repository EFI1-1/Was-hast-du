import customtkinter
import random
from database import Database

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

Database.dbconnect()

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

        self.label2 = customtkinter.CTkLabel(self.main_frame, text="Wähle deine Option:", font=("Arial", 18))
        self.label2.grid(row=1, column=0, columnspan=3, pady=10, sticky="n")

        self.label3 = customtkinter.CTkLabel(self.main_frame, text="", font=("Arial", 16))
        self.label3.grid(row=2, column=0, columnspan=3, pady=10, sticky="n")

        self.scissorsBtn = customtkinter.CTkButton(self.main_frame, text="✂ Schere", width=120, height=40, font=("Arial", 16), command=lambda: self.on_button_click("Schere"))
        self.rockBtn = customtkinter.CTkButton(self.main_frame, text="🪨 Stein", width=120, height=40, font=("Arial", 16), command=lambda: self.on_button_click("Stein"))
        self.paperBtn = customtkinter.CTkButton(self.main_frame, text="📄 Papier", width=120, height=40, font=("Arial", 16), command=lambda: self.on_button_click("Papier"))
        self.scissorsBtn.grid(row=3, column=0, padx=10, pady=20)
        self.rockBtn.grid(row=3, column=1, padx=10, pady=20)
        self.paperBtn.grid(row=3, column=2, padx=10, pady=20)

    def on_button_click(self, choice):
        self.label2.configure(text=f"Du hast gewählt: {choice}")
        self.ai_choice(choice)

    def ai_choice(self, choice):
        options = ["Schere", "Stein", "Papier"]
        ai_choice = random.choice(options)
        self.label3.configure(text=f"Die KI hat gewählt: {ai_choice}")

        # Gewinner Bestimmen
        if (choice == "Schere" and ai_choice == "Papier") or \
           (choice == "Stein" and ai_choice == "Schere") or \
           (choice == "Papier" and ai_choice == "Stein"):
            self.label2.configure(text="Du hast gewonnen!")
        elif choice == ai_choice:
            self.label2.configure(text="Unentschieden!")
        else:
            self.label2.configure(text="Die KI hat gewonnen!")

if __name__ == "__main__":
    app = Game()
    app.mainloop()