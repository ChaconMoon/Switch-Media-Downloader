import json


def set_game_hashtag(game_id: str) -> str:
    try:
        with open("../data/game_hashtag_es.json") as game_hashtags:
            hashtag_list = json.loads(game_hashtags.read())
            return f"{hashtag_list[game_id]}"
    except KeyError:
        return None
