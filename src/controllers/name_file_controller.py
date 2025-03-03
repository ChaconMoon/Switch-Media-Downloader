def get_game_id(file_name: str) -> str:
    return file_name.split("-")[-1].split(".")[0]


def get_file_name(url_file: str) -> str:
    return url_file.split("/")[-1]
