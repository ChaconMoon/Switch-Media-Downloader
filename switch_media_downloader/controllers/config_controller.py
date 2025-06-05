import configparser
from importlib.resources import files
from switch_media_downloader.controllers.selenium.firefox import Firefox
from switch_media_downloader.controllers.selenium.edge import Edge
from switch_media_downloader.controllers.selenium.web_browser import WebBrowser


def set_browser_to_web_scrapper() -> WebBrowser:
        config = configparser.ConfigParser()

        config_path = files("switch_media_downloader").joinpath("config.ini")
        config.read(config_path)

        web_scapper = config["config"]["web-scapper"]

        if web_scapper == "Edge":
                return Edge()
        if web_scapper == "Firefox":
                return Firefox()
        return Edge()
