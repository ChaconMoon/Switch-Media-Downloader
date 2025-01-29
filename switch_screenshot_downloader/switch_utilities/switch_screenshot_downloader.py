from switch_connection import (
    get_switch_network,
    connect_to_switch,
    disconnect_to_swicth,
)
from screenshot_downloader import connect_to_website_images, get_images


if __name__ == "__main__":
    wifi = get_switch_network()
    print(f"Wifi Switch = {wifi}")
    password = input("Contraseña Wifi Switch: ")
    if connect_to_switch(wifi, password):
        url_list = connect_to_website_images()
        try:
            if url_list is not None:
                get_images(url_list)
        finally:
            disconnect_to_swicth()
