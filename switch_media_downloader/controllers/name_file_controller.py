import re


def get_game_id(file_name: str) -> str:
        if re.search("\\d{16}-\\w{32}[.]{1}\\w{3}", file_name):
                return file_name.split("-")[-1].split(".")[0]
        return None


def get_file_name(url_file: str) -> str:
        if url_file is None:
                return None
        if (url_file.startswith(("http://", "https://"))) and (
                url_file.endswith((".mp4", ".jpg"))
        ):
                return url_file.split("/")[-1]
        return None
