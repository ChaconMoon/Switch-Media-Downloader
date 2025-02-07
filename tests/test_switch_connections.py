import pytest
from src.switch.connector import (
    connect_to_switch,
    get_switch_network,
    disconnect_to_swicth,
)
from src.switch.downloaders.image import (
    connect_to_website_images,
    get_switch_images,
)


def test_switch_search():
    assert get_switch_network() is not None


def test_connect_switch():
    assert (
        connect_to_switch(ssid=get_switch_network(), password="4qqwwgnh") is not False
    )


def test_switch_screenshots_downloads():
    assert get_switch_images(connect_to_website_images()) is not None


def test_disconnect_switch():
    assert disconnect_to_swicth() is True
