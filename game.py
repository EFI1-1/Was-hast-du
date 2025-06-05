import customtkinter
import random
from PIL import Image

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

class MainMenu(customtkinter.CTkFrame):
    def __init__(self, master, start_callback):
        super().__init__(master)
        self.grid(row=0, column=0, sticky="nsew")
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        title = customtkinter.CTkLabel(self, text="Schere Stein Papier", font=("Arial", 32, "bold"))
        title.pack(pady=(80, 40))

        start_btn = customtkinter.CTkButton(self, text="Spiel starten", font=("Arial", 20), width=200, height=60, command=start_callback)
        start_btn.pack(pady=20)

        quit_btn = customtkinter.CTkButton(self, text="Beenden", font=("Arial", 16), width=200, height=40, command=master.destroy)
        quit_btn.pack(pady=10)

class Game(customtkinter.CTkFrame):
    def __init__(self, master, back_callback):
        super().__init__(master)
        # Game-Frame über das ganze Fenster strecken
        self.grid(row=0, column=0, sticky="nsew")
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        self.back_callback = back_callback

        self.center_frame = customtkinter.CTkFrame(self)
        self.center_frame.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.center_frame.grid_rowconfigure((0,1,2,3,4), weight=1)
        self.center_frame.grid_columnconfigure((0,1,2), weight=1)
        self.center_frame.configure(fg_color="#dbdbdb")

        self.label = customtkinter.CTkLabel(self.center_frame, text="Schere Stein Papier", font=("Arial", 28, "bold"))
        self.label.grid(row=0, column=0, columnspan=3, pady=(10, 20), sticky="n")

        # Spielerwahl-Bild
        self.player_label = customtkinter.CTkLabel(self.center_frame, text="")
        self.player_label.grid(row=2, column=0, pady=10, sticky="n")

        # Info-Label (Mitte)
        self.info_label = customtkinter.CTkLabel(self.center_frame, text="", font=("Arial", 16))
        self.info_label.grid(row=2, column=1, pady=10, sticky="n")

        # KI-Wahl-Bild
        self.ai_label = customtkinter.CTkLabel(self.center_frame, text="")
        self.ai_label.grid(row=2, column=2, pady=10, sticky="n")

        self.img_scissors = customtkinter.CTkImage(light_image=Image.open("images/Schere.png"), size=(150, 170))
        self.img_rock = customtkinter.CTkImage(light_image=Image.open("images/Stein.png"), size=(150, 170))
        self.img_paper = customtkinter.CTkImage(light_image=Image.open("images/Papier.png"), size=(150, 170))

        self.scissorsBtn = customtkinter.CTkButton(
            self.center_frame, text="", image=self.img_scissors, width=150, height=150, font=("Arial", 16), fg_color="transparent", hover_color="white",
            command=lambda: self.on_button_click("Schere")
        )
        self.rockBtn = customtkinter.CTkButton(
            self.center_frame, text="", image=self.img_rock, width=150, height=150, font=("Arial", 16), fg_color="transparent", hover_color="white",
            command=lambda: self.on_button_click("Stein")
        )
        self.paperBtn = customtkinter.CTkButton(
            self.center_frame, text="", image=self.img_paper, width=150, height=150, font=("Arial", 16), fg_color="transparent", hover_color="white",
            command=lambda: self.on_button_click("Papier")
        )

        self.scissorsBtn.grid(row=3, column=0, padx=10, pady=20)
        self.rockBtn.grid(row=3, column=1, padx=10, pady=20)
        self.paperBtn.grid(row=3, column=2, padx=10, pady=20)

        self.backBtn = customtkinter.CTkButton(self.center_frame, text="Zurück zum Hauptmenü", command=self.back_callback)
        self.backBtn.grid(row=4, column=0, columnspan=3, pady=(10, 20))

        self.default_fg_color = "#dbdbdb"

        # Best-of-3 Zähler
        self.player_score = 0
        self.ai_score = 0
        self.rounds = 0

        self.score_label = customtkinter.CTkLabel(self.center_frame, text="Spieler: 0  |  KI: 0", font=("Arial", 18, "bold"))
        self.score_label.grid(row=1, column=0, columnspan=3, pady=(0, 10))

    def on_button_click(self, choice):
        if self.player_score == 3 or self.ai_score == 3:
            return  # Keine weiteren Züge nach Spielende
        self.show_player_choice(choice)
        self.info_label.configure(text="...")
        self.after(500, lambda: self.ai_choice(choice))

    def show_player_choice(self, choice):
        if choice == "Schere":
            img = self.img_scissors
        elif choice == "Stein":
            img = self.img_rock
        else:
            img = self.img_paper
        self.player_label.configure(image=img, text="")

    def ai_choice(self, choice):
        options = ["Schere", "Stein", "Papier"]
        ai_choice = random.choice(options)
        if ai_choice == "Schere":
            ai_img = self.img_scissors
        elif ai_choice == "Stein":
            ai_img = self.img_rock
        else:
            ai_img = self.img_paper

        self.ai_label.configure(image=ai_img, text="")

        # Ergebnis bestimmen
        if (choice == "Schere" and ai_choice == "Papier") or \
           (choice == "Stein" and ai_choice == "Schere") or \
           (choice == "Papier" and ai_choice == "Stein"):
            self.player_score += 1
            result = "win"
        elif choice == ai_choice:
            result = "draw"
        else:
            self.ai_score += 1
            result = "lose"

        self.rounds += 1
        self.score_label.configure(text=f"Spieler: {self.player_score}  |  KI: {self.ai_score}")

        self.show_result(result)

        # Wer zuerst 3 Punkte hat, gewinnt sofort
        if self.player_score == 3 or self.ai_score == 3:
            self.after(1800, self.show_final_result)

    def show_final_result(self):
        if self.player_score > self.ai_score:
            msg = "Du hast das Best-of-3 gewonnen! 🎉"
        elif self.player_score < self.ai_score:
            msg = "Die KI hat das Best-of-3 gewonnen! 😢"
        else:
            msg = "Unentschieden im Best-of-3!"
        self.info_label.configure(text=msg)
        self.after(2500, self.back_callback)

    def show_result(self, result):
        # Ziel-Farbe bestimmen
        target_color = {"win": "#aaffaa", "draw": "#ffffaa", "lose": "#ffaaaa"}[result]
        text = {"win": "Sieg!", "draw": "Unentschieden!", "lose": "Verloren!"}[result]
        self.info_label.configure(text=text)
        self.animate_bg(self.center_frame.cget("fg_color"), target_color, steps=20, delay=20)
        self.after(500, lambda: self.animate_bg(self.center_frame.cget("fg_color"), self.default_fg_color, steps=20, delay=20))
        self.after(1200, lambda: self.info_label.configure(text=""))

    def animate_bg(self, start, end, steps=10, delay=20):
        # Hilfsfunktion: hex -> rgb
        def hex2rgb(hexcolor):
            hexcolor = hexcolor.lstrip("#")
            return tuple(int(hexcolor[i:i+2], 16) for i in (0, 2, 4))
        # Hilfsfunktion: rgb -> hex
        def rgb2hex(rgb):
            return "#%02x%02x%02x" % rgb

        start_rgb = hex2rgb(start)
        end_rgb = hex2rgb(end)
        diff = [end_rgb[i] - start_rgb[i] for i in range(3)]

        def step(i):
            if i > steps:
                self.center_frame.configure(fg_color=end)
                return
            new_rgb = tuple(int(start_rgb[j] + diff[j] * i / steps) for j in range(3))
            self.center_frame.configure(fg_color=rgb2hex(new_rgb))
            self.after(delay, lambda: step(i+1))

        step(0)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Schere Stein Papier")
        self.geometry("800x600")
        self.resizable(True, True)
        self.show_main_menu()

    def show_main_menu(self):
        self.clear_widgets()
        self.menu = MainMenu(self, self.start_game)

    def start_game(self):
        self.clear_widgets()
        self.game = Game(self, self.show_main_menu)

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

        #Database.db_insert(choice, ai_choice, self.label2._text)

if __name__ == "__main__":
    app = App()
    app.mainloop()