import tkinter as tk
from tkinter import simpledialog as sd


class ResultDialog(sd.Dialog):

    def __init__(self, master, title, text, result):
        self.__title = title
        self.__text = text
        self.__result = result
        self.__frm_answer = None
        self.__lbl_text = None
        self.__lbl_result = None
        super().__init__(master)

    def body(self, master):
        self.title(self.__title)
        self.geometry("500x100")
        self.iconbitmap("symboltc1.ico")
        self.update_idletasks()
        self.after_idle(lambda: self.minsize(500, 100))
        self.after_idle(lambda: self.maxsize(500, 100))
        self.configure_answer_frame(master)

    def buttonbox(self):
        pass

    def configure_answer_frame(self, master):
        self.__frm_answer = tk.Frame(master)
        self.__frm_answer.grid(row=0, column=0)
        self.bind("<Return>", lambda event: self.handle_key())
        self.bind("<Escape>", lambda event: self.handle_key())
        self.configure_text()
        self.configure_result()

    def configure_text(self):
        self.__lbl_text = tk.Label(self.__frm_answer, text=self.__text, font=("book antiqua", 20, "bold"))
        self.__lbl_text.grid(row=0, column=0)

    def configure_result(self):
        self.__lbl_result = tk.Label(self.__frm_answer, text=self.__result, font=("book antiqua", 21, "bold"),
                                     fg="grey")
        self.__lbl_result.grid(row=1, column=0)

    def handle_key(self):
        self.destroy()
