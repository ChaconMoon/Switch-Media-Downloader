import requests
import json
import pathlib
import re
from controllers.name_file_controller import get_game_id, get_file_name


def download_file(url_file: str) -> str:
    if url_file is not None:
        file_request = request_file(url_file)
        if file_request.status_code == 200:
            file_name = get_file_name(url_file)
            game_id = get_game_id(file_name)
            extension = f"{file_name.split('.')[-1]}"
            with open("./data/game_titles.json", encoding="utf-8") as games_buffer:
                games_list = games_buffer.read()
                try:
                    base_path = "/Screenshots/"
                    if extension == "mp4":
                        base_path = "/Video/"
                    list_of_games = json.loads(games_list)
                    game_name = f"{list_of_games[game_id]}"
                    file_name = f"{game_name} {file_name.split('-')[0]}"
                    game_name = re.sub(r"[/\\:*\"<>|]", "", game_name)
                    file_name = re.sub(r"[/\\:*\"<>|]", "", file_name)

                    home_path = pathlib.Path().home()
                    file_path = f"./Pictures/Nintendo Switch{base_path}{game_name}"

                except KeyError:
                    print("Ese ID no esta en la lista, se usara el nombre por defecto.")
                    home_path = pathlib.Path().home()
                    file_path = f"./Pictures/Nintendo Switch{base_path}{game_id}"

                output_path = home_path / file_path
                output_path.mkdir(parents=True, exist_ok=True)
            with open(
                f"{output_path.absolute()}/{file_name}.{extension}", "wb"
            ) as file:
                file.write(file_request.content)
                return f"{file_path}/{file_name}.{extension}"
    else:
        return None


def request_file(url_file: str):
    if url_file is not None:
        print(f"Downloading: {url_file}")
        return requests.get(url_file)
    else:
        return None


def get_absolute_path(relative_path: str):
    home_path = pathlib.Path().home()
    full_path = home_path / relative_path
    return str(full_path)
