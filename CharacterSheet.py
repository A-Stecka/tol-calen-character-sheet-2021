import json
import Dice


class CharacterSheet:

    def __init__(self):
        self.__concept = {'imię': "", 'pochodzenie': "", 'klasa': "", 'gracz': ""}
        self.__attributes = {'krzepa': 0, 'wytrzymałość': 0, 'zręczność': 0, 'zmysły': 0, 'intelekt': 0, 'charakter': 0}
        self.__skills = {'blef': 0, 'empatia': 0, 'jeździectwo': 0, 'leczenie': 0, 'obycie': 0, 'perswazja': 0,
                         'przetrwanie': 0, 'rzemiosło': 0, 'siła woli': 0, 'skradanie': 0, 'skupienie': 0,
                         'spostrzegawczość': 0, 'strzelectwo': 0, 'walka': 0, 'wykształcenie': 0, 'wysportowanie': 0,
                         'zastraszanie': 0, 'złodziejstwo': 0, 'żegluga': 0}
        self.__point_stats = {'pancerz': 1, 'tarcza': 0, 'broń': 0, 'zdrowie': 0, 'energia': 0, 'inicjatywa': 0,
                              'szczęście': 3, 'doświadczenie': 0, 'atrybuty': 15, 'umiejętności': 20}
        self.__is_mage = False
        self.__dice10 = Dice.Dice(10)
        self.__dice6 = Dice.Dice(6)

    def set_attribute(self, attribute_name, val):
        if val < 0 or val > 5 or self.__point_stats["atrybuty"] - val < 0:
            return False
        self.__attributes[attribute_name] = val
        self.__point_stats["atrybuty"] -= val

    def set_skill(self, skill_name, val):
        if val < 0 or val > 5 or self.__point_stats["umiejętności"] - val < 0:
            return False
        self.__skills[skill_name] = val
        self.__point_stats["umiejętności"] -= val

    def set_armour(self, val):
        if val < 1 or val > 3:
            return False
        self.__point_stats["pancerz"] = val
        return True

    def set_shield(self, val):
        if val < 0 or val > 3:
            return False
        self.__point_stats["tarcza"] = val
        return True

    def set_weapon(self, val):
        if val < 0 or val > 6 or val == 1:
            return False
        self.__point_stats["broń"] = val
        return True

    def roll_for(self, attribute_name, skill_name):
        success_counter = 0
        for i in range(0, 3):
            if self.__dice10.roll_for(self.__attributes[attribute_name], self.__skills[skill_name]):
                success_counter += 1
        return success_counter

    def roll_damage(self):
        damage = 0
        for i in range(0, self.__point_stats['broń']):
            roll_result = self.__dice6.roll()
            if roll_result == 1 or roll_result == 2:
                damage += 1
            if roll_result == 5 or roll_result == 6:
                damage += 2
        return damage

    def roll_initiative(self):
        roll_result = self.__dice10.roll()
        return self.__point_stats['inicjatywa'] + roll_result

    def roll_against_death(self):
        return self.roll_for("wytrzymałość", "przetrwanie")

    def reset(self):
        for key in self.__concept:
            self.__concept[key] = ""
        for key in self.__attributes:
            self.__attributes[key] = 0
        for key in self.__skills:
            self.__skills[key] = 0
        for key in self.__point_stats:
            self.__point_stats[key] = 0
        self.__point_stats['pancerz'] = 1
        self.__point_stats['szczęście'] = 3
        self.__point_stats['atrybuty'] = 15
        self.__point_stats['umiejętności'] = 20
        self.__is_mage = False

    def prep_for_new_campaign(self):
        self.__point_stats['szczęście'] = 3
        for key in self.__point_stats:
            if key == 'doświadczenie' or key == 'atrybuty' or key == 'umiejętności':
                self.__point_stats[key] = 0

    def set_concept(self, field, value):
        if field not in self.__concept:
            return False
        self.__concept[field] = value
        return True

    def inc_attribute(self, attribute):
        if attribute not in self.__attributes:
            return False
        if self.__point_stats['atrybuty'] > 0 and self.__attributes[attribute] < 5:
            self.__attributes[attribute] += 1
            self.__point_stats['atrybuty'] -= 1
            return True
        return False

    def dec_attribute(self, attribute):
        if attribute not in self.__attributes:
            return False
        if self.__attributes[attribute] != 0:
            self.__attributes[attribute] -= 1
            self.__point_stats['atrybuty'] += 1
            return True
        return False

    def inc_skill(self, skill):
        if skill not in self.__skills:
            return False
        if self.__point_stats['umiejętności'] - 1 >= 0 and self.__skills[skill] < 5:
            self.__skills[skill] += 1
            self.__point_stats['umiejętności'] -= 1
            return True
        return False

    def dec_skill(self, skill):
        if skill not in self.__skills:
            return False
        if self.__skills[skill] != 0:
            self.__skills[skill] -= 1
            self.__point_stats['umiejętności'] += 1
            return True
        return False

    def set_is_mage(self, is_mage):
        if self.__is_mage and not is_mage:
            self.__point_stats['atrybuty'] += 1
            self.__is_mage = is_mage
            return True
        if not self.__is_mage and is_mage:
            if self.__point_stats['atrybuty'] - 1 >= 0:
                self.__point_stats['atrybuty'] -= 1
                self.__is_mage = is_mage
                return True
            return False

    def inc_armour(self):
        if self.__point_stats['pancerz'] == 3:
            return False
        self.__point_stats['pancerz'] += 1
        return True

    def dec_armour(self):
        if self.__point_stats['pancerz'] == 1:
            return False
        self.__point_stats['pancerz'] -= 1
        return True

    def inc_shield(self):
        if self.__point_stats['tarcza'] == 3:
            return False
        self.__point_stats['tarcza'] += 1
        return True

    def dec_shield(self):
        if self.__point_stats['tarcza'] == 0:
            return False
        self.__point_stats['tarcza'] -= 1
        return True

    def inc_weapon(self):
        if self.__point_stats['broń'] == 6:
            return False
        if self.__point_stats['broń'] == 0:
            self.__point_stats['broń'] = 2
        else:
            self.__point_stats['broń'] += 1
        return True

    def dec_weapon(self):
        if self.__point_stats['broń'] == 0:
            return False
        if self.__point_stats['broń'] == 2:
            self.__point_stats['broń'] = 0
        else:
            self.__point_stats['broń'] -= 1
        return True

    def calculate_health(self):
        self.__point_stats['zdrowie'] = self.__attributes['wytrzymałość'] * 6

    def calculate_energy(self):
        self.__point_stats['energia'] = 0
        if self.__concept['klasa'] == "Uczony":
            self.__point_stats['energia'] += self.__attributes['intelekt'] * 2
        elif self.__concept['klasa'] == "Waleczny":
            self.__point_stats['energia'] += self.__attributes['zręczność'] * 2
        else:
            self.__point_stats['energia'] += self.__attributes['charakter'] * 2
        self.__point_stats['energia'] += self.__skills['siła woli']
        if self.__is_mage:
            self.__point_stats['energia'] += 1

    def calculate_initiative(self):
        self.__point_stats['inicjatywa'] = self.__attributes['zręczność'] + self.__skills['spostrzegawczość']

    def lose_health(self, no_of_health_points):
        if self.__point_stats['zdrowie'] - no_of_health_points >= 0:
            self.__point_stats['zdrowie'] -= no_of_health_points
        else:
            self.__point_stats['zdrowie'] = 0

    def heal_health(self, no_of_health_points):
        if self.__point_stats['zdrowie'] + no_of_health_points <= self.__attributes['wytrzymałość'] * 6:
            self.__point_stats['zdrowie'] += no_of_health_points
        else:
            self.__point_stats['zdrowie'] = self.__attributes['wytrzymałość'] * 6

    def spend_energy(self, no_of_energy_points):
        if self.__point_stats['energia'] - no_of_energy_points >= 0:
            self.__point_stats['energia'] -= no_of_energy_points
            return True
        return False

    def regain_energy(self, no_of_energy_points):
        max_energy = 0
        if self.__concept['klasa'] == "Uczony":
            max_energy += self.__attributes['intelekt'] * 2
        elif self.__concept['klasa'] == "Waleczny":
            max_energy += self.__attributes['zręczność'] * 2
        else:
            max_energy += self.__attributes['charakter'] * 2
        max_energy += self.__skills['siła woli']
        if self.__is_mage:
            max_energy += 1
        if self.__point_stats['energia'] + no_of_energy_points <= max_energy:
            self.__point_stats['energia'] += no_of_energy_points
        else:
            self.__point_stats['energia'] = max_energy

    def burn_luck_point(self):
        if self.__point_stats['szczęście'] > 0:
            self.__point_stats['szczęście'] -= 1
            return True
        return False

    def set_exp_points(self, no_of_points):
        self.__point_stats['doświadczenie'] = no_of_points

    def spend_exp_on_attributes(self, no_of_points):
        if no_of_points <= self.__point_stats['doświadczenie']:
            self.__point_stats['atrybuty'] += no_of_points
            self.__point_stats['doświadczenie'] -= no_of_points
            return True
        return False

    def spend_exp_on_skills(self, no_of_points):
        if no_of_points <= self.__point_stats['doświadczenie']:
            self.__point_stats['umiejętności'] += no_of_points * 3
            self.__point_stats['doświadczenie'] -= no_of_points
            return True
        return False

    def get_concept_val(self, field):
        if field not in self.__concept:
            return None
        return self.__concept[field]

    def get_attribute_val(self, attribute):
        if attribute not in self.__attributes:
            return None
        return self.__attributes[attribute]

    def get_skill_val(self, skill):
        if skill not in self.__skills:
            return None
        return self.__skills[skill]

    @property
    def is_mage(self):
        return self.__is_mage

    @property
    def armour(self):
        return self.__point_stats['pancerz']

    @property
    def shield(self):
        return self.__point_stats['tarcza']

    @property
    def weapon(self):
        return self.__point_stats['broń']

    @property
    def health(self):
        return self.__point_stats['zdrowie']

    @property
    def energy(self):
        return self.__point_stats['energia']

    @property
    def initiative(self):
        return self.__point_stats['inicjatywa']

    @property
    def luck_points(self):
        return self.__point_stats['szczęście']

    @property
    def exp_points(self):
        return self.__point_stats['doświadczenie']

    @property
    def attribute_points(self):
        return self.__point_stats['atrybuty']

    @property
    def skill_points(self):
        return self.__point_stats['umiejętności']

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def update_with_json(self, json_string):
        json_object = json.loads(json_string)
        if '_CharacterSheet__concept' not in json_object or '_CharacterSheet__attributes' not in json_object or \
                '_CharacterSheet__skills' not in json_object or '_CharacterSheet__point_stats' not in json_object or \
                '_CharacterSheet__is_mage' not in json_object:
            return False
        self.__concept['imię'] = json_object['_CharacterSheet__concept']['imię']
        self.__concept['pochodzenie'] = json_object['_CharacterSheet__concept']['pochodzenie']
        self.__concept['klasa'] = json_object['_CharacterSheet__concept']['klasa']
        self.__concept['gracz'] = json_object['_CharacterSheet__concept']['gracz']
        self.__attributes['krzepa'] = json_object['_CharacterSheet__attributes']['krzepa']
        self.__attributes['wytrzymałość'] = json_object['_CharacterSheet__attributes']['wytrzymałość']
        self.__attributes['zręczność'] = json_object['_CharacterSheet__attributes']['zręczność']
        self.__attributes['zmysły'] = json_object['_CharacterSheet__attributes']['zmysły']
        self.__attributes['intelekt'] = json_object['_CharacterSheet__attributes']['intelekt']
        self.__attributes['charakter'] = json_object['_CharacterSheet__attributes']['charakter']
        self.__skills['blef'] = json_object['_CharacterSheet__skills']['blef']
        self.__skills['empatia'] = json_object['_CharacterSheet__skills']['empatia']
        self.__skills['jeździectwo'] = json_object['_CharacterSheet__skills']['jeździectwo']
        self.__skills['leczenie'] = json_object['_CharacterSheet__skills']['leczenie']
        self.__skills['obycie'] = json_object['_CharacterSheet__skills']['obycie']
        self.__skills['perswazja'] = json_object['_CharacterSheet__skills']['perswazja']
        self.__skills['przetrwanie'] = json_object['_CharacterSheet__skills']['przetrwanie']
        self.__skills['rzemiosło'] = json_object['_CharacterSheet__skills']['rzemiosło']
        self.__skills['siła woli'] = json_object['_CharacterSheet__skills']['siła woli']
        self.__skills['skupienie'] = json_object['_CharacterSheet__skills']['skupienie']
        self.__skills['skradanie'] = json_object['_CharacterSheet__skills']['skradanie']
        self.__skills['spostrzegawczość'] = json_object['_CharacterSheet__skills']['spostrzegawczość']
        self.__skills['strzelectwo'] = json_object['_CharacterSheet__skills']['strzelectwo']
        self.__skills['walka'] = json_object['_CharacterSheet__skills']['walka']
        self.__skills['wykształcenie'] = json_object['_CharacterSheet__skills']['wykształcenie']
        self.__skills['wysportowanie'] = json_object['_CharacterSheet__skills']['wysportowanie']
        self.__skills['zastraszanie'] = json_object['_CharacterSheet__skills']['zastraszanie']
        self.__skills['złodziejstwo'] = json_object['_CharacterSheet__skills']['złodziejstwo']
        self.__skills['żegluga'] = json_object['_CharacterSheet__skills']['żegluga']
        self.__point_stats['pancerz'] = json_object['_CharacterSheet__point_stats']['pancerz']
        self.__point_stats['tarcza'] = json_object['_CharacterSheet__point_stats']['tarcza']
        self.__point_stats['broń'] = json_object['_CharacterSheet__point_stats']['broń']
        self.__point_stats['zdrowie'] = json_object['_CharacterSheet__point_stats']['zdrowie']
        self.__point_stats['energia'] = json_object['_CharacterSheet__point_stats']['energia']
        self.__point_stats['inicjatywa'] = json_object['_CharacterSheet__point_stats']['inicjatywa']
        self.__point_stats['szczęście'] = json_object['_CharacterSheet__point_stats']['szczęście']
        self.__point_stats['doświadczenie'] = json_object['_CharacterSheet__point_stats']['doświadczenie']
        self.__point_stats['atrybuty'] = json_object['_CharacterSheet__point_stats']['atrybuty']
        self.__point_stats['umiejętności'] = json_object['_CharacterSheet__point_stats']['umiejętności']
        self.__is_mage = json_object['_CharacterSheet__is_mage']
        return True
