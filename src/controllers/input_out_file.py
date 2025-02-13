import requests
import json
import os


def download_file(url_file: str) -> str:
    file_request = requests.get(url_file)
    if file_request.status_code == 200:
        file_name = url_file.split("/")[-1]
    print(f"Downloading: {file_name}")
    game_id = file_name.split("-")[-1].split(".")[0]
    with open("./data/games.json") as games_buffer:
        games_list = games_buffer.read()
        try:
            list_of_games = json.loads(games_list)
            file_name = f"{list_of_games[game_id]} {file_name.split('-')[0]}"
            file_path = f"./img/{list_of_games[game_id]}/{file_name}.jpg"
            try:
                os.makedirs(f"./img/{list_of_games[game_id]}")
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
    return f"./img/{file_name}"
