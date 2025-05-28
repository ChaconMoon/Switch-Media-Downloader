from enum import Enum
import configparser
import os


class Lenguage(Enum):
        ESP = 1
        ENG = 2


class LenguagesController:
        _instance = None

        def __new__(cls):
                if cls._instance is None:
                        cls._instance = super(LenguagesController, cls).__new__(cls)
                return cls._instance

        def __init__(self):
                self.strings_file = ""
                self.set_localization_lenguage()

        def set_localization_lenguage(self):
                config = configparser.ConfigParser()

                base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                config_path = os.path.join(base_dir, "config.ini")
                config.read(config_path)

                localization = config["config"]["language"]

                if localization == "ESP":
                        self.lang = Lenguage.ESP
                elif localization == "ENG":
                        self.lang = Lenguage.ENG
                else:
                        self.lang = Lenguage.ENG

        def set_program_string_file(self, idiom_id: int):
                match idiom_id:
                        case 1:
                                self.strings_file = "data/strings_en.json"
                        case 2:
                                self.strings_file = "data/strings_es.json"

        def set_game_title_string_file(self, idiom_id):
                match idiom_id:
                        case 1:
                                return "data/game_data/game_titles_en.json"
                        case 2:
                                return "data/game_data/game_titles_es.json"

        def set_game_hashtag_string_file(self, idiom_id):
                match idiom_id:
                        case 1:
                                return "data/game_data/game_hashtag_en.json"
                        case 2:
                                return "data/game_data/game_hashtag_es.json"
