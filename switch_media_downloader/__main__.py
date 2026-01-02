"""
Script made by Carlos Chacón.

Module: __main__.py
Description: Module that starts the Switch Media Downloader
Author: Carlos Chacón
Date: 09-03-2025.
"""
from sys import platform
# --- Standard Dependence ---
import argparse
from enum import Enum

# --- Hashtag of the games Dependence ---
from switch_media_downloader.controllers.hashtag_controller import set_game_hashtag

# --- Get media info Dependence ---
from switch_media_downloader.controllers.name_file_controller import (
        get_file_name,
        get_game_id,
)

# --- Get APIs Dependence ---
from switch_media_downloader.controllers.publish import select_apis
from switch_media_downloader.controllers.string_localization import StringLocalization

# --- Connect to switch Dependence ---
from switch_media_downloader.switch.connector import (
        connect_to_switch,
        disconnect_to_swicth,
        get_switch_network,
)

# --- Get switch images Dependence ---
from switch_media_downloader.switch.downloaders.image import (
        connect_to_website_images,
        get_switch_images,
)

# --- Get switch video Dependence ---
from switch_media_downloader.switch.downloaders.video import (
        connect_to_website_video,
        get_video,
)


class TypeMedia(Enum):
        """
        Define the names used to reference the type of media that will be download as a Enum.

        Args:
            VIDEO (1): Download/Publish a video
            IMAGE (2): Download/Publish one or more images.

        """  # noqa: E501

        VIDEO = 1
        IMAGE = 2


def arguments():
        """Arguments of the program."""
        parser = argparse.ArgumentParser(
                description=StringLocalization().get_localizated_string("params_text")
        )
        parser.add_argument(
                "-p",
                "--password",
                type=str,
                help=StringLocalization().get_localizated_string("param_password_text"),
        )
        media = parser.add_mutually_exclusive_group()
        media.add_argument(
                "-v",
                "--video",
                action="store_true",
                help=StringLocalization().get_localizated_string("param_video_text"),
        )
        media.add_argument(
                "-i",
                "--image",
                action="store_true",
                help=StringLocalization().get_localizated_string("param_image_text"),
        )
        parser.add_argument(
                "--download-only",
                action="store_true",
                help=StringLocalization().get_localizated_string(
                        "param_download_only_text"
                ),
        )
        parser.add_argument(
                "--post",
                "--msg",
                type=str,
                help=StringLocalization().get_localizated_string("param_post_text"),
        )
        parser.add_argument(
                "-m",
                "--mastodon",
                action="store_true",
                help=StringLocalization().get_localizated_string("param_mastodon_text"),
        )
        parser.add_argument(
                "-t",
                "--twitter",
                action="store_true",
                help=StringLocalization().get_localizated_string("param_twitter_text"),
        )
        parser.add_argument(
                "-b",
                "--bluesky",
                action="store_true",
                help=StringLocalization().get_localizated_string("param_bluesky_text"),
        )
        hashtag_arg = parser.add_mutually_exclusive_group()
        hashtag_arg.add_argument(
                "--hashtag",
                action="store_true",
                help=StringLocalization().get_localizated_string("param_hashtag_text"),
        )
        hashtag_arg.add_argument(
                "--no-hashtag",
                action="store_true",
                help=StringLocalization().get_localizated_string("param_no_hastag_text"),
        )
        return parser.parse_args()


def display_logo():
        """Print the program logo in the CLI."""
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
        """
        Get the post and Add the Hashtag if exits and the user select use it.

        Args:
            msg (str): The text of the post
            reference_url (str): url used as a reference to get the file info
            use_hashtag (bool): True if the program must use the Game Hashtag.
        Example Reference URL:
            >>> 'http://192.168.0.1/img/2025030913522800-A8E55523A054F56F3FE005BBD56F49A7.jpg'
        Returns:
            the text in msg and the Hashtag if exists
        Example return:
            msg = "Lorem Ipsum"
            Returns = "Lorem Ipsum" or "Lorem Ipsum #Something"

        """
        game_hashtag = set_game_hashtag(get_game_id(get_file_name(reference_url)))
        if game_hashtag is not None and not arguments().no_hashtag:
                if use_hashtag:
                        print(
                                StringLocalization()
                                .get_localizated_string("hashtag_found_text")
                                .format(game_hashtag)
                        )
                        return f"{msg} {game_hashtag}"
                if (
                        input(
                                StringLocalization()
                                .get_localizated_string("hashtag_found_question_text")
                                .format(game_hashtag)
                        )
                        == "y"
                ):
                        return f"{msg} {game_hashtag}"
        return msg


