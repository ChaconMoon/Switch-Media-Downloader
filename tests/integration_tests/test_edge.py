from switch_media_downloader.controllers.selenium.edge import (
    start_selenium_connection_edge,
    exit_selenium_connection_edge,
)
from selenium.webdriver.edge.webdriver import WebDriver


def test_start_selenium_connection_edge():
    assert type(start_selenium_connection_edge()) is WebDriver


def test_exit_selenium_connection_edge():
    assert exit_selenium_connection_edge(start_selenium_connection_edge()) is True
