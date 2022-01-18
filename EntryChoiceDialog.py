import tkinter as tk
from tkinter import simpledialog as sd
from tkinter import ttk as ttk
import ErrorDialog as erd


class EntryChoiceDialog(sd.Dialog):

    def __init__(self, master, character_sheet):
        self.__character_sheet = character_sheet
        self.__frm_answer = None
        self.__lbl_text = None
        self.__lbl_a = None
        self.__lbl_s = None
        self.__iv_choice = None
        self.__rdb_a_choice = None
        self.__rdb_s_choice = None
        self.__sv_points = None
        self.__ent_points = None
        self.__btn_assign = None
        self.__dlg_error = None
        self.__master = master
        super().__init__(self.__master)

    def body(self, master):
        self.title("Punkty Doświadczenia")
        self.geometry("500x150")
        self.iconbitmap("symboltc1.ico")
        self.update_idletasks()
        self.after_idle(lambda: self.minsize(500, 150))
        self.after_idle(lambda: self.maxsize(500, 150))
        self.configure_answer_frame(master)

    def buttonbox(self):
        pass

    def configure_answer_frame(self, master):
        self.__frm_answer = tk.Frame(master)
        self.__frm_answer.grid(row=0, column=0)
        self.bind("<Return>", lambda event: self.handle_button())
        self.bind("<Escape>", lambda event: self.handle_key())
        self.configure_radio_buttons()
        self.configure_text()
        self.configure_points()
        self.configure_button()

    def configure_radio_buttons(self):
        self.__iv_choice = tk.IntVar(self.__frm_answer)
        self.__rdb_a_choice = ttk.Radiobutton(self.__frm_answer, text="", value=0, var=self.__iv_choice)
        self.__lbl_a = tk.Label(self.__frm_answer, text="Atrybuty", font=("book antiqua", 20))
        self.__rdb_s_choice = ttk.Radiobutton(self.__frm_answer, text="", value=1, var=self.__iv_choice)
        self.__lbl_s = tk.Label(self.__frm_answer, text="Umiejętności", font=("book antiqua", 20))
        self.__rdb_a_choice.grid(row=0, column=0, sticky="w")
        self.__lbl_a.grid(row=0, column=1, sticky="w")
        self.__rdb_s_choice.grid(row=0, column=2, sticky="w")
        self.__lbl_s.grid(row=0, column=3, sticky="w")

    def configure_text(self):
        self.__lbl_text = tk.Label(self.__frm_answer, text="Liczba punktów", font=("book antiqua", 20, "bold"))
        self.__lbl_text.grid(row=1, column=0, columnspan=2, sticky="w")

    def configure_points(self):
        self.__sv_points = tk.StringVar(self.__frm_answer)
        self.__ent_points = tk.Entry(self.__frm_answer, font=("book antiqua", 20), width=15,
                                     textvariable=self.__sv_points)
        self.__ent_points.grid(row=1, column=2, columnspan=2, padx=5, sticky="e")

    def configure_button(self):
        self.__btn_assign = tk.Button(self.__frm_answer, text="Zużyj", font=("book antiqua", 15, "italic"),
                                      command=self.handle_button)
        self.__btn_assign.grid(row=2, column=0, columnspan=4, padx=5, pady=5, sticky="we")

    def handle_key(self):
        self.destroy()

    def handle_button(self):
        if self.__sv_points.get().isdigit():
            if self.__iv_choice.get() == 0:
                self.__character_sheet.spend_exp_on_attributes(int(self.__sv_points.get()))
                self.__master.update_a_points()
            else:
                self.__character_sheet.spend_exp_on_skills(int(self.__sv_points.get()))
                self.__master.update_s_points()
            self.__master.update_exp()
            self.destroy()
        else:
            self.__dlg_error = erd.ErrorDialog(self, "Podana wartość nie jest liczbą całkowitą!")
            self.__ent_points.delete(0, 'end')
