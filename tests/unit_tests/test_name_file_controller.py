from switch_media_downloader.controllers.name_file_controller import (
    get_file_name,
    get_game_id,
)

# GET_FILE_NAME

# VALID NAME TEST


def test_get_file_valid_name_image():
    assert get_file_name("http://192.0.0.1/image.png") == "image.png"


def test_get_file_valid_name_video():
    assert get_file_name("http://192.0.0.1/video.mp4") == "video.mp4"

    # INVALID NAME TEST


def test_get_file_invalid_name_image():
    assert get_file_name("image.png") is None


def test_get_file_invalid_name_video():
    assert get_file_name("video.mp4") is None


def test_get_file_invalid_no_name():
    assert get_file_name("http://192.0.0.1/") is None

    # NULL TEST


def test_get_file_null_name():
    assert get_file_name(None) is None


# GET_GAME_ID


# VALID ID TEST
def test_game_id_valid_name():
    assert (
        get_game_id("2025030319095200-B6CE40797459B0890BF7CEF68A4CE587.jpg")
        == "B6CE40797459B0890BF7CEF68A4CE587"
    )


# INVALID ID TEST
def test_game_id_none_name():
    assert get_game_id("2025030319095200") is None
