from switch.connector import (
    get_switch_network,
    connect_to_switch,
    disconnect_to_swicth,
)
from switch.downloaders.image import (
    connect_to_website_images,
    get_switch_images,
)
from controllers.hashtag_controller import set_game_hashtag
from controllers.name_file_controller import get_file_name, get_game_id

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
                            reference_url = url_list[0]
                            can_publish = True
                    except BaseException:
                        pass
                    disconnect_to_swicth()
                    if can_publish:
                        print(f"Se han descargado {len(url_list)} imagenes")
                        match input("Quieres publicar esta imagen: (y/n)"):
                            case "y":
                                client = selectAPIs()
                                msg = input("Mensaje del post: ")
                                game_hashtag = set_game_hashtag(
                                    get_game_id(get_file_name(reference_url))
                                )
                                if game_hashtag is not None:
                                    if (
                                        input(
                                            f"Se ha encontrado el siguiente hashtag {game_hashtag} ¿Quieres usarlo? y/n"
                                        )
                                        == "y"
                                    ):
                                        msg += f" {game_hashtag}"

                                alt_text = ""
                                client.publish_image(
                                    msg=msg, file=photo_path[0], alt_text=alt_text
                                )
                case "VIDEO":
                    link_video = connect_to_website_video()
                    try:
                        video_path = get_video(link_video)
                        reference_url = link_video
                        can_publish = True
                    except BaseException:
                        pass
                    disconnect_to_swicth()
                    if can_publish:
                        match input("Quieres publicar este video: (y/n)"):
                            case "y":
                                client = selectAPIs()
                                msg = input("Mensaje del post: ")
                                game_hashtag = set_game_hashtag(
                                    get_game_id(get_file_name(reference_url))
                                )
                                if game_hashtag is not None:
                                    if (
                                        input(
                                            f"Se ha encontrado el siguiente hashtag {game_hashtag} ¿Quieres usarlo? y/n"
                                        )
                                        == "y"
                                    ):
                                        msg += f" {game_hashtag}"

                                alt_text = ""
                                client.publish_video(
                                    msg=msg, file=video_path, alt_text=alt_text
                                )
        else:
            print("No se ha podido descargar nada de la switch ")
    else:
        print("No hay una red Wifi correspondiente a una Nintendo Switch")
