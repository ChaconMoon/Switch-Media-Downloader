"""
Module: edge.py.

Description: Edge Integration with Selenium module
Author: Carlos Chacón
Date: 29-05-2025.
"""

# --- Import Selenium Dependecies ---
from selenium import webdriver
from selenium.webdriver.edge.webdriver import WebDriver

# --- Import WebBrowser Abstact Class ---
from switch_media_downloader.controllers.selenium.web_browser import WebBrowser

# --- Import String Localization Module ---
from switch_media_downloader.controllers.string_localization import StringLocalization


class Edge(WebBrowser):
        """
        Class to Interact with the Edge Browsing Using Selenium.

        Args:
                strat_selenium(): Open the Edge Browser with the Switch Screenshot Site
                exit_selenium(): Close Edge Browser.

        """

        options = webdriver.EdgeOptions()

        def __init__(self):
                """Create a object to interact with the Edge Browser."""
                self.options.add_argument("--no-sandbox")
                self.options.add_argument("--disable-dev-shm-usage")
                self.options.add_argument("--headless")
                self.driver = webdriver.Edge(options=self.options)

        def start_selenium(self) -> WebDriver:
                """Open the Edge Browser with Selenium on the Switch Screenshot site."""
                try:
                        self.driver.get("http://192.168.0.1/index.html")
                        print(
                                StringLocalization().get_localizated_string(
                                        "web_browser_open_text"
                                )
                        )
                        return True
                except Exception as e:
                        raise e

        def exit_selenium(self) -> bool:
                """Close Edge Browser."""
                try:
                        print(
                                StringLocalization().get_localizated_string(
                                        "web_browser_exit_text"
                                )
                        )
                        self.driver.quit()
                        return True
                except Exception:
                        return False
