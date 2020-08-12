import json
import random
import re
from enum import Enum

import utils.rtext
from utils import rtext


class ItemStack:
    def __init__(self, material, number):
        self.material = material
        self.number = number
        self.meta = ItemMeta()

    def get_material(self):
        return self.materia

    def set_material(self, material):
        self.material = material
        return self

    def get_number(self):
        return self.number

    def set_number(self, number):
        if type(number) == int:
            if number > 0:
                self.number = number
                return self
            else:
                raise ValueError("invalid value for set_number() with '" + str(number) + "'")
        raise TypeError("set_number() argument must be a int, not '" + str(type(number)) + "'")

    def get_meta(self):
        return self.meta

    def set_meta(self, meta):
        if type(meta) == ItemMeta:
            self.meta = meta
            return self
        raise TypeError("set_meta() argument must be a ItemMeta, not '" + str(type(meta)) + "'")

    def give(self, server, player):
        print ("give {0} {1}{2} {3}".format(player, self.material, self.meta.to_nbt_string().replace("\\", "\\\\"), str(self.number)))
        server.execute("give {0} {1}{2} {3}".format(player, self.material, self.meta.to_nbt_string().replace("\\", "\\\\"), str(self.number)))


class ItemMeta:
    def __init__(self):
        self.nbt = {}

    def get_enchantments(self):
        if "Enchantments" in self.nbt.keys():
            return self.nbt["Enchantments"]
        return ""

    def set_enchantments(self, enchantments):
        if type(enchantments) == list:
            self.nbt["Enchantments"] = enchantments
        elif type(enchantments) == dict:
            self.nbt["Enchantments"] = [enchantments]
        else:
            raise TypeError("set_enchantments() argument must be a dict or a list, not '" + str(type(enchantments)) + "'")
        return self

    def add_enchantments(self, enchantment, level):
        if type(enchantment) != Enchantment:
            raise TypeError("enchantment argument must be a Enchantment, not '" + str(type(enchantment)) + "'")
        if type(level) != int:
            raise TypeError("level argument must be a int, not '" + str(type(enchantment)) + "'")
        if level <= 0:
            raise ValueError("invalid value for level argument with '" + str(level) + "'")

        if "Enchantments" in self.nbt.keys():
            if type(self.nbt["Enchantments"]) == list:
                self.nbt["Enchantments"].append({"id": enchantment, "lvl": level})
            else:
                self.nbt["Enchantments"] = [{"id": enchantment, "lvl": level}]
        else:
            self.nbt["Enchantments"] = [{"id": enchantment, "lvl": level}]
        return self

    def get_display_name(self):
        try:
            return self.nbt["display"]["Name"]
        except:
            self.nbt["display"] = {}
            self.nbt["display"]["Name"] = []
            return []

    def set_display_name(self, name):
        if "display" not in self.nbt.keys():
            self.nbt["display"] = {}
        if type(name) == str:
            self.nbt["display"]["Name"] = [{"text": name}]
        elif isinstance(name, rtext.RTextBase):
            self.nbt["display"]["Name"] = name.to_json_object()
        else:
            raise TypeError("name argument must be a str or RTextBase, not '" + str(type(name)) + "'")
        return self

    def get_lore(self):
        try:
            return self.nbt["display"]["Lore"]
        except:
            self.nbt["display"] = {}
            self.nbt["display"]["Lore"] = []
            return []

    def set_lore(self, lines):
        if "display" not in self.nbt.keys():
            self.nbt["display"] = {}
        if type(lines) == list:
            lines2 = []
            for l in lines:
                if isinstance(l, rtext.RTextBase):
                    lines2.append(l.to_json_object())
                else:
                    lines2.append(l)
            self.nbt["display"]["Lore"] = lines2
        elif isinstance(lines, rtext.RTextBase):
            self.nbt["display"]["Lore"] = [lines.to_json_object()]
        else:
            raise TypeError("name argument must be a str or RTextBase, not '" + str(type(lines)) + "'")
        return self

    def to_nbt_string(self):
        result = json.dumps(self.nbt, cls=JsonCustomEncoder)

        # 处理屑mojang的物品名单引号
        if "display" in self.nbt.keys():
            if "Name" in self.nbt["display"].keys():
                result = result.replace('"' + json.dumps(self.nbt["display"]["Name"], ensure_ascii=False) + '"', "'" + json.dumps(self.nbt["display"]["Name"], ensure_ascii=False) + "'")
            if "Lore" in self.nbt["display"].keys():
                result = result.replace('"' + json.dumps(self.nbt["display"]["Name"], ensure_ascii=False) + '"', "'" + json.dumps(self.nbt["display"]["Lore"], ensure_ascii=False) + "'")
        return result


class Enchantment(Enum):
    AQUA_AFFINITY = "aqua_affinity"
    BANE_OF_ARTHROPODS = "bane_of_arthropods"
    BLAST_PROTECTION = "blast_protection"
    CHANNELI = "channeli"
    CHOPPING = "chopping"
    CURSE_OF_BINDING = "curse_of_binding"
    CURSE_OF_VANISHING = "curse_of_vanishing"
    DEPTH_STRIDER = "depth_strider"
    EFFICIENCY = "efficiency"
    FEATHER_FALLING = "feather_falling"
    FIRE_ASPECT = "fire_aspect"
    FIRE_PROTECTION = "fire_protection"
    FLAME = "flame"
    FORTUNE = "fortune"
    FROST_WALKER = "frost_walker"
    IMPALING = "impaling"
    INFINITY = "infinity"
    KNOCKBACK = "knockback"
    LOOTING = "looting"
    LOYALTY = "loyalty"
    LUCK_OF_THE_SEA = "luck_of_the_sea"
    LURE = "lure"
    MENDING = "mending"
    MULTISHOT = "multishot"
    PIERCING = "piercing"
    POWER = "power"
    PROJECTILE_PROTECTION = "projectile_protection"
    PROTECTION = "protection"
    PUNCH = "punch"
    QUICK_CHARGE = "quick_charge"
    RESPIRATION = "respiration"
    RIPTIDE = "riptide"
    SHARPNESS = "sharpness"
    SILK_TOUCH = "silk_touch"
    SMITE = "smite"
    SOUL_SPEED = "soul_speed"
    SWEEPING_EDGE = "sweeping_edge"
    THORNS = "thorns"
    UNBREAKING = "unbreaking"


class JsonCustomEncoder(json.JSONEncoder):
    def default(self, field):
        if type(field) == Enchantment:
            return field.value
        else:
            return json.JSONEncoder.default(self, field)
