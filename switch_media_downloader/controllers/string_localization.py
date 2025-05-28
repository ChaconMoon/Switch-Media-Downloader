import json
from importlib.resources import files
from switch_media_downloader.controllers.lenguages_settings_controller import (
        LenguagesController,
        Lenguage,
)


class StringLocalization:
        _instance = None

        def get_localizated_string(self, string_id: str) -> str:
                return self.localizated_strings[string_id]

        def set_string_file(self):
                lenguages_controller = LenguagesController()
                if lenguages_controller.lang == Lenguage.ESP:
                        strings_file_path = files("switch_media_downloader").joinpath(
                                "data/strings_es.json"
                        )
                elif lenguages_controller.lang == Lenguage.ENG:
                        strings_file_path = files("switch_media_downloader").joinpath(
                                "data/strings_en.json"
                        )
                with open(strings_file_path, encoding="utf-8") as strings_paths:
                        self.localizated_strings = json.loads(strings_paths.read())

        def __new__(cls):
                if cls._instance is None:
                        cls._instance = super(StringLocalization, cls).__new__(cls)
                return cls._instance

        def __init__(self):
                self.set_string_file()