def publish_media(
        typemedia: TypeMedia,
        media_paths: list[str],
        reference_url: str,
        hashtag: bool,
        social_medias: list[str],
        text="",
):
        """
        Publish the media in the social media that the user choose.

        Args:
                typemedia (TypeMedia): Define the media to post IMAGE / VIDEO
                media_paths (list[str]): The paths of the media file in the computer
                reference_url (str): url used as a reference to get the file info
                hashtag (bool): True if the progrma must use the hashtag at publish the post
                social_medias: list[str]:
                The list of the options of the social media to publish the post
                text (str): The text of the post.
        Example Reference URL:
            >>> 'http://192.168.0.1/img/2025030913522800-A8E55523A054F56F3FE005BBD56F49A7.jpg'.

        """  # noqa: E501
        clients = []
        if "T" in social_medias:
                clients.append(select_apis(option="T"))
        if "B" in social_medias:
                clients.append(select_apis(option="B"))
        if "M" in social_medias:
                clients.append(select_apis(option="M"))
        if text == "":
                msg = input(
                        StringLocalization().get_localizated_string(
                                "posting_message_input_text"
                        )
                )
        else:
                msg = text
        msg = add_hashtag_to_message(msg, reference_url, hashtag)
        alt_text = ""
        for client in clients:
                if typemedia is TypeMedia.IMAGE:
                        client.publish_images(
                                msg=msg, files=media_paths, alt_text=alt_text
                        )
                else:
                        client.publish_video(
                                msg=msg,
                                file=media_paths[0].replace("/", "\\"),
                                alt_text=alt_text,
                        )
        return ""


def start_connection_to_switch(password: str):
        """
        Establish a connection to the Nintendo Switch using the provided Wi-Fi password.

        Args:
            password (str): The password for the Switch Wi-Fi network.

        Returns:
            bool: True if the connection is successful, False otherwise.

        """
        wifi = get_switch_network()
        if platform == "linux" or platform == "linux2":
                input("Please Connect to the Switch Wi-Fi manually. Then press Enter to continue...")
                return True
        if wifi is not None:
                if password is None:
                        print(
                                StringLocalization()
                                .get_localizated_string("switch_show_wifi_text")
                                .format(wifi)
                        )
                        password = input(
                                StringLocalization()
                                .get_localizated_string("switch_get_password")
                                .format(wifi)
                        )
                else:
                        password = password
                return connect_to_switch(wifi, password)
        print(StringLocalization().get_localizated_string("switch_no_wifi_error_text"))
        return False


def get_media_type(arg_video: bool, arg_image: bool):
        """
        Determine the type of media to download based on the provided arguments.

        Args:
            arg_video (bool): True if video is selected.
            arg_image (bool): True if image is selected.

        Returns:
            str: The type of media ("VIDEO" or "IMAGE").

        """
        if arg_video:
                type_media = "VIDEO"
        elif arg_image:
                type_media = "IMAGE"
        else:
                type_media = input(
                        StringLocalization().get_localizated_string(
                                "downloading_media_select_type_text"
                        )
                )
        return type_media


