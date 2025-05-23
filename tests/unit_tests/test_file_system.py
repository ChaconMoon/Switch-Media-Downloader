import pytest


@pytest.fixture
def test_download():
        from switch_media_downloader.controllers.downloads import download_file

        download_file()
