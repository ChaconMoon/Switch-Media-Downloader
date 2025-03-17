import time
from selenium.webdriver.common.by import By
from controllers.selenium.firefox import Firefox
from controllers.downloads import download_file


def connect_to_website_images():
    time.sleep(5)

    web_scrapper = Firefox()
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


def get_switch_images(images_url_list: list[str]):
    images_files = []
    try:
        for url_image in images_url_list:
            images_files.append(download_file(url_image))
        return images_files
    except OSError as e:
        print(e)
        print("Error en la obtención de la imagen.")
        return None
    except BlockingIOError:
        print("Error en la escritura de la imagen")
        return None
