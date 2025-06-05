import pathlib
import time

from selenium.webdriver.common.by import By

from switch_media_downloader.controllers.downloads import download_file
from switch_media_downloader.controllers.string_localization import StringLocalization
from switch_media_downloader.controllers.config_controller import (
        set_browser_to_web_scrapper,
)


def connect_to_website_images():
        time.sleep(5)

        web_scrapper = set_browser_to_web_scrapper()
        web_scrapper.start_selenium()
        driver = web_scrapper.driver
        while driver.find_elements(By.TAG_NAME, "img") == []:
                time.sleep(0.1)
        images = driver.find_elements(By.TAG_NAME, "img")
        try:
                link_list = [img.get_attribute("src") for img in images]
        except Exception as e:
                print(e)
        finally:
                web_scrapper.exit_selenium()
        return link_list


def get_switch_images(images_url_list: list[str]) -> list[str]:
        images_files = []
        number_of_images = 0
        try:
                for url_image in images_url_list:
                        images_files.append(get_image(url_image))
                        if number_of_images < 4:
                                number_of_images += 1
                return images_files[0:number_of_images]
        except OSError as e:
                print(e)
                print(
                        StringLocalization().get_localizated_string(
                                "image_downloading_error_text"
                        )
                )
                return None
        except BlockingIOError:
                print(
                        StringLocalization().get_localizated_string(
                                "image_writting_error_text"
                        )
                )
                return None


def get_image(url_video: str):
        home_path = str(pathlib.Path.home().absolute())
        return home_path + download_file(url_video).replace("./", "/")
