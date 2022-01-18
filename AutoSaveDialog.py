import tkinter as tk
from tkinter import simpledialog as sd


class AutoSaveDialog(sd.Dialog):

    def __init__(self, master):
        self.__frm_answer = None
        self.__lbl_text = None
        self.__btn_yes = None
        self.__btn_no = None
        self.__btn_cancel = None
        self.__master = master
        super().__init__(self.__master)

    def body(self, master):
        self.title("")
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
        self.bind("<Escape>", lambda event: self.handle_cancel_button())
        self.configure_text()
        self.configure_button()

    def configure_text(self):
        self.__lbl_text = tk.Label(self.__frm_answer, text="Czy chcesz zapisać przed wyjściem?", font=("book antiqua", 20, "bold"))
        self.__lbl_text.grid(row=0, column=0, columnspan=3, sticky="we")

    def configure_button(self):
        self.__btn_yes = tk.Button(self.__frm_answer, text="Tak", font=("book antiqua", 15, "italic"),
                                   command=self.handle_yes_button)
        self.__btn_no = tk.Button(self.__frm_answer, text="Nie", font=("book antiqua", 15, "italic"),
                                  command=self.handle_no_button)
        self.__btn_cancel = tk.Button(self.__frm_answer, text="Anuluj", font=("book antiqua", 15, "italic"),
                                      command=self.handle_cancel_button)
        self.__btn_yes.grid(row=1, column=0, pady=5, sticky="we")
        self.__btn_no.grid(row=1, column=1, pady=5, sticky="we")
        self.__btn_cancel.grid(row=1, column=2, pady=5, sticky="we")

    def handle_yes_button(self):
        self.destroy()
        self.__master.save()
        self.__master.close()

    def handle_no_button(self):
        self.destroy()
        self.__master.close()

    def handle_cancel_button(self):
        self.destroy()
