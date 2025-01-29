import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import requests


def connect_to_website_images():
    time.sleep(5)
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")
    driver = webdriver.Edge(options=options)
    driver.get("http://192.168.0.1/index.html")
    while driver.find_elements(By.TAG_NAME, "img") == []:
        time.sleep(0.1)
    images = driver.find_elements(By.TAG_NAME, "img")
    try:
        link_list = [img.get_attribute("src") for img in images]
    except Exception as e:
        print(e)
    finally:
        driver.quit()
        return link_list


def get_images(images_url: list[str]):
    for link in images_url:
        picture_test = requests.get(link)
        if picture_test.status_code == 200:
            picture_name = link.split("/")[-1]
            print(f"Downloading: {picture_name}")
            with open(f"./img/{picture_name}", "wb") as file:
                file.write(picture_test.content)
        pass
