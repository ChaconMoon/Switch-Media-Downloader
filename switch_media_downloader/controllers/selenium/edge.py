from selenium import webdriver
from selenium.webdriver.edge.webdriver import WebDriver


def start_selenium_connection_edge() -> WebDriver:
    try:
        options = webdriver.EdgeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--headless")
        driver = webdriver.Edge(options=options)
        driver.get("http://192.168.0.1/index.html")
        print("Open Web Browser")
        return driver
    except Exception as e:
        raise e
        return None


def exit_selenium_connection_edge(driver: WebDriver) -> bool:
    try:
        print("Exit Web Browser")
        driver.quit()
        return True
    except Exception:
        return False
