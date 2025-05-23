from switch_media_downloader.switch.connector import (
        connect_to_switch,
        disconnect_to_swicth,
        get_switch_network,
)
from switch_media_downloader.switch.downloaders.image import (
        connect_to_website_images,
        get_switch_images,
)


def test_switch_search():
        assert get_switch_network() is not None


def test_connect_switch():
        assert (
                connect_to_switch(ssid=get_switch_network(), password="3qwty7e")
                is not False
        )


def test_switch_screenshots_downloads():
        assert get_switch_images(connect_to_website_images()) is not None


def test_disconnect_switch():
        assert disconnect_to_swicth() is True
