import customtkinter as ctk



class GameView(ctk.CTkFrame):
    def __init__(self, master: ctk.CTkTabview):
        super().__init__(master=master, fg_color="green")

