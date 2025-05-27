from switch_media_downloader.controllers.name_file_controller import (
        get_file_name,
        get_game_id,
)

# GET_FILE_NAME

# VALID NAME TEST


def test_get_file_valid_name_image():
        assert get_file_name("http://192.0.0.1/image.jpg") == "image.jpg"


def test_get_file_valid_name_video():
        assert get_file_name("http://192.0.0.1/video.mp4") == "video.mp4"


def test_get_file_invalid_name_image_github():
        assert (
                get_file_name(
                        "https://github.com/ChaconMoon/Switch-Media-Downloader/blob/master/tests/test_media/2024100319575600-DB679239AE5C0DC0D5E47C22D6492D98.jpg"
                )
                == "2024100319575600-DB679239AE5C0DC0D5E47C22D6492D98.jpg"
        )

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
                get_game_id("2024100319575600-DB679239AE5C0DC0D5E47C22D6492D98.jpg")
                == "DB679239AE5C0DC0D5E47C22D6492D98"
        )


# INVALID ID TEST
def test_game_id_none_name():
        assert get_game_id("2025030319095200") is None
