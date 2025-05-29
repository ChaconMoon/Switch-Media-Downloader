"""
Module: firefox.py.

Description: Firefox Integration with Selenium module
Author: Carlos Chacón
Date: 29-05-2025.
"""

# --- Import Selenium Dependecy ---
from selenium import webdriver

# --- Import WebBrowser Abstact Class ---
from switch_media_downloader.controllers.selenium.web_browser import WebBrowser

# --- Import String Localization Module ---
from switch_media_downloader.controllers.string_localization import StringLocalization


class Firefox(WebBrowser):
        """
        Class to Interact with the Firefox Browsing Using Selenium.

        Args:
                strat_selenium(): Open the Firefox Browser with the Switch Screenshot Site
                exit_selenium(): Close Firefox Browser.

        """

        options = webdriver.FirefoxOptions()

        def __init__(self):
                """Create a object to interact with the Firefox Browser."""
                self.options.add_argument("--no-sandbox")
                self.options.add_argument("--disable-dev-shm-usage")
                self.options.add_argument("--headless")
                self.driver = webdriver.Firefox(options=self.options)

        def start_selenium(self):
                """Open the Firefox Browser with Selenium on the Switch Screenshot site."""  # noqa: E501
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

        def exit_selenium(self):
                """Close Firefox Browser."""
                try:
                        print(
                                StringLocalization().get_localizated_string(
                                        "web_browser_exit_text"
                                )
                        )
                        self.driver.quit()
                        return True
                except Exception:  # noqa: BLE001
                        return False
