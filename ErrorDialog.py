import tkinter as tk
from tkinter import simpledialog as sd


class ErrorDialog(sd.Dialog):

    def __init__(self, master, text):
        self.__text = text
        self.__frm_answer = None
        self.__lbl_text = None
        self.__sv_points = None
        self.__ent_points = None
        self.__btn_assign = None
        self.__master = master
        super().__init__(self.__master)

    def body(self, master):
        self.title("Błąd")
        self.geometry("600x80")
        self.iconbitmap("symboltc1.ico")
        self.update_idletasks()
        self.after_idle(lambda: self.minsize(600, 80))
        self.after_idle(lambda: self.maxsize(600, 80))
        self.configure_answer_frame(master)

    def buttonbox(self):
        pass

    def configure_answer_frame(self, master):
        self.__frm_answer = tk.Frame(master)
        self.__frm_answer.grid(row=0, column=0)
        self.bind("<Escape>", lambda event: self.handle_key())
        self.configure_text()

    def configure_text(self):
        self.__lbl_text = tk.Label(self.__frm_answer, text=self.__text, font=("book antiqua", 20))
        self.__lbl_text.grid(row=0, column=0, sticky="w")

    def handle_key(self):
        self.destroy()
