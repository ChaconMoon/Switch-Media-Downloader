from selenium import webdriver

from switch_media_downloader.controllers.selenium.web_browser import WebBrowser
from switch_media_downloader.controllers.string_localization import StringLocalization


class Firefox(WebBrowser):
        options = webdriver.FirefoxOptions()

        def __init__(self):
                self.options.add_argument("--no-sandbox")
                self.options.add_argument("--disable-dev-shm-usage")
                self.options.add_argument("--headless")
                self.driver = webdriver.Firefox(options=self.options)

        def start_selenium(self):
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
