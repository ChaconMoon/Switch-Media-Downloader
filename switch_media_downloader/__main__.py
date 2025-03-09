"""
Module: __main__.py
Description: Module that starts the Switch Media Downloader
Author: Carlos Chacón
Date: 09-03-2025
"""

# --- Standard Dependence ---
from enum import Enum

# --- Connect to switch Dependence ---
from switch.connector import (
    get_switch_network,
    connect_to_switch,
    disconnect_to_swicth,
)

# --- Get switch images Dependence ---
from switch.downloaders.image import (
    connect_to_website_images,
    get_switch_images,
)

# --- Hashtag of the games Dependence ---
from controllers.hashtag_controller import set_game_hashtag

# --- Get media info Dependence ---
from controllers.name_file_controller import get_file_name, get_game_id

# --- Get switch video Dependence ---
from switch.downloaders.video import connect_to_website_video, get_video

# --- Get APIs Dependence ---
from controllers.publish import selectAPIs


class TypeMedia(Enum):
    """Defines the names used to reference the type of media that will be download as a Enum
    Args:
        VIDEO (1): Download/Publish a video
        IMAGE (2): Download/Publish one or more images
    """

    VIDEO = 1
    IMAGE = 2


def display_logo():
    "Prints the program logo in the CLI"
    print("        ╭───┐┌─────────────────────────┐┌───╮")
    print("        │   │ │ ┌───────────────────┐ │ │ o │")
    print("        │ O │ │ │                   │ │ │o o│")
    print("        │ o │ │ │         |>        │ │ │ o │")
    print("        │o o│ │ │                   │ │ │ O │")
    print("        │ o │ │ └───────────────────┘ │ │   │")
    print("        ╰───┘└─────────────────────────┘└───╯")
    print("  ___          _  _        _")
    print(" / __|__ __ __(_)| |_  __ | |_")
    print(" \\__ \\\\ V  V /| ||  _|/ _|| ' \\")
    print(" |___/ \\_/\\_/ |_| \\__|\\__||_||_|")
    print("  __  __          _  _")
    print(" |  \\/  | ___  __| |(_) __ _")
    print(" | |\\/| |/ -_)/ _` || |/ _` |")
    print(" |_|  |_|\\___|\\__,_||_|\\__,_| ")
    print("  ___                      _                _")
    print(" |   \\  ___ __ __ __ _ _  | | ___  __ _  __| | ___  _ _")
    print(" | |) |/ _ \\\\ V  V /| ' \\ | |/ _ \\/ _` |/ _` |/ -_)| '_|")
    print(" |___/ \\___/ \\_/\\_/ |_||_||_|\\___/\\__,_|\\__,_|\\___||_|\n")


def add_hashtag_to_message(msg: str, reference_url: str) -> str:
    """Get the post and Add the Hashtag if exits and the user select use it

    Args:
        msg (str): The text of the post
        reference_url (str): url used as a reference to get the file info
    Example Reference URL:
        >>> 'http://192.168.0.1/img/2025030913522800-A8E55523A054F56F3FE005BBD56F49A7.jpg'
    Returns:
        the text in msg and the Hashtag if exists
    Example return:
        msg = "Lorem Ipsum"
        Returns = "Lorem Ipsum" or "Lorem Ipsum #Something"

    """
    game_hashtag = set_game_hashtag(get_game_id(get_file_name(reference_url)))
    if game_hashtag is not None:
        if (
            input(
                f"Se ha encontrado el siguiente hashtag {game_hashtag} ¿Quieres usarlo? y/n"
            )
            == "y"
        ):
            return f"{msg} {game_hashtag}"
    return msg


def publish_media(typemedia: TypeMedia, media_path: str, reference_url: str):
    """Publish the media in the social media that the user choose
    Args:
        typemedia (TypeMedia): Define the media to post IMAGE / VIDEO
        media_path (str): The path of the media file in the computer
        reference_url (str): url used as a reference to get the file info
    Example Reference URL:
        >>> 'http://192.168.0.1/img/2025030913522800-A8E55523A054F56F3FE005BBD56F49A7.jpg'

    """
    client = selectAPIs()
    msg = input("Mensaje del post: ")
    msg = add_hashtag_to_message(msg, reference_url)
    alt_text = ""
    if typemedia is TypeMedia.IMAGE:
        client.publish_image(msg=msg, file=media_path, alt_text=alt_text)
    else:
        client.publish_video(msg=msg, file=media_path, alt_text=alt_text)


def main():
    """
    Main fuction of the program
    """
    display_logo()
    can_publish = False
    wifi = get_switch_network()
    if wifi is not None:
        print(f"Wifi Switch = {wifi}")
        password = input("Contraseña Wifi Switch: ")

        if connect_to_switch(wifi, password):
            match input("Indique el contenido a descargar: (IMAGE/VIDEO)"):
                case TypeMedia.IMAGE.name:
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
                                publish_media(
                                    TypeMedia.IMAGE, photo_path[0], reference_url
                                )

                case TypeMedia.VIDEO.name:
                    link_video = connect_to_website_video()
                    try:
                        video_path = get_video(link_video)
                        can_publish = True
                    except BaseException:
                        pass
                    disconnect_to_swicth()
                    if can_publish:
                        match input("Quieres publicar este video: (y/n)"):
                            case "y":
                                publish_media(TypeMedia.VIDEO, video_path, link_video)
        else:
            print("No se ha podido descargar nada de la switch ")
    else:
        print("No hay una red Wifi correspondiente a una Nintendo Switch")


if __name__ == "__main__":
    main()
