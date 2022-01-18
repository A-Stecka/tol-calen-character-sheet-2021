import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as fd
import json
import ResultDialog as rd
import ChoiceDialog as cd
import EntryDialog as ed
import EntryChoiceDialog as ecd
import IfDialog as ifd
import CharacterSheet as cs
import ErrorDialog as erd
import AutoSaveDialog as asd


class Application(tk.Frame):

    def __init__(self, master=None):
        self.__character_sheet = cs.CharacterSheet()
        self.__master = master
        self.__filename = ""
        # okno startowe
        self.__pht_logo = None
        self.__can_logo = None
        self.__frm_buttons_menu = None
        self.__lbl_title_menu = None
        self.__btn_create = None
        self.__btn_open = None
        self.__dlg_error = None
        # pasek menu
        self.__menu_options = None
        self.__menu_options_items = None
        self.__menu_reset_items = None
        self.__dlg_reset = None
        self.__dlg_new_campaign = None
        self.__dlg_autosave = None
        # sekcja tytulowa
        self.__frm_title = None
        self.__lbl_title = None
        # sekcja koncept
        self.__frm_concept = None
        self.__frm_name = None
        self.__frm_race = None
        self.__frm_player = None
        self.__frm_class = None
        self.__lbl_name = None
        self.__lbl_race = None
        self.__lbl_player = None
        self.__lbl_class = None
        self.__sv_name = None
        self.__sv_race = None
        self.__sv_player = None
        self.__sv_class = None
        self.__ent_name = None
        self.__ent_race = None
        self.__ent_player = None
        self.__ent_class = None
        self.__cmb_class = None
        # sekcja atrybuty
        self.__frm_attributes = None
        self.__frm_a_title = None
        self.__frm_a1 = None
        self.__frm_a2 = None
        self.__frm_a3 = None
        self.__frm_a4 = None
        self.__frm_a5 = None
        self.__frm_a6 = None
        self.__lbl_a_title = None
        self.__lbl_a_points = None
        self.__lbl_a1 = None
        self.__lbl_a1_points = None
        self.__lbl_a2 = None
        self.__lbl_a2_points = None
        self.__lbl_a3 = None
        self.__lbl_a3_points = None
        self.__lbl_a4 = None
        self.__lbl_a4_points = None
        self.__lbl_a5 = None
        self.__lbl_a5_points = None
        self.__lbl_a6 = None
        self.__lbl_a6_points = None
        self.__btn_a1_minus = None
        self.__btn_a1_plus = None
        self.__btn_a2_minus = None
        self.__btn_a2_plus = None
        self.__btn_a3_minus = None
        self.__btn_a3_plus = None
        self.__btn_a4_minus = None
        self.__btn_a4_plus = None
        self.__btn_a5_minus = None
        self.__btn_a5_plus = None
        self.__btn_a6_minus = None
        self.__btn_a6_plus = None
        self.__iv_a_points = None
        # sekcja umiejetnosci
        self.__frm_skills = None
        self.__frm_s_title = None
        self.__frm_s1 = None
        self.__frm_s2 = None
        self.__frm_s3 = None
        self.__frm_s4 = None
        self.__frm_s4 = None
        self.__frm_s5 = None
        self.__frm_s6 = None
        self.__frm_s7 = None
        self.__frm_s8 = None
        self.__frm_s9 = None
        self.__frm_s10 = None
        self.__frm_s11 = None
        self.__frm_s12 = None
        self.__frm_s13 = None
        self.__frm_s14 = None
        self.__frm_s15 = None
        self.__frm_s16 = None
        self.__frm_s17 = None
        self.__frm_s18 = None
        self.__frm_s19 = None
        self.__lbl_s_title = None
        self.__lbl_s_points = None
        self.__lbl_s1 = None
        self.__lbl_s1_points = None
        self.__lbl_s2 = None
        self.__lbl_s2_points = None
        self.__lbl_s3 = None
        self.__lbl_s3_points = None
        self.__lbl_s4 = None
        self.__lbl_s4_points = None
        self.__lbl_s5 = None
        self.__lbl_s5_points = None
        self.__lbl_s6 = None
        self.__lbl_s6_points = None
        self.__lbl_s7 = None
        self.__lbl_s7_points = None
        self.__lbl_s8 = None
        self.__lbl_s8_points = None
        self.__lbl_s9 = None
        self.__lbl_s9_points = None
        self.__lbl_s10 = None
        self.__lbl_s10_points = None
        self.__lbl_s11 = None
        self.__lbl_s11_points = None
        self.__lbl_s12 = None
        self.__lbl_s12_points = None
        self.__lbl_s13 = None
        self.__lbl_s13_points = None
        self.__lbl_s14 = None
        self.__lbl_s14_points = None
        self.__lbl_s15 = None
        self.__lbl_s15_points = None
        self.__lbl_s16 = None
        self.__lbl_s16_points = None
        self.__lbl_s17 = None
        self.__lbl_s17_points = None
        self.__lbl_s18 = None
        self.__lbl_s18_points = None
        self.__lbl_s19 = None
        self.__lbl_s19_points = None
        self.__btn_s1_minus = None
        self.__btn_s1_plus = None
        self.__btn_s2_minus = None
        self.__btn_s2_plus = None
        self.__btn_s3_minus = None
        self.__btn_s3_plus = None
        self.__btn_s4_minus = None
        self.__btn_s4_plus = None
        self.__btn_s5_minus = None
        self.__btn_s5_plus = None
        self.__btn_s6_minus = None
        self.__btn_s6_plus = None
        self.__btn_s7_minus = None
        self.__btn_s7_plus = None
        self.__btn_s8_minus = None
        self.__btn_s8_plus = None
        self.__btn_s9_minus = None
        self.__btn_s9_plus = None
        self.__btn_s10_minus = None
        self.__btn_s10_plus = None
        self.__btn_s11_minus = None
        self.__btn_s11_plus = None
        self.__btn_s12_minus = None
        self.__btn_s12_plus = None
        self.__btn_s13_minus = None
        self.__btn_s13_plus = None
        self.__btn_s14_minus = None
        self.__btn_s14_plus = None
        self.__btn_s15_minus = None
        self.__btn_s15_plus = None
        self.__btn_s16_minus = None
        self.__btn_s16_plus = None
        self.__btn_s17_minus = None
        self.__btn_s17_plus = None
        self.__btn_s18_minus = None
        self.__btn_s18_plus = None
        self.__btn_s19_minus = None
        self.__btn_s19_plus = None
        # sekcja przyciski
        self.__frm_buttons = None
        self.__frm_buttons_centered = None
        self.__btn_roll_for = None
        self.__btn_roll_against_death = None
        self.__btn_roll_damage = None
        self.__btn_roll_initiative = None
        self.__btn_lose_health = None
        self.__btn_heal_health = None
        self.__btn_spend_energy = None
        self.__btn_regain_energy = None
        self.__btn_gain_exp = None
        self.__btn_spend_exp = None
        self.__btn_burn = None
        self.__dlg_roll_for = None
        self.__dlg_against_death = None
        self.__dlg_damage = None
        self.__dlg_initiative = None
        self.__dlg_lose_health = None
        self.__dlg_heal_health = None
        self.__dlg_spend_energy = None
        self.__dlg_regain_energy = None
        self.__dlg_gain_exp = None
        self.__dlg_spend_exp = None
        # sekcja ekwipunek
        self.__frm_equipment = None
        self.__frm_e_title = None
        self.__frm_e1 = None
        self.__frm_e2 = None
        self.__frm_e3 = None
        self.__lbl_e_title = None
        self.__lbl_e1 = None
        self.__lbl_e1_points = None
        self.__lbl_e2 = None
        self.__lbl_e2_points = None
        self.__lbl_e3 = None
        self.__lbl_e3_points = None
        self.__lbl_mage = None
        self.__lbl_health = None
        self.__lbl_health_points = None
        self.__lbl_energy = None
        self.__lbl_energy_points = None
        self.__lbl_initiative = None
        self.__lbl_initiative_points = None
        self.__btn_e1_minus = None
        self.__btn_e1_plus = None
        self.__btn_e2_minus = None
        self.__btn_e2_plus = None
        self.__btn_e3_minus = None
        self.__btn_e3_plus = None
        # sekcja statystyki
        self.__frm_stats = None
        self.__frm_mage = None
        self.__frm_health = None
        self.__frm_energy = None
        self.__frm_initiative = None
        self.__bv_mage = None
        self.__chb_mage = None
        # sekcja punkty
        self.__frm_points = None
        self.__frm_luck = None
        self.__frm_exp = None
        self.__lbl_luck_title = None
        self.__lbl_luck_points = None
        self.__lbl_exp_title = None
        self.__lbl_exp_points = None
        super().__init__(self.__master)
        self.configure_buttons_menu()
        self.configure_logo_menu()
        self.configure_self_menu()
        self.configure_master_menu()

    def configure_master_menu(self):
        self.__master.title("Tol Calen")
        self.__master.geometry("800x600+100+0")
        self.__master.iconbitmap("symboltc1.ico")
        self.__master.config(bg="#dddddd")
        self.__master.columnconfigure(0, weight=1)
        self.__master.rowconfigure(0, weight=1)
        self.__master.update_idletasks()
        self.__master.after_idle(lambda: self.master.minsize(800, 0))

    def configure_self_menu(self):
        self.config(bg="#ffffff")
        self.grid(column=0, row=0)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def configure_logo_menu(self):
        self.__pht_logo = tk.PhotoImage(file="symboltc2.png")
        self.__can_logo = tk.Canvas(self, width=400, height=600, highlightthickness=0)
        self.__can_logo.grid(column=0, row=0)
        self.__can_logo.create_image((200, 300), image=self.__pht_logo, anchor="center")

    def configure_buttons_menu(self):
        self.__frm_buttons_menu = tk.Frame(self, bg="#ffffff", width=400, height=300)
        self.__frm_buttons_menu.pack_propagate(False)
        self.__frm_buttons_menu.grid(column=1, row=0)
        self.__lbl_title_menu = tk.Label(self.__frm_buttons_menu, bg="#ffffff", text="Tol Calen",
                                         font=("century schoolbook", 55, "bold"))
        self.__lbl_title_menu.pack()
        self.__btn_create = tk.Button(self.__frm_buttons_menu, bg="#ffffff", text="Utwórz nową kartę",
                                      font=("book antiqua", 15, "italic"), command=self.create_new_sheet)
        self.__btn_create.pack(fill="x", padx=5)
        self.__btn_open = tk.Button(self.__frm_buttons_menu, bg="#ffffff", text="Wybierz kartę",
                                    font=("book antiqua", 15, "italic"), command=self.create_sheet_from_file)
        self.__btn_open.pack(fill="x", padx=5)

    def create_new_sheet(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.configure_points_frame()
        self.configure_stats_frame()
        self.configure_equipment_frame()
        self.configure_buttons_frame()
        self.configure_skill_frame()
        self.configure_attribute_frame()
        self.configure_concept_frame()
        self.configure_title_frame()
        self.configure_self()
        self.configure_master()

    def create_sheet_from_file(self):
        self.create_new_sheet()
        self.open_sheet_from_file()

    def open_sheet_from_file(self):
        filename = fd.askopenfilename(filetypes=[('Text files', '.txt')])
        if not filename:
            return
        else:
            file = open(filename, 'r', encoding="UTF-8")
            line = file.read()
            file.close()
            try:
                json.loads(line.replace("\n", ""))
            except json.decoder.JSONDecodeError:
                self.__dlg_error = erd.ErrorDialog(self, "Brak karty postaci w pliku. Tworzę nową kartę.")
                self.__filename = ""
                self.__character_sheet.reset()
            else:
                if not self.__character_sheet.update_with_json(line.replace("\n", "")):
                    self.__dlg_error = erd.ErrorDialog(self, "Brak karty postaci w pliku. Tworzę nową kartę.")
                    self.__filename = ""
                    self.__character_sheet.reset()
                else:
                    self.__filename = filename
        self.update()

    def save(self):
        if not self.__filename:
            self.__filename = fd.asksaveasfilename(defaultextension='.txt', filetypes=[('Text files', '.txt')])
        if not self.__filename:
            return
        file = open(self.__filename, 'w', encoding="UTF-8")
        file.write(self.__character_sheet.to_json())
        file.close()

    def save_as(self):
        self.__filename = fd.asksaveasfilename(defaultextension='.txt', filetypes=[('Text files', '.txt')])
        if not self.__filename:
            return
        file = open(self.__filename, 'w', encoding="UTF-8")
        file.write(self.__character_sheet.to_json())
        file.close()

    def configure_master(self):
        self.__master.title("Tol Calen")
        self.__master.geometry("1550x1000")
        self.__master.iconbitmap("symboltc1.ico")
        self.__master.config(bg="#dddddd")
        self.__menu_options = tk.Menu(self.__master)
        self.__menu_options_items = tk.Menu(self.__menu_options, tearoff=0)
        self.__menu_options_items.add_command(label="Zapisz", command=self.save)
        self.__menu_options_items.add_command(label="Zapisz jako", command=self.save_as)
        self.__menu_options_items.add_command(label="Otwórz inną kartę", command=self.open_sheet_from_file)
        self.__menu_options.add_cascade(label="Opcje", menu=self.__menu_options_items)
        self.__menu_reset_items = tk.Menu(self.__menu_options, tearoff=0)
        self.__menu_reset_items.add_command(label="Czyść kartę", command=self.reset)
        self.__menu_reset_items.add_command(label="Nowa kampania", command=self.prep_for_new_campaign)
        self.__menu_options.add_cascade(label="Reset karty", menu=self.__menu_reset_items)
        self.__master.config(menu=self.__menu_options)
        self.__master.columnconfigure(0, weight=1)
        self.__master.rowconfigure(0, weight=1)
        self.__master.update_idletasks()
        self.__master.after_idle(lambda: self.master.minsize(1525, 0))
        self.__master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def configure_self(self):
        self.config(bg="#dddddd")
        self.grid(column=0, row=0)

    def configure_title_frame(self):
        self.__frm_title = tk.Frame(self)
        self.__frm_title.grid(row=0, column=2)
        self.__lbl_title = tk.Label(self.__frm_title, bg="#dddddd", text="Tol Calen",
                                    font=("century schoolbook", 55, "bold"))
        self.__lbl_title.pack()

    def configure_concept_frame(self):
        self.__frm_concept = tk.Frame(self, relief="ridge", borderwidth=2, width=1145, height=110)
        self.__frm_concept.grid_propagate(False)
        self.__frm_concept.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        for i in range(2):
            self.__frm_concept.rowconfigure(i, weight=1)
            self.__frm_concept.columnconfigure(i, weight=1)
        self.configure_name_frame()
        self.configure_race_frame()
        self.configure_player_frame()
        self.configure_class_frame()

    def configure_name_frame(self):
        self.__frm_name = tk.Frame(self.__frm_concept)
        self.__frm_name.grid(row=0, column=0, padx=10)
        self.__lbl_name = tk.Label(self.__frm_name, text="Imię:", font=("book antiqua", 20, "bold"))
        self.__sv_name = tk.StringVar(self.__frm_name, self.__character_sheet.get_concept_val("imię"))
        self.__sv_name.trace("w", lambda name, index, mode, sv=self.__sv_name: self.edit_name())
        self.__ent_name = tk.Entry(self.__frm_name, font=("book antiqua", 20), width=50, textvariable=self.__sv_name)
        self.__lbl_name.pack(side="left")
        self.__ent_name.pack(side="right", padx=5)

    def configure_race_frame(self):
        self.__frm_race = tk.Frame(self.__frm_concept)
        self.__frm_race.grid(row=1, column=0, padx=10)
        self.__lbl_race = tk.Label(self.__frm_race, text="Pochodzenie:", font=("book antiqua", 20, "bold"))
        self.__sv_race = tk.StringVar(self.__frm_race, self.__character_sheet.get_concept_val("pochodzenie"))
        self.__sv_race.trace("w", lambda name, index, mode, sv=self.__sv_race: self.edit_race())
        self.__ent_race = tk.Entry(self.__frm_race, font=("book antiqua", 20), width=45, textvariable=self.__sv_race)
        self.__lbl_race.pack(side="left")
        self.__ent_race.pack(side="right", padx=5)

    def configure_player_frame(self):
        self.__frm_player = tk.Frame(self.__frm_concept)
        self.__frm_player.grid(row=0, column=1, padx=10)
        self.__lbl_player = tk.Label(self.__frm_player, text="Gracz:", font=("book antiqua", 20, "bold"))
        self.__sv_player = tk.StringVar(self.__frm_player, self.__character_sheet.get_concept_val("gracz"))
        self.__sv_player.trace("w", lambda name, index, mode, sv=self.__sv_player: self.edit_player())
        self.__ent_player = tk.Entry(self.__frm_player, font=("book antiqua", 20), width=20,
                                     textvariable=self.__sv_player)
        self.__lbl_player.pack(side="left")
        self.__ent_player.pack(side="right", padx=5)

    def configure_class_frame(self):
        self.__frm_class = tk.Frame(self.__frm_concept)
        self.__frm_class.grid(row=1, column=1, padx=10)
        self.__lbl_class = tk.Label(self.__frm_class, text="Klasa:", font=("book antiqua", 20, "bold"))
        self.__sv_class = tk.StringVar(self.__frm_class)
        self.__sv_class.trace("w", lambda name, index, mode, sv=self.__sv_class: self.edit_class())
        self.__cmb_class = ttk.Combobox(self.__frm_class, font=("book antiqua", 20), state="readonly",
                                        textvariable=self.__sv_class)
        self.__cmb_class["values"] = ("Cwany", "Uczony", "Waleczny")
        if self.__character_sheet.get_concept_val("klasa") == "Uczony":
            self.__cmb_class.current(1)
        elif self.__character_sheet.get_concept_val("klasa") == "Waleczny":
            self.__cmb_class.current(2)
        else:
            self.__cmb_class.current(0)
        self.__frm_class.option_add('*TCombobox*Listbox.font', ("book antiqua", 20))
        self.__lbl_class.pack(side="left")
        self.__cmb_class.pack(side="right", padx=5)

    def configure_attribute_frame(self):
        self.__frm_attributes = tk.Frame(self, relief="ridge", borderwidth=2, width=435, height=600)
        self.__frm_attributes.grid_propagate(False)
        self.__frm_attributes.grid(row=1, column=0, padx=5, pady=5)
        self.configure_attribute_title()
        self.configure_a1()
        self.configure_a2()
        self.configure_a3()
        self.configure_a4()
        self.configure_a5()
        self.configure_a6()

    def configure_attribute_title(self):
        self.__frm_a_title = tk.Frame(self.__frm_attributes)
        self.__frm_a_title.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.__lbl_a_title = tk.Label(self.__frm_a_title, text="Atrybuty", font=("century schoolbook", 20, "bold"))
        self.__iv_a_points = tk.IntVar(self.__frm_a_title, value=self.__character_sheet.attribute_points)
        self.__iv_a_points.trace("w", lambda name, index, mode, sv=self.__iv_a_points: self.manage_checkbox_mage())
        self.__lbl_a_points = tk.Label(self.__frm_a_title, font=("century schoolbook", 20, "bold"), fg="grey",
                                       textvariable=self.__iv_a_points)
        self.__lbl_a_title.pack(side="left")
        self.__lbl_a_points.pack(side="left", padx=5)

    def configure_a1(self):
        self.__frm_a1 = tk.Frame(self.__frm_attributes)
        self.__frm_a1.grid(row=1, column=0, padx=10, pady=5, sticky="we")
        self.__btn_a1_minus = tk.Button(self.__frm_a1, text="–", font=("book antiqua", 25), width=2,
                                        command=self.dec_a1)
        self.__btn_a1_plus = tk.Button(self.__frm_a1, text="+", font=("book antiqua", 25), width=2,
                                       command=self.inc_a1)
        self.__lbl_a1 = tk.Label(self.__frm_a1, text="Krzepa", font=("book antiqua", 25))
        self.__lbl_a1_points = tk.Label(self.__frm_a1, text=self.__character_sheet.get_attribute_val('krzepa'),
                                        font=("book antiqua", 26, "bold"), fg="grey")
        self.__btn_a1_minus.pack(side="left")
        self.__btn_a1_plus.pack(side="left")
        self.__lbl_a1.pack(side="left", padx=15)
        self.__lbl_a1_points.pack(side="right", padx=5)

    def configure_a2(self):
        self.__frm_a2 = tk.Frame(self.__frm_attributes)
        self.__frm_a2.grid(row=2, column=0, padx=10, pady=5, sticky="we")
        self.__btn_a2_minus = tk.Button(self.__frm_a2, text="–", font=("book antiqua", 25), width=2,
                                        command=self.dec_a2)
        self.__btn_a2_plus = tk.Button(self.__frm_a2, text="+", font=("book antiqua", 25), width=2,
                                       command=self.inc_a2)
        self.__lbl_a2 = tk.Label(self.__frm_a2, text="Wytrzymałość", font=("book antiqua", 25))
        self.__lbl_a2_points = tk.Label(self.__frm_a2, text=self.__character_sheet.get_attribute_val('wytrzymałość'),
                                        font=("book antiqua", 26, "bold"), fg="grey")
        self.__btn_a2_minus.pack(side="left")
        self.__btn_a2_plus.pack(side="left")
        self.__lbl_a2.pack(side="left", padx=15)
        self.__lbl_a2_points.pack(side="right", padx=5)

    def configure_a3(self):
        self.__frm_a3 = tk.Frame(self.__frm_attributes)
        self.__frm_a3.grid(row=3, column=0, padx=10, pady=5, sticky="we")
        self.__btn_a3_minus = tk.Button(self.__frm_a3, text="–", font=("book antiqua", 25), width=2,
                                        command=self.dec_a3)
        self.__btn_a3_plus = tk.Button(self.__frm_a3, text="+", font=("book antiqua", 25), width=2,
                                       command=self.inc_a3)
        self.__lbl_a3 = tk.Label(self.__frm_a3, text="Zręczność", font=("book antiqua", 25))
        self.__lbl_a3_points = tk.Label(self.__frm_a3, text=self.__character_sheet.get_attribute_val('zręczność'),
                                        font=("book antiqua", 26, "bold"), fg="grey")
        self.__btn_a3_minus.pack(side="left")
        self.__btn_a3_plus.pack(side="left")
        self.__lbl_a3.pack(side="left", padx=15)
        self.__lbl_a3_points.pack(side="right", padx=5)

    def configure_a4(self):
        self.__frm_a4 = tk.Frame(self.__frm_attributes)
        self.__frm_a4.grid(row=4, column=0, padx=10, pady=5, sticky="we")
        self.__btn_a4_minus = tk.Button(self.__frm_a4, text="–", font=("book antiqua", 25), width=2,
                                        command=self.dec_a4)
        self.__btn_a4_plus = tk.Button(self.__frm_a4, text="+", font=("book antiqua", 25), width=2,
                                       command=self.inc_a4)
        self.__lbl_a4 = tk.Label(self.__frm_a4, text="Zmysły", font=("book antiqua", 25))
        self.__lbl_a4_points = tk.Label(self.__frm_a4, text=self.__character_sheet.get_attribute_val('zmysły'),
                                        font=("book antiqua", 26, "bold"), fg="grey")
        self.__btn_a4_minus.pack(side="left")
        self.__btn_a4_plus.pack(side="left")
        self.__lbl_a4.pack(side="left", padx=15)
        self.__lbl_a4_points.pack(side="right", padx=5)

    def configure_a5(self):
        self.__frm_a5 = tk.Frame(self.__frm_attributes)
        self.__frm_a5.grid(row=5, column=0, padx=10, pady=5, sticky="we")
        self.__btn_a5_minus = tk.Button(self.__frm_a5, text="–", font=("book antiqua", 25), width=2,
                                        command=self.dec_a5)
        self.__btn_a5_plus = tk.Button(self.__frm_a5, text="+", font=("book antiqua", 25), width=2,
                                       command=self.inc_a5)
        self.__lbl_a5 = tk.Label(self.__frm_a5, text="Intelekt", font=("book antiqua", 25))
        self.__lbl_a5_points = tk.Label(self.__frm_a5, text=self.__character_sheet.get_attribute_val('intelekt'),
                                        font=("book antiqua", 26, "bold"), fg="grey")
        self.__btn_a5_minus.pack(side="left")
        self.__btn_a5_plus.pack(side="left")
        self.__lbl_a5.pack(side="left", padx=15)
        self.__lbl_a5_points.pack(side="right", padx=5)

    def configure_a6(self):
        self.__frm_a6 = tk.Frame(self.__frm_attributes)
        self.__frm_a6.grid(row=6, column=0, padx=10, pady=5, sticky="we")
        self.__btn_a6_minus = tk.Button(self.__frm_a6, text="–", font=("book antiqua", 25), width=2,
                                        command=self.dec_a6)
        self.__btn_a6_plus = tk.Button(self.__frm_a6, text="+", font=("book antiqua", 25), width=2,
                                       command=self.inc_a6)
        self.__lbl_a6 = tk.Label(self.__frm_a6, text="Charakter", font=("book antiqua", 25))
        self.__lbl_a6_points = tk.Label(self.__frm_a6, text=self.__character_sheet.get_attribute_val('charakter'),
                                        font=("book antiqua", 26, "bold"), fg="grey")
        self.__btn_a6_minus.pack(side="left")
        self.__btn_a6_plus.pack(side="left")
        self.__lbl_a6.pack(side="left", padx=15)
        self.__lbl_a6_points.pack(side="right", padx=5)

    def configure_skill_frame(self):
        self.__frm_skills = tk.Frame(self, relief="ridge", borderwidth=2, width=695, height=600)
        self.__frm_skills.grid_propagate(False)
        self.__frm_skills.grid(row=1, column=1, padx=5, pady=5)
        self.configure_skill_title()
        self.configure_s1()
        self.configure_s2()
        self.configure_s3()
        self.configure_s4()
        self.configure_s5()
        self.configure_s6()
        self.configure_s7()
        self.configure_s8()
        self.configure_s9()
        self.configure_s10()
        self.configure_s11()
        self.configure_s12()
        self.configure_s13()
        self.configure_s14()
        self.configure_s15()
        self.configure_s16()
        self.configure_s17()
        self.configure_s18()
        self.configure_s19()

    def configure_skill_title(self):
        self.__frm_s_title = tk.Frame(self.__frm_skills)
        self.__frm_s_title.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="w")
        self.__lbl_s_title = tk.Label(self.__frm_s_title, text="Umiejętności", font=("century schoolbook", 20, "bold"))
        self.__lbl_s_points = tk.Label(self.__frm_s_title, text=self.__character_sheet.skill_points,
                                       font=("century schoolbook", 20, "bold"), fg="grey")
        self.__lbl_s_title.pack(side="left")
        self.__lbl_s_points.pack(side="left", padx=5)

    def configure_s1(self):
        self.__frm_s1 = tk.Frame(self.__frm_skills)
        self.__frm_s1.grid(row=1, column=0, padx=10, pady=5, sticky="we")
        self.__btn_s1_minus = tk.Button(self.__frm_s1, text="–", font=("book antiqua", 15), width=2,
                                        command=self.dec_s1)
        self.__btn_s1_plus = tk.Button(self.__frm_s1, text="+", font=("book antiqua", 15), width=2,
                                       command=self.inc_s1)
        self.__lbl_s1 = tk.Label(self.__frm_s1, text="Blef", font=("book antiqua", 15))
        self.__lbl_s1_points = tk.Label(self.__frm_s1, text=self.__character_sheet.get_skill_val('blef'),
                                        font=("book antiqua", 16, "bold"), fg="grey")
        self.__btn_s1_minus.pack(side="left")
        self.__btn_s1_plus.pack(side="left")
        self.__lbl_s1.pack(side="left", padx=15)
        self.__lbl_s1_points.pack(side="right", padx=5)

    def configure_s2(self):
        self.__frm_s2 = tk.Frame(self.__frm_skills)
        self.__frm_s2.grid(row=2, column=0, padx=10, pady=5, sticky="we")
        self.__btn_s2_minus = tk.Button(self.__frm_s2, text="–", font=("book antiqua", 15), width=2,
                                        command=self.dec_s2)
        self.__btn_s2_plus = tk.Button(self.__frm_s2, text="+", font=("book antiqua", 15), width=2,
                                       command=self.inc_s2)
        self.__lbl_s2 = tk.Label(self.__frm_s2, text="Empatia", font=("book antiqua", 15))
        self.__lbl_s2_points = tk.Label(self.__frm_s2, text=self.__character_sheet.get_skill_val('empatia'),
                                        font=("book antiqua", 16, "bold"), fg="grey")
        self.__btn_s2_minus.pack(side="left")
        self.__btn_s2_plus.pack(side="left")
        self.__lbl_s2.pack(side="left", padx=15)
        self.__lbl_s2_points.pack(side="right", padx=5)

    def configure_s3(self):
        self.__frm_s3 = tk.Frame(self.__frm_skills)
        self.__frm_s3.grid(row=3, column=0, padx=10, pady=5, sticky="we")
        self.__btn_s3_minus = tk.Button(self.__frm_s3, text="–", font=("book antiqua", 15), width=2,
                                        command=self.dec_s3)
        self.__btn_s3_plus = tk.Button(self.__frm_s3, text="+", font=("book antiqua", 15), width=2,
                                       command=self.inc_s3)
        self.__lbl_s3 = tk.Label(self.__frm_s3, text="Jeździectwo", font=("book antiqua", 15))
        self.__lbl_s3_points = tk.Label(self.__frm_s3, text=self.__character_sheet.get_skill_val('jeździectwo'),
                                        font=("book antiqua", 16, "bold"), fg="grey")
        self.__btn_s3_minus.pack(side="left")
        self.__btn_s3_plus.pack(side="left")
        self.__lbl_s3.pack(side="left", padx=15)
        self.__lbl_s3_points.pack(side="right", padx=5)

    def configure_s4(self):
        self.__frm_s4 = tk.Frame(self.__frm_skills)
        self.__frm_s4.grid(row=4, column=0, padx=10, pady=5, sticky="we")
        self.__btn_s4_minus = tk.Button(self.__frm_s4, text="–", font=("book antiqua", 15), width=2,
                                        command=self.dec_s4)
        self.__btn_s4_plus = tk.Button(self.__frm_s4, text="+", font=("book antiqua", 15), width=2,
                                       command=self.inc_s4)
        self.__lbl_s4 = tk.Label(self.__frm_s4, text="Leczenie", font=("book antiqua", 15))
        self.__lbl_s4_points = tk.Label(self.__frm_s4, text=self.__character_sheet.get_skill_val('leczenie'),
                                        font=("book antiqua", 16, "bold"), fg="grey")
        self.__btn_s4_minus.pack(side="left")
        self.__btn_s4_plus.pack(side="left")
        self.__lbl_s4.pack(side="left", padx=15)
        self.__lbl_s4_points.pack(side="right", padx=5)

    def configure_s5(self):
        self.__frm_s5 = tk.Frame(self.__frm_skills)
        self.__frm_s5.grid(row=5, column=0, padx=10, pady=5, sticky="we")
        self.__btn_s5_minus = tk.Button(self.__frm_s5, text="–", font=("book antiqua", 15), width=2,
                                        command=self.dec_s5)
        self.__btn_s5_plus = tk.Button(self.__frm_s5, text="+", font=("book antiqua", 15), width=2,
                                       command=self.inc_s5)
        self.__lbl_s5 = tk.Label(self.__frm_s5, text="Obycie", font=("book antiqua", 15))
        self.__lbl_s5_points = tk.Label(self.__frm_s5, text=self.__character_sheet.get_skill_val('obycie'),
                                        font=("book antiqua", 16, "bold"), fg="grey")
        self.__btn_s5_minus.pack(side="left")
        self.__btn_s5_plus.pack(side="left")
        self.__lbl_s5.pack(side="left", padx=15)
        self.__lbl_s5_points.pack(side="right", padx=5)

    def configure_s6(self):
        self.__frm_s6 = tk.Frame(self.__frm_skills)
        self.__frm_s6.grid(row=6, column=0, padx=10, pady=5, sticky="we")
        self.__btn_s6_minus = tk.Button(self.__frm_s6, text="–", font=("book antiqua", 15), width=2,
                                        command=self.dec_s6)
        self.__btn_s6_plus = tk.Button(self.__frm_s6, text="+", font=("book antiqua", 15), width=2,
                                       command=self.inc_s6)
        self.__lbl_s6 = tk.Label(self.__frm_s6, text="Perswazja", font=("book antiqua", 15))
        self.__lbl_s6_points = tk.Label(self.__frm_s6, text=self.__character_sheet.get_skill_val('perswazja'),
                                        font=("book antiqua", 16, "bold"), fg="grey")
        self.__btn_s6_minus.pack(side="left")
        self.__btn_s6_plus.pack(side="left")
        self.__lbl_s6.pack(side="left", padx=15)
        self.__lbl_s6_points.pack(side="right", padx=5)

    def configure_s7(self):
        self.__frm_s7 = tk.Frame(self.__frm_skills)
        self.__frm_s7.grid(row=7, column=0, padx=10, pady=5, sticky="we")
        self.__btn_s7_minus = tk.Button(self.__frm_s7, text="–", font=("book antiqua", 15), width=2,
                                        command=self.dec_s7)
        self.__btn_s7_plus = tk.Button(self.__frm_s7, text="+", font=("book antiqua", 15), width=2,
                                       command=self.inc_s7)
        self.__lbl_s7 = tk.Label(self.__frm_s7, text="Przetrwanie", font=("book antiqua", 15))
        self.__lbl_s7_points = tk.Label(self.__frm_s7, text=self.__character_sheet.get_skill_val('przetrwanie'),
                                        font=("book antiqua", 16, "bold"), fg="grey")
        self.__btn_s7_minus.pack(side="left")
        self.__btn_s7_plus.pack(side="left")
        self.__lbl_s7.pack(side="left", padx=15)
        self.__lbl_s7_points.pack(side="right", padx=5)

    def configure_s8(self):
        self.__frm_s8 = tk.Frame(self.__frm_skills)
        self.__frm_s8.grid(row=8, column=0, padx=10, pady=5, sticky="we")
        self.__btn_s8_minus = tk.Button(self.__frm_s8, text="–", font=("book antiqua", 15), width=2,
                                        command=self.dec_s8)
        self.__btn_s8_plus = tk.Button(self.__frm_s8, text="+", font=("book antiqua", 15), width=2,
                                       command=self.inc_s8)
        self.__lbl_s8 = tk.Label(self.__frm_s8, text="Rzemiosło", font=("book antiqua", 15))
        self.__lbl_s8_points = tk.Label(self.__frm_s8, text=self.__character_sheet.get_skill_val('rzemiosło'),
                                        font=("book antiqua", 16, "bold"), fg="grey")
        self.__btn_s8_minus.pack(side="left")
        self.__btn_s8_plus.pack(side="left")
        self.__lbl_s8.pack(side="left", padx=15)
        self.__lbl_s8_points.pack(side="right", padx=5)

    def configure_s9(self):
        self.__frm_s9 = tk.Frame(self.__frm_skills)
        self.__frm_s9.grid(row=9, column=0, padx=10, pady=5, sticky="we")
        self.__btn_s9_minus = tk.Button(self.__frm_s9, text="–", font=("book antiqua", 15), width=2,
                                        command=self.dec_s9)
        self.__btn_s9_plus = tk.Button(self.__frm_s9, text="+", font=("book antiqua", 15), width=2,
                                       command=self.inc_s9)
        self.__lbl_s9 = tk.Label(self.__frm_s9, text="Siła woli", font=("book antiqua", 15))
        self.__lbl_s9_points = tk.Label(self.__frm_s9, text=self.__character_sheet.get_skill_val('siła woli'),
                                        font=("book antiqua", 16, "bold"), fg="grey")
        self.__btn_s9_minus.pack(side="left")
        self.__btn_s9_plus.pack(side="left")
        self.__lbl_s9.pack(side="left", padx=15)
        self.__lbl_s9_points.pack(side="right", padx=5)

    def configure_s10(self):
        self.__frm_s10 = tk.Frame(self.__frm_skills)
        self.__frm_s10.grid(row=10, column=0, padx=10, pady=5, sticky="we")
        self.__btn_s10_minus = tk.Button(self.__frm_s10, text="–", font=("book antiqua", 15), width=2,
                                         command=self.dec_s10)
        self.__btn_s10_plus = tk.Button(self.__frm_s10, text="+", font=("book antiqua", 15), width=2,
                                        command=self.inc_s10)
        self.__lbl_s10 = tk.Label(self.__frm_s10, text="Skradanie", font=("book antiqua", 15))
        self.__lbl_s10_points = tk.Label(self.__frm_s10, text=self.__character_sheet.get_skill_val('skradanie'),
                                         font=("book antiqua", 16, "bold"), fg="grey")
        self.__btn_s10_minus.pack(side="left")
        self.__btn_s10_plus.pack(side="left")
        self.__lbl_s10.pack(side="left", padx=15)
        self.__lbl_s10_points.pack(side="right", padx=5)

    def configure_s11(self):
        self.__frm_s11 = tk.Frame(self.__frm_skills)
        self.__frm_s11.grid(row=1, column=1, padx=10, pady=5, sticky="we")
        self.__btn_s11_minus = tk.Button(self.__frm_s11, text="–", font=("book antiqua", 15), width=2,
                                         command=self.dec_s11)
        self.__btn_s11_plus = tk.Button(self.__frm_s11, text="+", font=("book antiqua", 15), width=2,
                                        command=self.inc_s11)
        self.__lbl_s11 = tk.Label(self.__frm_s11, text="Skupienie", font=("book antiqua", 15))
        self.__lbl_s11_points = tk.Label(self.__frm_s11, text=self.__character_sheet.get_skill_val('skupienie'),
                                         font=("book antiqua", 16, "bold"), fg="grey")
        self.__btn_s11_minus.pack(side="left")
        self.__btn_s11_plus.pack(side="left")
        self.__lbl_s11.pack(side="left", padx=15)
        self.__lbl_s11_points.pack(side="right", padx=5)

    def configure_s12(self):
        self.__frm_s12 = tk.Frame(self.__frm_skills)
        self.__frm_s12.grid(row=2, column=1, padx=10, pady=5, sticky="we")
        self.__btn_s12_minus = tk.Button(self.__frm_s12, text="–", font=("book antiqua", 15), width=2,
                                         command=self.dec_s12)
        self.__btn_s12_plus = tk.Button(self.__frm_s12, text="+", font=("book antiqua", 15), width=2,
                                        command=self.inc_s12)
        self.__lbl_s12 = tk.Label(self.__frm_s12, text="Spostrzegawczość", font=("book antiqua", 15))
        self.__lbl_s12_points = tk.Label(self.__frm_s12, text=self.__character_sheet.get_skill_val('spostrzegawczość'),
                                         font=("book antiqua", 16, "bold"), fg="grey")
        self.__btn_s12_minus.pack(side="left")
        self.__btn_s12_plus.pack(side="left")
        self.__lbl_s12.pack(side="left", padx=15)
        self.__lbl_s12_points.pack(side="right", padx=5)

    def configure_s13(self):
        self.__frm_s13 = tk.Frame(self.__frm_skills)
        self.__frm_s13.grid(row=3, column=1, padx=10, pady=5, sticky="we")
        self.__btn_s13_minus = tk.Button(self.__frm_s13, text="–", font=("book antiqua", 15), width=2,
                                         command=self.dec_s13)
        self.__btn_s13_plus = tk.Button(self.__frm_s13, text="+", font=("book antiqua", 15), width=2,
                                        command=self.inc_s13)
        self.__lbl_s13 = tk.Label(self.__frm_s13, text="Strzelectwo", font=("book antiqua", 15))
        self.__lbl_s13_points = tk.Label(self.__frm_s13, text=self.__character_sheet.get_skill_val('strzelectwo'),
                                         font=("book antiqua", 16, "bold"), fg="grey")
        self.__btn_s13_minus.pack(side="left")
        self.__btn_s13_plus.pack(side="left")
        self.__lbl_s13.pack(side="left", padx=15)
        self.__lbl_s13_points.pack(side="right", padx=5)

    def configure_s14(self):
        self.__frm_s14 = tk.Frame(self.__frm_skills)
        self.__frm_s14.grid(row=4, column=1, padx=10, pady=5, sticky="we")
        self.__btn_s14_minus = tk.Button(self.__frm_s14, text="–", font=("book antiqua", 15), width=2,
                                         command=self.dec_s14)
        self.__btn_s14_plus = tk.Button(self.__frm_s14, text="+", font=("book antiqua", 15), width=2,
                                        command=self.inc_s14)
        self.__lbl_s14 = tk.Label(self.__frm_s14, text="Walka", font=("book antiqua", 15))
        self.__lbl_s14_points = tk.Label(self.__frm_s14, text=self.__character_sheet.get_skill_val('walka'),
                                         font=("book antiqua", 16, "bold"), fg="grey")
        self.__btn_s14_minus.pack(side="left")
        self.__btn_s14_plus.pack(side="left")
        self.__lbl_s14.pack(side="left", padx=15)
        self.__lbl_s14_points.pack(side="right", padx=5)

    def configure_s15(self):
        self.__frm_s15 = tk.Frame(self.__frm_skills)
        self.__frm_s15.grid(row=5, column=1, padx=10, pady=5, sticky="we")
        self.__btn_s15_minus = tk.Button(self.__frm_s15, text="–", font=("book antiqua", 15), width=2,
                                         command=self.dec_s15)
        self.__btn_s15_plus = tk.Button(self.__frm_s15, text="+", font=("book antiqua", 15), width=2,
                                        command=self.inc_s15)
        self.__lbl_s15 = tk.Label(self.__frm_s15, text="Wykształcenie", font=("book antiqua", 15))
        self.__lbl_s15_points = tk.Label(self.__frm_s15, text=self.__character_sheet.get_skill_val('wykształcenie'),
                                         font=("book antiqua", 16, "bold"), fg="grey")
        self.__btn_s15_minus.pack(side="left")
        self.__btn_s15_plus.pack(side="left")
        self.__lbl_s15.pack(side="left", padx=15)
        self.__lbl_s15_points.pack(side="right", padx=5)

    def configure_s16(self):
        self.__frm_s16 = tk.Frame(self.__frm_skills)
        self.__frm_s16.grid(row=6, column=1, padx=10, pady=5, sticky="we")
        self.__btn_s16_minus = tk.Button(self.__frm_s16, text="–", font=("book antiqua", 15), width=2,
                                         command=self.dec_s16)
        self.__btn_s16_plus = tk.Button(self.__frm_s16, text="+", font=("book antiqua", 15), width=2,
                                        command=self.inc_s16)
        self.__lbl_s16 = tk.Label(self.__frm_s16, text="Wysportowanie", font=("book antiqua", 15))
        self.__lbl_s16_points = tk.Label(self.__frm_s16, text=self.__character_sheet.get_skill_val('wysportowanie'),
                                         font=("book antiqua", 16, "bold"), fg="grey")
        self.__btn_s16_minus.pack(side="left")
        self.__btn_s16_plus.pack(side="left")
        self.__lbl_s16.pack(side="left", padx=15)
        self.__lbl_s16_points.pack(side="right", padx=5)

    def configure_s17(self):
        self.__frm_s17 = tk.Frame(self.__frm_skills)
        self.__frm_s17.grid(row=7, column=1, padx=10, pady=5, sticky="we")
        self.__btn_s17_minus = tk.Button(self.__frm_s17, text="–", font=("book antiqua", 15), width=2,
                                         command=self.dec_s17)
        self.__btn_s17_plus = tk.Button(self.__frm_s17, text="+", font=("book antiqua", 15), width=2,
                                        command=self.inc_s17)
        self.__lbl_s17 = tk.Label(self.__frm_s17, text="Zastraszanie", font=("book antiqua", 15))
        self.__lbl_s17_points = tk.Label(self.__frm_s17, text=self.__character_sheet.get_skill_val('zastraszanie'),
                                         font=("book antiqua", 16, "bold"), fg="grey")
        self.__btn_s17_minus.pack(side="left")
        self.__btn_s17_plus.pack(side="left")
        self.__lbl_s17.pack(side="left", padx=15)
        self.__lbl_s17_points.pack(side="right", padx=5)

    def configure_s18(self):
        self.__frm_s18 = tk.Frame(self.__frm_skills)
        self.__frm_s18.grid(row=8, column=1, padx=10, pady=5, sticky="we")
        self.__btn_s18_minus = tk.Button(self.__frm_s18, text="–", font=("book antiqua", 15), width=2,
                                         command=self.dec_s18)
        self.__btn_s18_plus = tk.Button(self.__frm_s18, text="+", font=("book antiqua", 15), width=2,
                                        command=self.inc_s18)
        self.__lbl_s18 = tk.Label(self.__frm_s18, text="Złodziejstwo", font=("book antiqua", 15))
        self.__lbl_s18_points = tk.Label(self.__frm_s18, text=self.__character_sheet.get_skill_val('złodziejstwo'),
                                         font=("book antiqua", 16, "bold"), fg="grey")
        self.__btn_s18_minus.pack(side="left")
        self.__btn_s18_plus.pack(side="left")
        self.__lbl_s18.pack(side="left", padx=15)
        self.__lbl_s18_points.pack(side="right", padx=5)

    def configure_s19(self):
        self.__frm_s19 = tk.Frame(self.__frm_skills)
        self.__frm_s19.grid(row=9, column=1, padx=10, pady=5, sticky="we")
        self.__btn_s19_minus = tk.Button(self.__frm_s19, text="–", font=("book antiqua", 15), width=2,
                                         command=self.dec_s19)
        self.__btn_s19_plus = tk.Button(self.__frm_s19, text="+", font=("book antiqua", 15), width=2,
                                        command=self.inc_s19)
        self.__lbl_s19 = tk.Label(self.__frm_s19, text="Żegluga", font=("book antiqua", 15))
        self.__lbl_s19_points = tk.Label(self.__frm_s19, text=self.__character_sheet.get_skill_val('żegluga'),
                                         font=("book antiqua", 16, "bold"), fg="grey")
        self.__btn_s19_minus.pack(side="left")
        self.__btn_s19_plus.pack(side="left")
        self.__lbl_s19.pack(side="left", padx=15)
        self.__lbl_s19_points.pack(side="right", padx=5)

    def configure_buttons_frame(self):
        self.__frm_buttons = tk.Frame(self, bg="#dddddd", width=360, height=600)
        self.__frm_buttons.grid_propagate(False)
        self.__frm_buttons.grid(row=1, column=2, padx=5, pady=5)
        self.__frm_buttons.columnconfigure(0, weight=1)
        self.__frm_buttons.rowconfigure(0, weight=1)
        self.__frm_buttons_centered = tk.Frame(self.__frm_buttons, bg="#dddddd")
        self.__frm_buttons_centered.grid(row=0, column=0)
        self.configure_buttons_roll()
        self.configure_buttons_health()
        self.configure_buttons_energy()
        self.configure_buttons_exp()
        self.configure_buttons_luck()

    def configure_buttons_roll(self):
        self.__btn_roll_for = tk.Button(self.__frm_buttons_centered, text="Rzuć na...",
                                        font=("book antiqua", 15, "italic"), command=self.roll_for)
        self.__btn_roll_against_death = tk.Button(self.__frm_buttons_centered, text="Rzuć przeciwko Śmierci",
                                                  font=("book antiqua", 15, "italic"), command=self.roll_against_death)
        self.__btn_roll_damage = tk.Button(self.__frm_buttons_centered, text="Rzuć na obrażenia",
                                           font=("book antiqua", 15, "italic"), command=self.roll_damage)
        self.__btn_roll_initiative = tk.Button(self.__frm_buttons_centered, text="Rzuć na inicjatywę",
                                               font=("book antiqua", 15, "italic"), command=self.roll_initiative)
        self.__btn_roll_for.grid(row=0, column=0, columnspan=2, pady=5, sticky="we")
        self.__btn_roll_against_death.grid(row=1, column=0, columnspan=2, pady=5, sticky="we")
        self.__btn_roll_damage.grid(row=2, column=0, pady=5, sticky="we")
        self.__btn_roll_initiative.grid(row=2, column=1, pady=5, sticky="we")

    def configure_buttons_health(self):
        self.__btn_lose_health = tk.Button(self.__frm_buttons_centered, text="Przyjmij obrażenia",
                                           font=("book antiqua", 15, "italic"), command=self.lose_health)
        self.__btn_heal_health = tk.Button(self.__frm_buttons_centered, text="Wylecz obrażenia",
                                           font=("book antiqua", 15, "italic"), command=self.heal_health)
        self.__btn_lose_health.grid(row=3, column=0, pady=5, sticky="we")
        self.__btn_heal_health.grid(row=3, column=1, pady=5, sticky="we")

    def configure_buttons_energy(self):
        self.__btn_spend_energy = tk.Button(self.__frm_buttons_centered, text="Zużyj Energię",
                                            font=("book antiqua", 15, "italic"), command=self.spend_energy)
        self.__btn_regain_energy = tk.Button(self.__frm_buttons_centered, text="Odnów Energię",
                                             font=("book antiqua", 15, "italic"), command=self.regain_energy)
        self.__btn_spend_energy.grid(row=4, column=0, pady=5, sticky="we")
        self.__btn_regain_energy.grid(row=4, column=1, pady=5, sticky="we")

    def configure_buttons_exp(self):
        self.__btn_gain_exp = tk.Button(self.__frm_buttons_centered, text="Otrzymaj Punkty Doświadczenia",
                                        font=("book antiqua", 15, "italic"), command=self.gain_exp)
        self.__btn_spend_exp = tk.Button(self.__frm_buttons_centered, text="Zużyj Punkty Doświadczenia",
                                         font=("book antiqua", 15, "italic"), command=self.spend_exp)
        self.__btn_gain_exp.grid(row=5, column=0, columnspan=2, pady=5, sticky="we")
        self.__btn_spend_exp.grid(row=6, column=0, columnspan=2, pady=5, sticky="we")

    def configure_buttons_luck(self):
        self.__btn_burn = tk.Button(self.__frm_buttons_centered, text="Spal Punkt Szczęścia",
                                    font=("book antiqua", 15, "italic"), command=self.burn_luck_point)
        self.__btn_burn.grid(row=7, column=0, columnspan=2, pady=5, sticky="we")

    def configure_equipment_frame(self):
        self.__frm_equipment = tk.Frame(self, relief="ridge", borderwidth=2, width=435, height=220)
        self.__frm_equipment.grid_propagate(False)
        self.__frm_equipment.grid(row=2, column=0, padx=5, pady=5)
        self.configure_e_title()
        self.configure_e1()
        self.configure_e2()
        self.configure_e3()

    def configure_e_title(self):
        self.__frm_e_title = tk.Frame(self.__frm_equipment)
        self.__frm_e_title.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.__lbl_e_title = tk.Label(self.__frm_e_title, text="Ekwipunek", font=("century schoolbook", 20, "bold"))
        self.__lbl_e_title.grid(row=0, column=0)

    def configure_e1(self):
        self.__frm_e1 = tk.Frame(self.__frm_equipment)
        self.__frm_e1.grid(row=1, column=0, padx=10, pady=5, sticky="we")
        self.__btn_e1_minus = tk.Button(self.__frm_e1, text="–", font=("book antiqua", 15), width=2,
                                        command=self.dec_e1)
        self.__btn_e1_plus = tk.Button(self.__frm_e1, text="+", font=("book antiqua", 15), width=2,
                                       command=self.inc_e1)
        self.__lbl_e1 = tk.Label(self.__frm_e1, text="Pancerz", font=("book antiqua", 15))
        self.__lbl_e1_points = tk.Label(self.__frm_e1, text=self.__character_sheet.armour,
                                        font=("book antiqua", 16, "bold"), fg="grey")
        self.__btn_e1_minus.pack(side="left")
        self.__btn_e1_plus.pack(side="left")
        self.__lbl_e1.pack(side="left", padx=15)
        self.__lbl_e1_points.pack(side="right", padx=5)

    def configure_e2(self):
        self.__frm_e2 = tk.Frame(self.__frm_equipment)
        self.__frm_e2.grid(row=2, column=0, padx=10, pady=5, sticky="we")
        self.__btn_e2_minus = tk.Button(self.__frm_e2, text="–", font=("book antiqua", 15), width=2,
                                        command=self.dec_e2)
        self.__btn_e2_plus = tk.Button(self.__frm_e2, text="+", font=("book antiqua", 15), width=2,
                                       command=self.inc_e2)
        self.__lbl_e2 = tk.Label(self.__frm_e2, text="Tarcza", font=("book antiqua", 15))
        self.__lbl_e2_points = tk.Label(self.__frm_e2, text=self.__character_sheet.shield,
                                        font=("book antiqua", 16, "bold"), fg="grey")
        self.__btn_e2_minus.pack(side="left")
        self.__btn_e2_plus.pack(side="left")
        self.__lbl_e2.pack(side="left", padx=15)
        self.__lbl_e2_points.pack(side="right", padx=5)

    def configure_e3(self):
        self.__frm_e3 = tk.Frame(self.__frm_equipment)
        self.__frm_e3.grid(row=3, column=0, padx=10, pady=5, sticky="we")
        self.__btn_e3_minus = tk.Button(self.__frm_e3, text="–", font=("book antiqua", 15), width=2,
                                        command=self.dec_e3)
        self.__btn_e3_plus = tk.Button(self.__frm_e3, text="+", font=("book antiqua", 15), width=2,
                                       command=self.inc_e3)
        self.__lbl_e3 = tk.Label(self.__frm_e3, text="Broń", font=("book antiqua", 15))
        self.__lbl_e3_points = tk.Label(self.__frm_e3, text=self.__character_sheet.weapon,
                                        font=("book antiqua", 16, "bold"), fg="grey")
        self.__btn_e3_minus.pack(side="left")
        self.__btn_e3_plus.pack(side="left")
        self.__lbl_e3.pack(side="left", padx=15)
        self.__lbl_e3_points.pack(side="right", padx=5)

    def configure_stats_frame(self):
        self.__frm_stats = tk.Frame(self, relief="ridge", borderwidth=2, width=695, height=220)
        self.__frm_stats.grid_propagate(False)
        self.__frm_stats.grid(row=2, column=1, padx=5, pady=5)
        for i in range(3):
            self.__frm_stats.columnconfigure(i, weight=1)
            self.__frm_stats.rowconfigure(i, weight=1)
        self.configure_mage()
        self.configure_health()
        self.configure_energy()
        self.configure_initiative()

    def configure_mage(self):
        self.__frm_mage = tk.Frame(self.__frm_stats)
        self.__lbl_mage = tk.Label(self.__frm_mage, text="Spokrewnienie", font=("book antiqua", 20, "bold"))
        self.__bv_mage = tk.BooleanVar(self.__frm_mage, self.__character_sheet.is_mage)
        self.__chb_mage = tk.Checkbutton(self.__frm_mage, var=self.__bv_mage, command=self.manage_mage)
        self.__lbl_mage.pack(side="left")
        self.__chb_mage.pack(side="right")
        self.__frm_mage.grid(row=1, column=0)

    def configure_health(self):
        self.__frm_health = tk.Frame(self.__frm_stats)
        self.__lbl_health = tk.Label(self.__frm_health, text="Zdrowie", font=("book antiqua", 20, "bold"))
        self.__lbl_health_points = tk.Label(self.__frm_health, text=self.__character_sheet.health,
                                            font=("book antiqua", 21, "bold"), fg="grey", width=2)
        self.__lbl_health.pack(side="left")
        self.__lbl_health_points.pack(side="right")
        self.__frm_health.grid(row=0, column=1, sticky="we")

    def configure_energy(self):
        self.__frm_energy = tk.Frame(self.__frm_stats)
        self.__lbl_energy = tk.Label(self.__frm_energy, text="Energia", font=("book antiqua", 20, "bold"))
        self.__lbl_energy_points = tk.Label(self.__frm_energy, text=self.__character_sheet.energy,
                                            font=("book antiqua", 21, "bold"), fg="grey", width=2)
        self.__lbl_energy.pack(side="left")
        self.__lbl_energy_points.pack(side="right")
        self.__frm_energy.grid(row=1, column=1, sticky="we")

    def configure_initiative(self):
        self.__frm_initiative = tk.Frame(self.__frm_stats)
        self.__lbl_initiative = tk.Label(self.__frm_initiative, text="Inicjatywa", font=("book antiqua", 20, "bold"))
        self.__lbl_initiative_points = tk.Label(self.__frm_initiative, text=self.__character_sheet.initiative,
                                                font=("book antiqua", 21, "bold"), fg="grey", width=2)
        self.__lbl_initiative.pack(side="left")
        self.__lbl_initiative_points.pack(side="right")
        self.__frm_initiative.grid(row=2, column=1, sticky="we")

    def configure_points_frame(self):
        self.__frm_points = tk.Frame(self, relief="ridge", borderwidth=2, width=360, height=220)
        self.__frm_points.grid_propagate(False)
        for i in range(2):
            self.__frm_points.rowconfigure(i, weight=1)
        self.__frm_points.grid(row=2, column=2, padx=5, pady=5)
        self.configure_luck_points()
        self.configure_exp_points()

    def configure_luck_points(self):
        self.__frm_luck = tk.Frame(self.__frm_points)
        self.__frm_luck.grid(row=0, column=0, padx=10)
        self.__lbl_luck_title = tk.Label(self.__frm_luck, text="Punkty Szczęścia",
                                         font=("century schoolbook", 20, "bold"))
        self.__lbl_luck_points = tk.Label(self.__frm_luck, text=self.__character_sheet.luck_points,
                                          font=("century schoolbook", 20, "bold"), fg="grey")
        self.__lbl_luck_title.grid(row=0, column=0)
        self.__lbl_luck_points.grid(row=1, column=0)

    def configure_exp_points(self):
        self.__frm_exp = tk.Frame(self.__frm_points)
        self.__frm_exp.grid(row=1, column=0, padx=10)
        self.__lbl_exp_title = tk.Label(self.__frm_exp, text="Punkty Doświadczenia",
                                        font=("century schoolbook", 20, "bold"))
        self.__lbl_exp_points = tk.Label(self.__frm_exp, text=self.__character_sheet.exp_points,
                                         font=("century schoolbook", 20, "bold"), fg="grey")
        self.__lbl_exp_title.grid(row=1, column=0)
        self.__lbl_exp_points.grid(row=2, column=0)

    def reset(self):
        self.__dlg_reset = ifd.IfDialog(self, self.__character_sheet, "Wyczyścić kartę?")

    def prep_for_new_campaign(self):
        self.__dlg_new_campaign = ifd.IfDialog(self, self.__character_sheet, "Zacząć nową kampanię?")

    def edit_name(self):
        self.__character_sheet.set_concept("imię", self.__sv_name.get())

    def edit_race(self):
        self.__character_sheet.set_concept("pochodzenie", self.__sv_race.get())

    def edit_player(self):
        self.__character_sheet.set_concept("gracz", self.__sv_player.get())

    def edit_class(self):
        self.__character_sheet.set_concept("klasa", self.__sv_class.get())
        self.__character_sheet.calculate_energy()
        self.update_energy()

    def manage_checkbox_mage(self):
        if self.__iv_a_points.get() == 0 and not self.__bv_mage.get():
            self.__chb_mage.config(state="disabled")
        else:
            self.__chb_mage.config(state="normal")

    def inc_a1(self):
        if self.__character_sheet.inc_attribute('krzepa'):
            self.__lbl_a1_points["text"] = self.__character_sheet.get_attribute_val('krzepa')
            self.__iv_a_points.set(self.__character_sheet.attribute_points)

    def dec_a1(self):
        if self.__character_sheet.dec_attribute('krzepa'):
            self.__lbl_a1_points["text"] = self.__character_sheet.get_attribute_val('krzepa')
            self.__iv_a_points.set(self.__character_sheet.attribute_points)

    def inc_a2(self):
        if self.__character_sheet.inc_attribute('wytrzymałość'):
            self.__lbl_a2_points["text"] = self.__character_sheet.get_attribute_val('wytrzymałość')
            self.__iv_a_points.set(self.__character_sheet.attribute_points)
            self.__character_sheet.calculate_health()
            self.update_health()

    def dec_a2(self):
        if self.__character_sheet.dec_attribute('wytrzymałość'):
            self.__lbl_a2_points["text"] = self.__character_sheet.get_attribute_val('wytrzymałość')
            self.__iv_a_points.set(self.__character_sheet.attribute_points)
            self.__character_sheet.calculate_health()
            self.update_health()

    def inc_a3(self):
        if self.__character_sheet.inc_attribute('zręczność'):
            self.__lbl_a3_points["text"] = self.__character_sheet.get_attribute_val('zręczność')
            self.__iv_a_points.set(self.__character_sheet.attribute_points)
            self.__character_sheet.calculate_initiative()
            self.__lbl_initiative_points["text"] = self.__character_sheet.initiative
            if self.__character_sheet.get_concept_val('klasa') == "Waleczny":
                self.__character_sheet.calculate_energy()
                self.update_energy()

    def dec_a3(self):
        if self.__character_sheet.dec_attribute('zręczność'):
            self.__lbl_a3_points["text"] = self.__character_sheet.get_attribute_val('zręczność')
            self.__iv_a_points.set(self.__character_sheet.attribute_points)
            self.__character_sheet.calculate_initiative()
            self.__lbl_initiative_points["text"] = self.__character_sheet.initiative
            if self.__character_sheet.get_concept_val('klasa') == "Waleczny":
                self.__character_sheet.calculate_energy()
                self.update_energy()

    def inc_a4(self):
        if self.__character_sheet.inc_attribute('zmysły'):
            self.__lbl_a4_points["text"] = self.__character_sheet.get_attribute_val('zmysły')
            self.__iv_a_points.set(self.__character_sheet.attribute_points)

    def dec_a4(self):
        if self.__character_sheet.dec_attribute('zmysły'):
            self.__lbl_a4_points["text"] = self.__character_sheet.get_attribute_val('zmysły')
            self.__iv_a_points.set(self.__character_sheet.attribute_points)

    def inc_a5(self):
        if self.__character_sheet.inc_attribute('intelekt'):
            self.__lbl_a5_points["text"] = self.__character_sheet.get_attribute_val('intelekt')
            self.__iv_a_points.set(self.__character_sheet.attribute_points)
            if self.__character_sheet.get_concept_val('klasa') == "Uczony":
                self.__character_sheet.calculate_energy()
                self.update_energy()

    def dec_a5(self):
        if self.__character_sheet.dec_attribute('intelekt'):
            self.__lbl_a5_points["text"] = self.__character_sheet.get_attribute_val('intelekt')
            self.__iv_a_points.set(self.__character_sheet.attribute_points)
            if self.__character_sheet.get_concept_val('klasa') == "Uczony":
                self.__character_sheet.calculate_energy()
                self.update_energy()

    def inc_a6(self):
        if self.__character_sheet.inc_attribute('charakter'):
            self.__lbl_a6_points["text"] = self.__character_sheet.get_attribute_val('charakter')
            self.__iv_a_points.set(self.__character_sheet.attribute_points)
            if self.__character_sheet.get_concept_val('klasa') == "Cwany":
                self.__character_sheet.calculate_energy()
                self.update_energy()

    def dec_a6(self):
        if self.__character_sheet.dec_attribute('charakter'):
            self.__lbl_a6_points["text"] = self.__character_sheet.get_attribute_val('charakter')
            self.__iv_a_points.set(self.__character_sheet.attribute_points)
            if self.__character_sheet.get_concept_val('klasa') == "Cwany":
                self.__character_sheet.calculate_energy()
                self.update_energy()

    def inc_s1(self):
        if self.__character_sheet.inc_skill('blef'):
            self.__lbl_s1_points["text"] = self.__character_sheet.get_skill_val('blef')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def dec_s1(self):
        if self.__character_sheet.dec_skill('blef'):
            self.__lbl_s1_points["text"] = self.__character_sheet.get_skill_val('blef')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def inc_s2(self):
        if self.__character_sheet.inc_skill('empatia'):
            self.__lbl_s2_points["text"] = self.__character_sheet.get_skill_val('empatia')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def dec_s2(self):
        if self.__character_sheet.dec_skill('empatia'):
            self.__lbl_s2_points["text"] = self.__character_sheet.get_skill_val('empatia')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def inc_s3(self):
        if self.__character_sheet.inc_skill('jeździectwo'):
            self.__lbl_s3_points["text"] = self.__character_sheet.get_skill_val('jeździectwo')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def dec_s3(self):
        if self.__character_sheet.dec_skill('jeździectwo'):
            self.__lbl_s3_points["text"] = self.__character_sheet.get_skill_val('jeździectwo')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def inc_s4(self):
        if self.__character_sheet.inc_skill('leczenie'):
            self.__lbl_s4_points["text"] = self.__character_sheet.get_skill_val('leczenie')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def dec_s4(self):
        if self.__character_sheet.dec_skill('leczenie'):
            self.__lbl_s4_points["text"] = self.__character_sheet.get_skill_val('leczenie')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def inc_s5(self):
        if self.__character_sheet.inc_skill('obycie'):
            self.__lbl_s5_points["text"] = self.__character_sheet.get_skill_val('obycie')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def dec_s5(self):
        if self.__character_sheet.dec_skill('obycie'):
            self.__lbl_s5_points["text"] = self.__character_sheet.get_skill_val('obycie')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def inc_s6(self):
        if self.__character_sheet.inc_skill('perswazja'):
            self.__lbl_s6_points["text"] = self.__character_sheet.get_skill_val('perswazja')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def dec_s6(self):
        if self.__character_sheet.dec_skill('perswazja'):
            self.__lbl_s6_points["text"] = self.__character_sheet.get_skill_val('perswazja')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def inc_s7(self):
        if self.__character_sheet.inc_skill('przetrwanie'):
            self.__lbl_s7_points["text"] = self.__character_sheet.get_skill_val('przetrwanie')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def dec_s7(self):
        if self.__character_sheet.dec_skill('przetrwanie'):
            self.__lbl_s7_points["text"] = self.__character_sheet.get_skill_val('przetrwanie')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def inc_s8(self):
        if self.__character_sheet.inc_skill('rzemiosło'):
            self.__lbl_s8_points["text"] = self.__character_sheet.get_skill_val('rzemiosło')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def dec_s8(self):
        if self.__character_sheet.dec_skill('rzemiosło'):
            self.__lbl_s8_points["text"] = self.__character_sheet.get_skill_val('rzemiosło')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def inc_s9(self):
        if self.__character_sheet.inc_skill('siła woli'):
            self.__lbl_s9_points["text"] = self.__character_sheet.get_skill_val('siła woli')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points
            self.__character_sheet.calculate_energy()
            self.update_energy()

    def dec_s9(self):
        if self.__character_sheet.dec_skill('siła woli'):
            self.__lbl_s9_points["text"] = self.__character_sheet.get_skill_val('siła woli')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points
            self.__character_sheet.calculate_energy()
            self.update_energy()

    def inc_s10(self):
        if self.__character_sheet.inc_skill('skradanie'):
            self.__lbl_s10_points["text"] = self.__character_sheet.get_skill_val('skradanie')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def dec_s10(self):
        if self.__character_sheet.dec_skill('skradanie'):
            self.__lbl_s10_points["text"] = self.__character_sheet.get_skill_val('skradanie')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def inc_s11(self):
        if self.__character_sheet.inc_skill('skupienie'):
            self.__lbl_s11_points["text"] = self.__character_sheet.get_skill_val('skupienie')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def dec_s11(self):
        if self.__character_sheet.dec_skill('skupienie'):
            self.__lbl_s11_points["text"] = self.__character_sheet.get_skill_val('skupienie')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def inc_s12(self):
        if self.__character_sheet.inc_skill('spostrzegawczość'):
            self.__lbl_s12_points["text"] = self.__character_sheet.get_skill_val('spostrzegawczość')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points
            self.__character_sheet.calculate_initiative()
            self.__lbl_initiative_points["text"] = self.__character_sheet.initiative

    def dec_s12(self):
        if self.__character_sheet.dec_skill('spostrzegawczość'):
            self.__lbl_s12_points["text"] = self.__character_sheet.get_skill_val('spostrzegawczość')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points
            self.__character_sheet.calculate_initiative()
            self.__lbl_initiative_points["text"] = self.__character_sheet.initiative

    def inc_s13(self):
        if self.__character_sheet.inc_skill('strzelectwo'):
            self.__lbl_s13_points["text"] = self.__character_sheet.get_skill_val('strzelectwo')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def dec_s13(self):
        if self.__character_sheet.dec_skill('strzelectwo'):
            self.__lbl_s13_points["text"] = self.__character_sheet.get_skill_val('strzelectwo')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def inc_s14(self):
        if self.__character_sheet.inc_skill('walka'):
            self.__lbl_s14_points["text"] = self.__character_sheet.get_skill_val('walka')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def dec_s14(self):
        if self.__character_sheet.dec_skill('walka'):
            self.__lbl_s14_points["text"] = self.__character_sheet.get_skill_val('walka')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def inc_s15(self):
        if self.__character_sheet.inc_skill('wykształcenie'):
            self.__lbl_s15_points["text"] = self.__character_sheet.get_skill_val('wykształcenie')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def dec_s15(self):
        if self.__character_sheet.dec_skill('wykształcenie'):
            self.__lbl_s15_points["text"] = self.__character_sheet.get_skill_val('wykształcenie')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def inc_s16(self):
        if self.__character_sheet.inc_skill('wysportowanie'):
            self.__lbl_s16_points["text"] = self.__character_sheet.get_skill_val('wysportowanie')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def dec_s16(self):
        if self.__character_sheet.dec_skill('wysportowanie'):
            self.__lbl_s16_points["text"] = self.__character_sheet.get_skill_val('wysportowanie')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def inc_s17(self):
        if self.__character_sheet.inc_skill('zastraszanie'):
            self.__lbl_s17_points["text"] = self.__character_sheet.get_skill_val('zastraszanie')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def dec_s17(self):
        if self.__character_sheet.dec_skill('zastraszanie'):
            self.__lbl_s17_points["text"] = self.__character_sheet.get_skill_val('zastraszanie')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def inc_s18(self):
        if self.__character_sheet.inc_skill('złodziejstwo'):
            self.__lbl_s18_points["text"] = self.__character_sheet.get_skill_val('złodziejstwo')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def dec_s18(self):
        if self.__character_sheet.dec_skill('złodziejstwo'):
            self.__lbl_s18_points["text"] = self.__character_sheet.get_skill_val('złodziejstwo')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def inc_s19(self):
        if self.__character_sheet.inc_skill('żegluga'):
            self.__lbl_s19_points["text"] = self.__character_sheet.get_skill_val('żegluga')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def dec_s19(self):
        if self.__character_sheet.dec_skill('żegluga'):
            self.__lbl_s19_points["text"] = self.__character_sheet.get_skill_val('żegluga')
            self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def roll_for(self):
        self.__dlg_roll_for = cd.ChoiceDialog(self, self.__character_sheet)

    def roll_against_death(self):
        self.__dlg_against_death = rd.ResultDialog(self, "Rzut przeciwko Śmierci", "Liczba sukcesów",
                                                   self.__character_sheet.roll_against_death())

    def roll_damage(self):
        self.__dlg_damage = rd.ResultDialog(self, "",  "Liczba obrażeń", self.__character_sheet.roll_damage())

    def roll_initiative(self):
        self.__dlg_initiative = rd.ResultDialog(self, "", "Wartość inicjatywy",
                                                self.__character_sheet.roll_initiative())

    def lose_health(self):
        self.__dlg_lose_health = ed.EntryDialog(self, self.__character_sheet, "Obrażenia", "Przyjmij")

    def heal_health(self):
        self.__dlg_heal_health = ed.EntryDialog(self, self.__character_sheet, "Obrażenia", "Wylecz")

    def spend_energy(self):
        self.__dlg_spend_energy = ed.EntryDialog(self, self.__character_sheet, "Energia", "Zużyj")

    def regain_energy(self):
        self.__dlg_regain_energy = ed.EntryDialog(self, self.__character_sheet, "Energia", "Odnów")

    def gain_exp(self):
        self.__dlg_gain_exp = ed.EntryDialog(self, self.__character_sheet, "Punkty Doświadczenia", "Otrzymaj")

    def spend_exp(self):
        self.__dlg_spend_exp = ecd.EntryChoiceDialog(self, self.__character_sheet)

    def burn_luck_point(self):
        if self.__character_sheet.burn_luck_point():
            self.__lbl_luck_points["text"] = self.__character_sheet.luck_points

    def inc_e1(self):
        if self.__character_sheet.inc_armour():
            self.__lbl_e1_points["text"] = self.__character_sheet.armour

    def dec_e1(self):
        if self.__character_sheet.dec_armour():
            self.__lbl_e1_points["text"] = self.__character_sheet.armour

    def inc_e2(self):
        if self.__character_sheet.inc_shield():
            self.__lbl_e2_points["text"] = self.__character_sheet.shield

    def dec_e2(self):
        if self.__character_sheet.dec_shield():
            self.__lbl_e2_points["text"] = self.__character_sheet.shield

    def inc_e3(self):
        if self.__character_sheet.inc_weapon():
            self.__lbl_e3_points["text"] = self.__character_sheet.weapon

    def dec_e3(self):
        if self.__character_sheet.dec_weapon():
            self.__lbl_e3_points["text"] = self.__character_sheet.weapon

    def manage_mage(self):
        if self.__character_sheet.set_is_mage(self.__bv_mage.get()):
            self.__iv_a_points.set(self.__character_sheet.attribute_points)
            self.__character_sheet.calculate_energy()
            self.update_energy()

    def update_name(self):
        self.__sv_name.set(self.__character_sheet.get_concept_val("imię"))
        if self.__sv_name.get() == "":
            self.__ent_name.delete(0, 'end')

    def update_race(self):
        self.__sv_race.set(self.__character_sheet.get_concept_val("pochodzenie"))
        if self.__sv_race.get() == "":
            self.__ent_race.delete(0, 'end')

    def update_player(self):
        self.__sv_player.set(self.__character_sheet.get_concept_val("gracz"))
        if self.__sv_player.get() == "":
            self.__ent_player.delete(0, 'end')

    def update_class(self):
        self.__sv_class.set(self.__character_sheet.get_concept_val("klasa"))
        if self.__sv_class.get() == "":
            self.__cmb_class.current(0)

    def update_a_points(self):
        self.__iv_a_points.set(self.__character_sheet.attribute_points)

    def update_s_points(self):
        self.__lbl_s_points["text"] = self.__character_sheet.skill_points

    def update_armour(self):
        self.__lbl_e1_points["text"] = self.__character_sheet.armour

    def update_shield(self):
        self.__lbl_e2_points["text"] = self.__character_sheet.shield

    def update_weapon(self):
        self.__lbl_e3_points["text"] = self.__character_sheet.weapon

    def update_health(self):
        self.__lbl_health_points["text"] = self.__character_sheet.health

    def update_energy(self):
        self.__lbl_energy_points["text"] = self.__character_sheet.energy

    def update_initiative(self):
        self.__lbl_initiative_points["text"] = self.__character_sheet.initiative

    def update_exp(self):
        self.__lbl_exp_points["text"] = self.__character_sheet.exp_points

    def update_luck(self):
        self.__lbl_luck_points["text"] = self.__character_sheet.luck_points

    def update(self):
        self.update_name()
        self.update_race()
        self.update_player()
        self.update_class()
        self.update_a_points()
        self.update_s_points()
        self.update_armour()
        self.update_shield()
        self.update_weapon()
        self.update_health()
        self.update_energy()
        self.update_initiative()
        self.update_exp()
        self.update_luck()
        self.__bv_mage.set(self.__character_sheet.is_mage)
        self.__lbl_a1_points["text"] = self.__character_sheet.get_attribute_val("krzepa")
        self.__lbl_a2_points["text"] = self.__character_sheet.get_attribute_val("wytrzymałość")
        self.__lbl_a3_points["text"] = self.__character_sheet.get_attribute_val("zręczność")
        self.__lbl_a4_points["text"] = self.__character_sheet.get_attribute_val("zmysły")
        self.__lbl_a5_points["text"] = self.__character_sheet.get_attribute_val("intelekt")
        self.__lbl_a6_points["text"] = self.__character_sheet.get_attribute_val("charakter")
        self.__lbl_s1_points["text"] = self.__character_sheet.get_skill_val("blef")
        self.__lbl_s2_points["text"] = self.__character_sheet.get_skill_val("empatia")
        self.__lbl_s3_points["text"] = self.__character_sheet.get_skill_val("jeździectwo")
        self.__lbl_s4_points["text"] = self.__character_sheet.get_skill_val("leczenie")
        self.__lbl_s5_points["text"] = self.__character_sheet.get_skill_val("obycie")
        self.__lbl_s6_points["text"] = self.__character_sheet.get_skill_val("perswazja")
        self.__lbl_s7_points["text"] = self.__character_sheet.get_skill_val("przetrwanie")
        self.__lbl_s8_points["text"] = self.__character_sheet.get_skill_val("rzemiosło")
        self.__lbl_s9_points["text"] = self.__character_sheet.get_skill_val("siła woli")
        self.__lbl_s10_points["text"] = self.__character_sheet.get_skill_val("skradanie")
        self.__lbl_s11_points["text"] = self.__character_sheet.get_skill_val("skupienie")
        self.__lbl_s12_points["text"] = self.__character_sheet.get_skill_val("spostrzegawczość")
        self.__lbl_s13_points["text"] = self.__character_sheet.get_skill_val("strzelectwo")
        self.__lbl_s14_points["text"] = self.__character_sheet.get_skill_val("walka")
        self.__lbl_s15_points["text"] = self.__character_sheet.get_skill_val("wykształcenie")
        self.__lbl_s16_points["text"] = self.__character_sheet.get_skill_val("wysportowanie")
        self.__lbl_s17_points["text"] = self.__character_sheet.get_skill_val("zastraszanie")
        self.__lbl_s18_points["text"] = self.__character_sheet.get_skill_val("złodziejstwo")
        self.__lbl_s19_points["text"] = self.__character_sheet.get_skill_val("żegluga")
        self.manage_checkbox_mage()

    def on_closing(self):
        self.__dlg_autosave = asd.AutoSaveDialog(self)

    def close(self):
        self.__master.destroy()
