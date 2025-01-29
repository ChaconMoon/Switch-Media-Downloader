from switch_utilities.switch_connection import (
    get_switch_network,
    connect_to_switch,
    disconnect_to_swicth,
)
from switch_utilities.screenshot_downloader import connect_to_website_images, get_images
from bluesky_API.bluesky_api import publish_photo


if __name__ == "__main__":
    wifi = get_switch_network()
    print(f"Wifi Switch = {wifi}")
    password = input("Contraseña Wifi Switch: ")
    if connect_to_switch(wifi, password):
        url_list = connect_to_website_images()
        try:
            if url_list is not None:
                photo_path = get_images(url_list)
        finally:
            disconnect_to_swicth()

        match input("Quieres publicar esta captura: (y/n)"):
            case "y":
                publish_photo(
                    msg="Esta imagen sirve para probar si puedo publicar una imagen con su relación de aspecto correcta",
                    file=photo_path,
                    alt_text="Foto con mi novio en la academia púrpura",
                )
