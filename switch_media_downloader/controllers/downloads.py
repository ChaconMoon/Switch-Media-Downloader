import json
import pathlib
import re
from importlib.resources import files

import requests

from switch_media_downloader.controllers.name_file_controller import (
        get_file_name,
        get_game_id,
)
from switch_media_downloader.controllers.string_localization import StringLocalization


def download_file(url_file: str) -> str:
        if url_file is not None:
                file_request = request_file(url_file)
                if file_request.status_code == 200:
                        file_name = get_file_name(url_file)
                        game_id = get_game_id(file_name)
                        extension = f"{file_name.split('.')[-1]}"
                        game_titles = files("switch_media_downloader").joinpath(
                                "data/game_data/game_titles_es.json"
                        )
                        with open(game_titles, encoding="utf-8") as games_buffer:
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
                                        file_path = f"./Pictures/Nintendo Switch{base_path}{game_name}"

                                except KeyError:
                                        print(
                                                StringLocalization().get_localizated_string(
                                                        "hashtah_not_found_text"
                                                )
                                        )
                                        home_path = pathlib.Path().home()
                                        file_path = f"./Pictures/Nintendo Switch{base_path}{game_id}"

                                output_path = home_path / file_path
                                output_path.mkdir(parents=True, exist_ok=True)
                        with open(
                                f"{output_path.absolute()}/{file_name}.{extension}", "wb"
                        ) as file:
                                file.write(file_request.content)
                                return f"{file_path}/{file_name}.{extension}"
                return None
        return None


def request_file(url_file: str):
        if url_file is not None:
                print(
                        StringLocalization()
                        .get_localizated_string("downloading_media_text")
                        .format(url_file)
                )
                return requests.get(url_file)
        return None


def get_absolute_path(relative_path: str):
        print(relative_path)
        relative_path = relative_path.replace("./", "/")
        home_path = str(pathlib.Path.home().absolute())
        full_path = home_path + relative_path
        return str(full_path)
