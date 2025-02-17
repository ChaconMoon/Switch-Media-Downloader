from switch.connector import (
    get_switch_network,
    connect_to_switch,
    disconnect_to_swicth,
)
from switch.downloaders.image import (
    connect_to_website_images,
    get_switch_images,
)
from switch.downloaders.video import connect_to_website_video, get_video
from controllers.publish import selectAPIs


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
    can_publish = False
    wifi = get_switch_network()
    if wifi is not None:
        print(f"Wifi Switch = {wifi}")
        password = input("Contraseña Wifi Switch: ")

        if connect_to_switch(wifi, password):
            match input("Indique el contenido a descargar: (IMG/VIDEO)"):
                case "IMG":
                    url_list = connect_to_website_images()
                    try:
                        if url_list is not None:
                            photo_path = get_switch_images(url_list)
                            can_publish = True
                    except BaseException:
                        pass
                case "VIDEO":
                    link_video = connect_to_website_video()
                    try:
                        video_path = get_video(link_video)
                        can_publish = True
                    except BaseException:
                        pass
        else:
            print("No se ha podido descargar nada de la switch ")
        disconnect_to_swicth()
        if can_publish:
            # print(f"Se han descargado {len(url_list)} imagenes")
            match input("Quieres publicar la priemra captura: (y/n)"):
                case "y":
                    client = selectAPIs()
                    msg = input("Mensaje del post")
                    alt_text = ""
                    client.publish_video(msg=msg, file=video_path, alt_text=alt_text)
    else:
        print("No hay una red Wifi correspondiente a una Nintendo Switch")
