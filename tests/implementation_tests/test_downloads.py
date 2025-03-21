from switch_media_downloader.controllers.downloads import download_file, request_file
from switch.downloaders.image import get_switch_images


def test_download_file_valid_image():
    image_list = list()
    image_list.append(
        "https://raw.githubusercontent.com/ChaconMoon/TESTING/main/Switch_Media_Downloader/2024100319575600-DB679239AE5C0DC0D5E47C22D6492D98.jpg"
    )
    photo_path = get_switch_images(image_list)
    assert (
        photo_path
        == "./Pictures/Nintendo Switch/Screenshots/WarioWare Move It!/WarioWare Move It! 2024100319575600.jpg"
    )


def test_download_file_invalid_image():
    assert (
        download_file(
            "https://raw.githubusercontent.com/ChaconMoon/TESTING/main/Switch_Media_Downloader/2024100319575600-DB679239DC0D5E47C22D6492D98.jpg"
        )
        is None
    )


def test_download_file_invalid_video():
    assert (
        download_file(
            "https://github.com/ChaconMoon/Switch-Media-Downloader/blob/master/tests/test_media/nothing.mp4"
        )
        is None
    )


def test_download_file_none():
    download_file(None) is None


def test_request_file_invalid_file():
    assert (
        request_file(
            "https://github.com/ChaconMoon/Switch-Media-Downloader/blob/master/tests/test_media/2024100319575600-nothing.jpg"
        ).status_code
        == 404
    )


def test_request_file_none():
    assert request_file(None) is None
