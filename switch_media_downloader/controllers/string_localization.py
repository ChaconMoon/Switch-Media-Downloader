import os
import pandas as pd
from importlib.resources import files
from switch_media_downloader.controllers.lenguages_settings_controller import (
        LenguagesController,
        Lenguage,
)


class StringLocalization:
        _instance = None

        def get_localizated_string(self, string_id: str) -> str:
                return self.localizated_strings[string_id, self.actual_localization]

        def set_string_file(self):
                base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                csv_path = os.path.join(base_dir, "data", "program_strings.csv")
                strings_data_frame = pd.read_csv(csv_path)
                strings_data_frame.set_index("COLUM_ID", inplace=True)
                self.localizated_strings = strings_data_frame.loc
                lenguages_controller = LenguagesController()
                if lenguages_controller.lang == Lenguage.ESP:
                        self.actual_localization = "ESP"
                elif lenguages_controller.lang == Lenguage.ENG:
                        self.actual_localization = "ENG"

        def __new__(cls):
                if cls._instance is None:
                        cls._instance = super().__new__(cls)
                return cls._instance

        def __init__(self):
                self.set_string_file()
