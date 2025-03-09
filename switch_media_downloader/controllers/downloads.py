import requests
import json
import os
import re
from controllers.name_file_controller import get_game_id, get_file_name


def download_file(url_file: str) -> str:
    file_request = request_file(url_file)
    if file_request.status_code == 200:
        file_name = get_file_name(url_file)
    game_id = get_game_id(file_name)
    extension = f"{file_name.split('.')[-1]}"
    with open("./data/game_titles.json", encoding="utf-8") as games_buffer:
        games_list = games_buffer.read()
        try:
            base_path = "./img/"
            if extension == "mp4":
                base_path = "./video/"
            list_of_games = json.loads(games_list)
            game_name = f"{list_of_games[game_id]}"
            file_name = f"{game_name} {file_name.split('-')[0]}"
            game_name = re.sub(r"[/\\:*\"<>|]", "", game_name)
            file_name = re.sub(r"[/\\:*\"<>|]", "", file_name)

            file_path = f"{base_path}{game_name}/{file_name}.{extension}"
            try:
                os.makedirs(base_path)
            except FileExistsError:
                pass
            try:
                os.makedirs(f"{base_path}{game_name}")
            except FileExistsError:
                pass
        except KeyError:
            print("Ese ID no esta en la lista, se usara el nombre por defecto.")
            try:
                os.makedirs(f"{base_path}{game_id}/".encode())
            except FileExistsError:
                pass
            file_path = f"{base_path}{game_id}/{file_name}".encode()
    with open(file_path, "wb") as file:
        file.write(file_request.content)
    return file_path


def request_file(url_file: str):
    print(f"Downloading: {url_file}")
    return requests.get(url_file)
