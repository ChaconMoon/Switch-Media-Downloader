"""
Module: downloads.py.

Description: Module to download files from the Nintendo Switch
Author: Carlos Chacón
Date: 29-05-2025.
"""

# --- Import Json Library ---
import json

# --- Import Pathlib Library ---
import pathlib

# --- Import Regular Expresions Library ---
import re

# --- Import files method of Pathlib
from importlib.resources import files

# --- Import web requests module ---
import requests

# --- Import module to name the download files ---
from switch_media_downloader.controllers.lenguages_settings_controller import (
        LenguagesController,
)
from switch_media_downloader.controllers.name_file_controller import (
        get_file_name,
        get_game_id,
)

# --- Import the Module to Translate the Program ---
from switch_media_downloader.controllers.string_localization import StringLocalization


def download_file(url_file: str) -> str:
        """
        Download a media file from the website and rename it.

        Args:
                url_file (str): the URL from the Downloable image.

        Returns:
                The downloaded image path

        """
        if url_file is not None:
                file_request = request_file(url_file)
                if file_request.status_code == 200:
                        file_name = get_file_name(url_file)
                        game_id = get_game_id(file_name)
                        extension = f"{file_name.split('.')[-1]}"
                        game_titles = files("switch_media_downloader").joinpath(
                                LenguagesController().set_game_title_string_file()
                        )
                        with pathlib.Path.open(
                                game_titles, encoding="utf-8"
                        ) as games_buffer:
                                games_list = games_buffer.read()
                                try:
                                        base_path = "/Screenshots/"
                                        if extension == "mp4":
                                                base_path = "/Video/"
                                        list_of_games = json.loads(games_list)
                                        game_name = f"{list_of_games[game_id]}"
                                        file_name = (
                                                f"{game_name} {file_name.split('-')[0]}"
                                        )
                                        game_name = re.sub(r"[/\\:*\"<>|]", "", game_name)
                                        file_name = re.sub(r"[/\\:*\"<>|]", "", file_name)

                                        home_path = pathlib.Path().home()
                                        file_path = (
                                                f"./Pictures/Nintendo Switch{base_path}"
                                                f"{game_name}"
                                        )

                                except KeyError:
                                        print(
                                                StringLocalization().get_localizated_string(
                                                        "hashtah_not_found_text"
                                                )
                                        )
                                        home_path = pathlib.Path().home()
                                        file_path = (
                                                f"./Pictures/Nintendo Switch{base_path}"
                                                f"{game_id}"
                                        )

                                output_path = home_path / file_path
                                output_path.mkdir(parents=True, exist_ok=True)
                        with pathlib.Path.open(
                                f"{output_path.absolute()}/{file_name}.{extension}", "wb"
                        ) as file:
                                file.write(file_request.content)
                                return f"{file_path}/{file_name}.{extension}"
                return None
        return None


def request_file(url_file: str) -> None | requests.Response:
        """
        Download a file and shows it.

        Args:
                url_file (str): The media Url on the web.

        """
        if url_file is not None:
                print(
                        StringLocalization()
                        .get_localizated_string("downloading_media_text")
                        .format(url_file)
                )
                return requests.get(url_file, timeout=10)
        return None


def get_absolute_path(relative_path: str):
        """
        Return the absolute path of a relative Path from the user folder.

        Args:
                relative_path: the path relative to the User Folder.

        """
        print(relative_path)
        relative_path = relative_path.replace("./", "/")
        home_path = str(pathlib.Path.home().absolute())
        full_path = home_path + relative_path
        return str(full_path)
