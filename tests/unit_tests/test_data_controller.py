from switch_media_downloader.controllers.hashtag_controller import set_game_hashtag
from switch_media_downloader.controllers.name_file_controller import (
    get_file_name,
    get_game_id,
)


def test_hashtag_get_name():
    assert set_game_hashtag("B6CE40797459B0890BF7CEF68A4CE587") == "#PokemonViolet"


def test_hashtag_get_name_none():
    assert set_game_hashtag("B6CE40797459B0890BF7CEF68A4CE580") is None


def test_get_name():
    assert get_file_name("http://www.example.com/image.png") == "image.png"


def test_game_id():
    assert (
        get_game_id("2025030319095200-B6CE40797459B0890BF7CEF68A4CE587.jpg")
        == "B6CE40797459B0890BF7CEF68A4CE587"
    )
