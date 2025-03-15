import re


def get_game_id(file_name: str) -> str:
    if re.search("\\d{16}-\\w{32}[.]{1}\\w{3}", file_name):
        return file_name.split("-")[-1].split(".")[0]


def get_file_name(url_file: str) -> str:
    if url_file is None:
        return None
    elif re.search(
        "^http:\/\/(([0-9]{1,3}\.){3}[0-9]{1,3}|([a-zA-Z0-9\-]+\.)+[a-zA-Z]{2,})/([a-zA-Z0-9\\-_]+)\\.([a-zA-Z0-9]+)",
        url_file,
    ):
        return url_file.split("/")[-1]
    else:
        return None
