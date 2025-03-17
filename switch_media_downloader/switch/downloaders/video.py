import time
from selenium.webdriver.common.by import By
from controllers.downloads import download_file
from controllers.selenium.firefox import Firefox


def connect_to_website_video():
    time.sleep(5)
    web_scrapper = Firefox()
    web_scrapper.start_selenium()
    driver = web_scrapper.driver
    while driver.find_elements(By.TAG_NAME, "source") == []:
        time.sleep(0.1)
    video = driver.find_elements(By.TAG_NAME, "source")[0]
    try:
        link_video = video.get_attribute("src")
    except Exception as e:
        print(e)
        return None
    finally:
        web_scrapper.exit_selenium(driver)
        return link_video


def get_video(url_video: str):
    return download_file(url_video)
