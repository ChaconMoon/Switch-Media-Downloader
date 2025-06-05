"""
Module: hashtag_controller.py.

Description: Module that get the Hashtag of a Game using they ID
Author: Carlos Chacón
Date: 29-05-2025.
"""

# --- Import Json Module ---
import json

# --- Import importlib resources ---
from importlib.resources import files

# --- Import Pathlib library ---
from pathlib import Path

# --- Import Localization Module ---
from switch_media_downloader.controllers.lenguages_settings_controller import (
        LenguagesController,
)


def set_game_hashtag(game_id: str) -> str | None:
        """
        Return the Hashtag of a Game if it Exists.

        Args:
                game_id (str): The id of the game.

        """
        game_hashtags = files("switch_media_downloader").joinpath(
                LenguagesController().set_game_hashtag_string_file()
        )
        try:
                with Path.open(game_hashtags, encoding="utf-8") as game_hashtags:
                        hashtag_list = json.loads(game_hashtags.read())
                        return f"{hashtag_list[game_id]}"
        except KeyError:
                return None
