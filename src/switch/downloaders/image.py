import time
from selenium.webdriver.common.by import By
from controllers.selenium.edge import (
    start_selenium_connection_edge,
    exit_selenium_connection_edge,
)
from controllers.input_out_file import download_file


def connect_to_website_images():
    time.sleep(5)
    driver = start_selenium_connection_edge()
    while driver.find_elements(By.TAG_NAME, "img") == []:
        time.sleep(0.1)
    images = driver.find_elements(By.TAG_NAME, "img")
    try:
        link_list = [img.get_attribute("src") for img in images]
    except Exception as e:
        print(e)
    finally:
        exit_selenium_connection_edge(driver)
        return link_list


def get_switch_images(images_url_list: list[str]):
    try:
        for url_image in images_url_list:
            download_file(url_image)
        return True
    except OSError:
        print("Error en la obtención de la escritura de la imagen.")
        return None
    except BlockingIOError:
        print("Error en la escritura de la imagen")
        return None
