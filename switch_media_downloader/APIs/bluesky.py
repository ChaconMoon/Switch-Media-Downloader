"""
Module: bluesky.py
Description: Module to interact with the Bluesky API
Author: Carlos Chacón
Date: 09-03-2025
"""

# --- Import the ATProto Client ---
from atproto import Client

# --- Import the ATProto Exceptions ---
from atproto.exceptions import AtProtocolError

# --- Import the AspectRadio module ---
from atproto_client.models.app.bsky.embed.defs import AspectRatio

# --- Import operative system operations ---
import os

# --- load the enviroment variables dependeces ---
from dotenv import load_dotenv

# --- load Apis module
from switch_media_downloader.APIs.api import Api


class BlueSky(Api):
    """
    Defines the methods for Bluesky API

    methods:
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
        load_dotenv()
        self.account = os.getenv(account)
        self.token = os.getenv(token)
        pass

    # Override the string method
    def __str__(self):
        return f"{self.account, self.client}"

    def connect(self) -> bool:
        """
        Connect to your BlueSky Account

        Returns:
            If the connection was Successful

        """
        try:
            print("Conectando...")
            self.client.login(self.account, self.token)
            print("Conexion exitosa")
            return True
        except AtProtocolError:
            print("Error en el inicio de sesión en BlueSky")
            return False
        except ValueError:
            print("Error a la hora de importar las credenciales")
            return None

    def publish_images(self, msg: str, files: list[str], alt_text: str) -> bool:
        """
        Publish an image in your Bluesky Profile

        Args:
            msg (str): The text of the post
            file (str): The path of the nintendo switch's image
            alt (str): The alterative text of the nintendo switch's image
        Returns:
            If the image is published
        """
        try:
            if len(files) > 1:
                print(
                    "Por limitaciones de la API de Bluesky no se permite la publicación de multiples imagen en un post, se usara solo la primera."
                )
            with open(files[0], "rb") as f:
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
            print("Error en ATProto, la imagen no ha sido publica")
            return False
        except TypeError:
            print("Error de tipo")
            return False

    def publish_video(self, msg: str, file: str, alt_text: str) -> bool:
        """
        Publish a video in your BlueSky Profile

        Args:
            msg (str): The text of the post
            file (str): The path of the nintendo switch's video
            alt (str): The alterative text of the nintendo switch's video
        Returns:
            If the video is published
        """
        try:
            with open(file, "rb") as v:
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
            print("Error en ATProto, el video no se ha publicado")
            return False
        except TypeError:
            print("Error de tipo")
            return False

    def publish_text():
        pass

    def view_preview():
        pass
