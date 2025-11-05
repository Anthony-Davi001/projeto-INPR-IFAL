import customtkinter as ctk

from .game import GameView

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("object")

        self.view=ctk.CTkTabview(master=self)
        self.view.pack(fill="both",expand=True)

        self.view.add("Game")
        game=GameView(master=self.view.tab("Game"))
        game.pack(fill="both", expand=True)
