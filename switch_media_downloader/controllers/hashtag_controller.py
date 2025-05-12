import json
from importlib.resources import files


def set_game_hashtag(game_id: str) -> str:
    game_hashtags = files("switch_media_downloader").joinpath(
        "data/game_hashtag_es.json"
    )
    try:
        with open(game_hashtags, encoding="utf-8") as game_hashtags:
            hashtag_list = json.loads(game_hashtags.read())
            return f"{hashtag_list[game_id]}"
    except KeyError:
        return None
