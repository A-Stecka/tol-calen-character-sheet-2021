import tkinter as tk
import tkinter.ttk as ttk
from tkinter import simpledialog as sd


class ChoiceDialog(sd.Dialog):

    def __init__(self, master, character_sheet):
        self.__character_sheet = character_sheet
        self.__frm_answer = None
        self.__lbl_attribute = None
        self.__lbl_skill = None
        self.__lbl_text = None
        self.__lbl_result = None
        self.__sv_attribute = None
        self.__sv_skill = None
        self.__cmb_attribute = None
        self.__cmb_skill = None
        self.__btn_roll = None
        super().__init__(master)

    def body(self, master):
        self.title("Rzut na...")
        self.geometry("500x235")
        self.iconbitmap("symboltc1.ico")
        self.update_idletasks()
        self.after_idle(lambda: self.minsize(500, 235))
        self.after_idle(lambda: self.maxsize(500, 235))
        self.configure_answer_frame(master)

    def buttonbox(self):
        pass

    def configure_answer_frame(self, master):
        self.__frm_answer = tk.Frame(master)
        self.__frm_answer.grid(row=0, column=0)
        self.bind("<Return>", lambda event: self.handle_button())
        self.bind("<Escape>", lambda event: self.handle_key())
        self.configure_attribute()
        self.configure_skill()
        self.configure_button()
        self.configure_text()
        self.configure_result()

    def configure_attribute(self):
        self.__lbl_attribute = tk.Label(self.__frm_answer, text="Atrybut", font=("book antiqua", 20, "bold"))
        self.__lbl_attribute.grid(row=0, column=0, sticky="w")

        self.__sv_attribute = tk.StringVar(self.__frm_answer)
        self.__cmb_attribute = ttk.Combobox(self.__frm_answer, font=("book antiqua", 20), state="readonly",
                                            textvariable=self.__sv_attribute)
        self.__cmb_attribute["values"] = ("Krzepa", "Wytrzymałość", "Zręczność", "Zmysły", "Intelekt", "Charakter")
        self.__cmb_attribute.current(0)
        self.__frm_answer.option_add('*TCombobox*Listbox.font', ("book antiqua", 20))
        self.__cmb_attribute.grid(row=0, column=1, padx=5, sticky="e")

    def configure_skill(self):
        self.__lbl_skill = tk.Label(self.__frm_answer, text="Umiejętność", font=("book antiqua", 20, "bold"))
        self.__lbl_skill.grid(row=1, column=0, sticky="w")

        self.__sv_skill = tk.StringVar(self.__frm_answer)
        self.__cmb_skill = ttk.Combobox(self.__frm_answer, font=("book antiqua", 20), state="readonly",
                                        textvariable=self.__sv_skill)
        self.__cmb_skill["values"] = ("Blef", "Empatia", "Jeździectwo", "Leczenie", "Obycie", "Perswazja",
                                      "Przetrwanie", "Rzemiosło", "Siła woli", "Skradanie", "Skupienie",
                                      "Spostrzegawczość", "Strzelectwo", "Walka", "Wykształcenie", "Wysportowanie",
                                      "Zastraszanie", "Złodziejstwo", "Żegluga")
        self.__cmb_skill.current(0)
        self.__frm_answer.option_add('*TCombobox*Listbox.font', ("book antiqua", 20))
        self.__cmb_skill.grid(row=1, column=1, padx=5, sticky="e")

    def configure_button(self):
        self.__btn_roll = tk.Button(self.__frm_answer, text="Rzuć!", font=("book antiqua", 15, "italic"),
                                    command=self.handle_button)
        self.__btn_roll.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    def configure_text(self):
        self.__lbl_text = tk.Label(self.__frm_answer, text="Liczba sukcesów", font=("book antiqua", 20, "bold"))
        self.__lbl_text.grid(row=3, column=0, columnspan=2, padx=5, sticky="we")

    def configure_result(self):
        self.__lbl_result = tk.Label(self.__frm_answer, text="", font=("book antiqua", 21, "bold"), fg="grey")
        self.__lbl_result.grid(row=4, column=0, columnspan=2, padx=5, sticky="we")

    def handle_key(self):
        self.destroy()

    def handle_button(self):
        self.__lbl_result["text"] = self.__character_sheet.roll_for(self.__sv_attribute.get().lower(),
                                                                    self.__sv_skill.get().lower())
