from switch_modules.switch_connection import (
    get_switch_network,
    connect_to_switch,
    disconnect_to_swicth,
)
from switch_modules.screenshot_downloader import connect_to_website_images, get_images
from APIs_Modules.bluesky_api import publish_image, connect_bluesky


def display_logo():
    print("     ╭───┐┌─────────────────────────┐┌───╮")
    print(
        "     │   │ │ ┌───────────────────┐ │ │ o │  __          _ _       _       __                              _           _        ___                      __                 _           "
    )
    print(
        "     │ O │ │ │                   │ │ │o o│ / _\\_      _(_) |_ ___| |__   / _\\ ___ _ __ ___  ___ _ __  ___| |__   ___ | |_     /   \\_____      ___ __   / /  ___   __ _  __| | ___ _ __ "
    )
    print(
        "     │ o │ │ │         |>        │ │ │ o │ \\ \\ \\ /\\ /  / | __/ __| '_ \\  \\ \\ / __| '__/ _ \\/ _ \\ '_ \\/ __| '_ \\ / _ \\| __|   / /\\ / _ \\ \\ /\\ / / '_ \\ / /  / _ \\ / _` |/ _` |/ _ \\ '__|"
    )
    print(
        "     │o o│ │ │                   │ │ │ O │ _\\ \\ V  V  /| | || (__| | | | _\\ \\ (__| | |  __/  __/ | | \\__ \\ | | | (_) | |_   / /_// (_) \\ V  V /| | | / /__| (_) | (_| | (_| |  __/ |   "
    )
    print(
        "     │ o │ │ └───────────────────┘ │ │   │ \\__/ \\_/\\_/ |_|\\__\\___|_| |_| \\__/\\___|_|  \\___|\\___|_| |_|___/_| |_|\\___/ \\__| /___,' \\___/ \\_/\\_/ |_| |_\\____/\\___/ \\__,_|\\__,_|\\___|_|   "
    )
    print("     ╰───┘└─────────────────────────┘└───╯\n")


if __name__ == "__main__":
    display_logo()
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
                publish_image(
                    msg="Esta imagen sirve para probar si puedo publicar una imagen con su relación de aspecto correcta",
                    file=photo_path,
                    alt_text="Esto es solo otra prueba",
                    client=connect_bluesky(),
                )
