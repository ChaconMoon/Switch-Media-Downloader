"""
Module: bluesky.py.

Description: Module to interact with the Bluesky API
Author: Carlos Chacón
Date: 09-03-2025.
"""

# --- Import the ATProto Client ---
# --- Import operative system operations ---
import os
from pathlib import Path

from atproto import Client

# --- Import the ATProto Exceptions ---
from atproto.exceptions import AtProtocolError

# --- Import the AspectRadio module ---
from atproto_client.models.app.bsky.embed.defs import AspectRatio

# --- load the enviroment variables dependeces ---
from dotenv import load_dotenv

# --- load Apis Abstact Class ---
from switch_media_downloader.APIs.api import Api

# --- load String Localization ---
from switch_media_downloader.controllers.string_localization import StringLocalization


class BlueSky(Api):
        """
        Defines the methods for Bluesky API.

        Methods:
            connect(): Defines the method to connect to BlueSky
            publish_image(): Defines the method used to publish a image BlueSky
            publish_video(): Defines the method used to publish a video in BlueSky.
            publish_text(): Defines the method to publish a only-text post in BlueSky.
            view_preview(): Defines the method to preview the post before publish it.

        """

        # Create a client object to manage the Api connection
        client = Client()

        # Init the name of the account and the token
        def __init__(self, account: str, token: str):
                """
                Create a new object to connect to the bluesky API.

                Args:
                        account (str): The Bluesky Account Username
                        token (str): The Bluesky API Token

                """
                load_dotenv()
                self.account = os.getenv(account)
                self.token = os.getenv(token)

        # Override the string method
        def __str__(self):
                """Overrride the string method to print the account info."""
                return f"{self.account, self.client}"

        def connect(self) -> bool:
                """
                Connect to your BlueSky Account.

                Returns:
                    If the connection was Successful

                """
                try:
                        print(
                                StringLocalization().get_localizated_string(
                                        "bluesky_connection_text_1"
                                )
                        )
                        self.client.login(self.account, self.token)
                        print(
                                StringLocalization().get_localizated_string(
                                        "bluesky_connection_text_2"
                                )
                        )
                        return True
                except AtProtocolError:
                        print(
                                StringLocalization().get_localizated_string(
                                        "bluesky_session_error_text"
                                )
                        )
                        return False
                except ValueError:
                        print(
                                StringLocalization().get_localizated_string(
                                        "bluesky_credential_import_error_text"
                                )
                        )
                        return None

        def publish_images(self, msg: str, files: list[str], alt_text: str) -> bool:
                """
                Publish an image in your Bluesky Profile.

                Args:
                    msg (str): The text of the post
                    files (list[str]): The path of the nintendo switch's image
                    alt_text (str): The alterative text of the nintendo switch's image
                Returns:
                    If the image is published

                """
                try:
                        if len(files) > 1:
                                print(
                                        StringLocalization().get_localizated_string(
                                                "bluesky_limitation_text"
                                        )
                                )
                        with Path.open(files[0], "rb") as f:
                                photo = f.read()
                                aspect_ratio = AspectRatio(width=1280, height=720)

                        self.client.send_image(
                                text=msg,
                                image=photo,
                                image_alt=alt_text,
                                image_aspect_ratio=aspect_ratio,
                        )
                        return True
                except AtProtocolError:
                        print(
                                StringLocalization().get_localizated_string(
                                        "bluesky_ATProtocol_Error_text_image"
                                )
                        )
                        return False
                except TypeError:
                        print(
                                StringLocalization().get_localizated_string(
                                        "typeError_text"
                                )
                        )
                        return False

        def publish_video(self, msg: str, file: str, alt_text: str) -> bool:
                """
                Publish a video in your BlueSky Profile.

                Args:
                    msg (str): The text of the post
                    file (str): The path of the nintendo switch's video
                    alt_text (str): The alterative text of the nintendo switch's video
                Returns:
                    If the video is published

                """
                try:
                        with Path.open(file, "rb") as v:
                                video = v.read()
                                aspect_ratio = AspectRatio(width=1280, height=720)

                        self.client.send_video(
                                text=msg,
                                video=video,
                                video_alt=alt_text,
                                video_aspect_ratio=aspect_ratio,
                        )
                        return True
                except AtProtocolError:
                        print(
                                StringLocalization().get_localizated_string(
                                        "bluesky_ATProtocol_Error_text_video"
                                )
                        )
                        return False
                except TypeError:
                        print(
                                StringLocalization().get_localizated_string(
                                        "typeError_text"
                                )
                        )
                        return False

        def publish_text():
                """Non Implemented."""

        def view_preview():
                """Non Implemented."""
