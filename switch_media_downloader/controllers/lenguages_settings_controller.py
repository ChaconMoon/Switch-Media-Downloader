from enum import Enum
import configparser
from importlib.resources import files
import os


class Lenguage(Enum):
        ESP = 1
        ENG = 2


class LenguagesController:
        _instance = None

        def __new__(cls):
                if cls._instance is None:
                        cls._instance = super().__new__(cls)
                return cls._instance

        def __init__(self):
                self.strings_file = ""
                self.set_localization_lenguage()

        def set_localization_lenguage(self):
                config = configparser.ConfigParser()

                config_path = files("switch_media_downloader").joinpath("config.ini")
                config.read(config_path)

                localization = config["config"]["language"]

                if localization == "ESP":
                        self.lang = Lenguage.ESP
                elif localization == "ENG":
                        self.lang = Lenguage.ENG
                else:
                        self.lang = Lenguage.ENG

        def set_game_title_string_file(self):
                """Return the file path for game titles based on the selected language."""
                match self.lang:
                        case Lenguage.ENG:
                                return "data/game_data/game_titles_en.json"
                        case Lenguage.ESP:
                                return "data/game_data/game_titles_es.json"

        def set_game_hashtag_string_file(self):
                """Return the file path for game hashtag based on the selected language."""  # noqa: E501
                match self.lang:
                        case Lenguage.ENG:
                                return "data/game_data/game_hashtag_en.json"
                        case Lenguage.ESP:
                                return "data/game_data/game_hashtag_es.json"
