import tkinter as tk
from tkinter import simpledialog as sd
import ErrorDialog as erd


class EntryDialog(sd.Dialog):

    def __init__(self, master, character_sheet, title, text):
        self.__character_sheet = character_sheet
        self.__title = title
        self.__text = text
        self.__frm_answer = None
        self.__lbl_text = None
        self.__sv_points = None
        self.__ent_points = None
        self.__btn_assign = None
        self.__dlg_error = None
        self.__master = master
        super().__init__(self.__master)

    def body(self, master):
        self.title(self.__title)
        self.geometry("500x125")
        self.iconbitmap("symboltc1.ico")
        self.update_idletasks()
        self.after_idle(lambda: self.minsize(500, 125))
        self.after_idle(lambda: self.maxsize(500, 125))
        self.configure_answer_frame(master)

    def buttonbox(self):
        pass

    def configure_answer_frame(self, master):
        self.__frm_answer = tk.Frame(master)
        self.__frm_answer.grid(row=0, column=0)
        self.bind("<Return>", lambda event: self.handle_button())
        self.bind("<Escape>", lambda event: self.handle_key())
        self.configure_text()
        self.configure_points()
        self.configure_button()

    def configure_text(self):
        self.__lbl_text = tk.Label(self.__frm_answer, text="Liczba punktów", font=("book antiqua", 20, "bold"))
        self.__lbl_text.grid(row=0, column=0, sticky="w")

    def configure_points(self):
        self.__sv_points = tk.StringVar(self.__frm_answer)
        self.__ent_points = tk.Entry(self.__frm_answer, font=("book antiqua", 20), width=15,
                                     textvariable=self.__sv_points)
        self.__ent_points.grid(row=0, column=1, padx=5, sticky="e")

    def configure_button(self):
        self.__btn_assign = tk.Button(self.__frm_answer, text=self.__text, font=("book antiqua", 15, "italic"),
                                      command=self.handle_button)
        self.__btn_assign.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    def handle_key(self):
        self.destroy()

    def handle_button(self):
        if self.__sv_points.get().isdigit():
            if self.__title == "Obrażenia":
                if self.__text == "Przyjmij":
                    self.__character_sheet.lose_health(int(self.__sv_points.get()))
                else:
                    self.__character_sheet.heal_health(int(self.__sv_points.get()))
                self.__master.update_health()
            elif self.__title == "Energia":
                if self.__text == "Zużyj":
                    self.__character_sheet.spend_energy(int(self.__sv_points.get()))
                else:
                    self.__character_sheet.regain_energy(int(self.__sv_points.get()))
                self.__master.update_energy()
            else:
                self.__character_sheet.set_exp_points(self.__character_sheet.exp_points + int(self.__sv_points.get()))
                self.__master.update_exp()
            self.destroy()
        else:
            self.__dlg_error = erd.ErrorDialog(self, "Podana wartość nie jest liczbą całkowitą!")
            self.__ent_points.delete(0, 'end')
