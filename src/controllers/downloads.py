import requests
import json
import os
import re


def download_file(url_file: str) -> str:
    print(f"Downloading: {url_file}")
    file_request = requests.get(url_file)
    if file_request.status_code == 200:
        file_name = url_file.split("/")[-1]
    game_id = file_name.split("-")[-1].split(".")[0]
    extension = f"{file_name.split('.')[-1]}"
    with open("./data/game_titles.json") as games_buffer:
        games_list = games_buffer.read()
        try:
            list_of_games = json.loads(games_list)
            game_name = f"{list_of_games[game_id]}"
            file_name = f"{game_name} {file_name.split('-')[0]}"
            game_name = re.sub(r"[/\\:*\"<>|]", "", game_name)
            file_name = re.sub(r"[/\\:*\"<>|]", "", file_name)
            file_path = f"./img/{game_name}/{file_name}.{extension}"
            try:
                os.makedirs("./img/")
            except FileExistsError:
                pass
            try:
                os.makedirs(f"./img/{game_name.replace(':', '')}")
            except FileExistsError:
                pass
        except KeyError:
            print("Ese ID no esta en la lista, se usara el nombre por defecto.")
            try:
                os.makedirs(f"./img/{game_id}/")
            except FileExistsError:
                pass
            file_path = f"./img/{game_id}/{file_name}"
    with open(file_path, "wb") as file:
        file.write(file_request.content)
    return file_path
