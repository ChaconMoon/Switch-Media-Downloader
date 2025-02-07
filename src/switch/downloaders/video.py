import time
from selenium.webdriver.common.by import By
from controllers.input_out_file import download_file
from controllers.selenium.edge import (
    start_selenium_connection_edge,
    exit_selenium_connection_edge,
)


def connect_to_website_video():
    time.sleep(5)
    driver = start_selenium_connection_edge()
    while driver.find_element(By.TAG_NAME, "video") is None:
        time.sleep(0.1)
        video = driver.find_element(By.TAG_NAME, "video")
    try:
        link_video = video.get_attribute("src")
    except Exception as e:
        print(e)
        return None
    finally:
        exit_selenium_connection_edge(driver)
        return link_video


def get_video(url_video: str):
    download_file(url_video)