def get_social_medias(
        args_mastodon: bool,
        args_twitter: bool,
        args_bluesky: bool,
        photos: list[str],
        typemedia: TypeMedia,
):
        """
        Determine which social media platforms to use for posting based on user input and arguments.

        Args:
            args_mastodon (bool): Whether to post to Mastodon.
            args_twitter (bool): Whether to post to Twitter.
            args_bluesky (bool): Whether to post to Bluesky.
            photos (list[str]): List of photo paths (used for image posts).
            typemedia (TypeMedia): The type of media (IMAGE or VIDEO).

        Returns:
            list[str] or None: List of selected social media codes or None if posting is cancelled.

        """  # noqa: E501
        social_medias = []
        if args_mastodon:
                social_medias.append("M")
        if args_twitter:
                social_medias.append("T")
        if args_bluesky:
                social_medias.append("B")
        if not social_medias:
                if typemedia is TypeMedia.IMAGE:
                        if (
                                input(
                                        StringLocalization()
                                        .get_localizated_string(
                                                "posting_images_input_text"
                                        )
                                        .format(len(photos))
                                )
                                != "y"
                        ):
                                return None
                else:
                        if (
                                input(
                                        StringLocalization().get_localizated_string(
                                                "posting_video_input_text"
                                        )
                                )
                                != "y"
                        ):
                                return None
                media_list = (
                        input(
                                StringLocalization().get_localizated_string(
                                        "posting_select_social_media_input_text"
                                )
                        )
                        .upper()
                        .split(" ")
                )
                for letter in media_list:
                        if letter in ("T", "B", "M"):
                                social_medias.extend(letter)
        return social_medias


def post_in_social_media(
        social_medias: list,
        post_text: str,
        media_type: TypeMedia,
        media_paths: list,
        reference_url: str,
        hashtag: str,
):
        """
        Publish media to selected social media platforms.

        Args:
            social_medias (list): List of social media codes to post to.
            post_text (str): The text content of the post.
            media_type (TypeMedia): The type of media (IMAGE or VIDEO).
            media_paths (list): List of paths to media files.
            reference_url (str): Reference URL for the media.
            hashtag (str): Whether to include a hashtag in the post.

        """
        if social_medias is not None:
                if post_text is None:
                        post_text = ""

                publish_media(
                        media_type,
                        media_paths,
                        reference_url,
                        hashtag,
                        social_medias,
                        text=post_text,
                )


def main():
        """Start function."""
        args = arguments()
        display_logo()

        if not start_connection_to_switch(password=args.password):
                exit()

        match get_media_type(args.video, args.image):
                case TypeMedia.IMAGE.name:
                        url_list = connect_to_website_images()
                        try:
                                if url_list is not None:
                                        photo_paths = get_switch_images(url_list)
                                        reference_url = url_list[0]
                                        can_publish = True
                        except BaseException as e:  # noqa: BLE001
                                print(e)
                        disconnect_to_swicth()
                        if can_publish and not arguments().download_only:
                                print(
                                        StringLocalization()
                                        .get_localizated_string(
                                                "download_finish_images_text"
                                        )
                                        .format(len(url_list))
                                )

                                social_medias = get_social_medias(
                                        args.mastodon,
                                        args.twitter,
                                        args.bluesky,
                                        photo_paths,
                                        TypeMedia.IMAGE,
                                )

                                if social_medias is not None:
                                        post_in_social_media(
                                                social_medias,
                                                args.post,
                                                TypeMedia.IMAGE,
                                                photo_paths,
                                                reference_url,
                                                args.hashtag,
                                        )

                case TypeMedia.VIDEO.name:
                        link_video = connect_to_website_video()
                        video_path = []
                        try:
                                video_path.append(get_video(link_video))
                                can_publish = True
                        except BaseException as e:  # noqa: BLE001
                                print(e)
                        disconnect_to_swicth()

                        if not arguments().download_only:
                                social_medias = get_social_medias(
                                        args.mastodon,
                                        args.twitter,
                                        args.bluesky,
                                        video_path,
                                        TypeMedia.VIDEO,
                                )

                                if social_medias is not None:
                                        post_in_social_media(
                                                social_medias,
                                                args.post,
                                                TypeMedia.VIDEO,
                                                video_path,
                                                link_video,
                                                args.hashtag,
                                        )


if __name__ == "__main__":
        try:
                main()
        except KeyboardInterrupt:
                disconnect_to_swicth()
                print(
                        StringLocalization().get_localizated_string(
                                "keyboard_interrupt_text"
                        )
                )
