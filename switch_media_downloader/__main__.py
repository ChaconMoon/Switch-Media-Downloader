"""
Module: __main__.py
Description: Module that starts the Switch Media Downloader
Author: Carlos Chacón
Date: 09-03-2025
"""

# --- Standard Dependence ---
from enum import Enum

import argparse

# --- Connect to switch Dependence ---
from switch_media_downloader.switch.connector import (
    get_switch_network,
    connect_to_switch,
    disconnect_to_swicth,
)

# --- Get switch images Dependence ---
from switch_media_downloader.switch.downloaders.image import (
    connect_to_website_images,
    get_switch_images,
)

# --- Hashtag of the games Dependence ---
from .controllers.hashtag_controller import set_game_hashtag

# --- Get media info Dependence ---
from .controllers.name_file_controller import get_file_name, get_game_id

# --- Get switch video Dependence ---
from .switch.downloaders.video import connect_to_website_video, get_video

# --- Get APIs Dependence ---
from .controllers.publish import selectAPIs


class TypeMedia(Enum):
    """Defines the names used to reference the type of media that will be download as a Enum
    Args:
        VIDEO (1): Download/Publish a video
        IMAGE (2): Download/Publish one or more images
    """

    VIDEO = 1
    IMAGE = 2


def arguments():
    parser = argparse.ArgumentParser(
        description="Opciones de automatización del Script"
    )
    parser.add_argument(
        "-p", "--password", type=str, help="The password of the Switch Wi-Fi"
    )
    media = parser.add_mutually_exclusive_group()
    media.add_argument(
        "-v", "--video", action="store_true", help="Set if you download a video"
    )
    media.add_argument(
        "-i", "--image", action="store_true", help="Set if you download images"
    )
    parser.add_argument(
        "--post", "--msg", type=str, help="The text of the post on the social media"
    )
    social = parser.add_mutually_exclusive_group()
    social.add_argument(
        "-m", "--mastodon", action="store_true", help="Publish the image on mastodon"
    )
    social.add_argument(
        "-t", "--twitter", action="store_true", help="Publish the image on twitter"
    )
    social.add_argument(
        "-b", "--bluesky", action="store_true", help="Publish the image on bluesky"
    )
    parser.add_argument(
        "--hashtag", action="store_true", help="Use the hashtag of the game in the post"
    )
    return parser.parse_args()


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


def add_hashtag_to_message(msg: str, reference_url: str, use_hashtag: bool) -> str:
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
        if use_hashtag:
            print(f"Se usara el siguiente hashtag {game_hashtag} ")
            return f"{msg} {game_hashtag}"
        elif (
            input(
                f"Se ha encontrado el siguiente hashtag {game_hashtag} ¿Quieres usarlo? (y/n): "
            )
            == "y"
        ):
            return f"{msg} {game_hashtag}"
    return msg


def publish_media(
    typemedia: TypeMedia,
    media_path: str,
    reference_url: str,
    hashtag: bool,
    social_media="",
    text="",
):
    """Publish the media in the social media that the user choose
    Args:
        typemedia (TypeMedia): Define the media to post IMAGE / VIDEO
        media_path (str): The path of the media file in the computer
        reference_url (str): url used as a reference to get the file info
    Example Reference URL:
        >>> 'http://192.168.0.1/img/2025030913522800-A8E55523A054F56F3FE005BBD56F49A7.jpg'

    """
    client = selectAPIs(option=social_media)
    if text == "":
        msg = input("Mensaje del post: ")
    else:
        msg = text
    msg = add_hashtag_to_message(msg, reference_url, hashtag)
    alt_text = ""
    if typemedia is TypeMedia.IMAGE:
        client.publish_image(msg=msg, file=media_path, alt_text=alt_text)
    else:
        client.publish_video(msg=msg, file=media_path, alt_text=alt_text)


def main():
    """
    Main fuction of the program
    """
    args = arguments()
    display_logo()
    can_publish = False
    wifi = get_switch_network()
    if wifi is not None:
        if args.password is None:
            print(f"Wifi Switch = {wifi}")
            password = input("Contraseña Wifi Switch: ")
        else:
            password = args.password

        if connect_to_switch(wifi, password):
            if args.video:
                type_media = "VIDEO"
            elif args.image:
                type_media = "IMAGE"
            else:
                type_media = input("Indique el contenido a descargar: (IMAGE/VIDEO): ")

            match type_media:
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
                        if args.mastodon:
                            social_media = "M"
                            pubish_option = "y"
                        elif args.twitter:
                            social_media = "T"
                            pubish_option = "y"
                        elif args.bluesky:
                            social_media = "B"
                            pubish_option = "y"
                        else:
                            pubish_option = input(
                                "Quieres publicar esta imagen: (y/n): "
                            )
                        match pubish_option:
                            case "y":
                                if args.post is not None:
                                    post_text = args.post

                                publish_media(
                                    TypeMedia.IMAGE,
                                    photo_path,
                                    reference_url,
                                    args.hashtag,
                                    social_media,
                                    text=post_text,
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
                        if args.mastodon:
                            social_media = "M"
                            pubish_option = "y"
                        elif args.twitter:
                            social_media = "T"
                            pubish_option = "y"
                        elif args.bluesky:
                            social_media = "B"
                            pubish_option = "y"
                        else:
                            pubish_option = input("Quieres publicar este video: (y/n)")
                        match pubish_option:
                            case "y":
                                if args.post is not None:
                                    post_text = args.post

                        match pubish_option:
                            case "y":
                                publish_media(
                                    TypeMedia.VIDEO,
                                    video_path,
                                    link_video,
                                    args.hashtag,
                                    social_media,
                                    text=post_text,
                                )
        else:
            print("No se ha podido descargar nada de la switch ")
    else:
        print("No hay una red Wifi correspondiente a una Nintendo Switch")


if __name__ == "__main__":
    main()
