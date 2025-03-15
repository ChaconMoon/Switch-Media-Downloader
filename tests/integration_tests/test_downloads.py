from switch_media_downloader.controllers.downloads import download_file, request_file


def test_download_file_valid_image():
    assert download_file()


def test_download_file_valid_video():
    pass


def test_download_file_invalid():
    pass


def test_download_file_none():
    pass
