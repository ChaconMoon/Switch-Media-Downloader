"""
Module: mastodon.py.

Description: Module to interact with the Mastodon API
Author: Carlos Chacón
Date: 29-05-2025.
"""

# --- Import operative system module ---
import os

# ---Import time module ---
import time

# --- Import module to load enviroment variables ---
from dotenv import load_dotenv

# --- Import Mastodon API module
from mastodon import Mastodon

# --- Import API Abstract Class ---
from switch_media_downloader.APIs.api import Api


class MastodonAPI(Api):
        """
        Defines the methods to interact with the Mastodon API.

        Methods:
            connect(): Defines the method to connect to Mastodon
            publish_image(): Defines the method used to publish a image Mastodon
            publish_video(): Defines the method used to publish a video in Mastodon.
            publish_text(): Defines the method to publish a only-text post in Mastodon.
            view_preview(): Defines the method to preview the post before publish it.

        """

        def __init__(
                self,
                client_id: str,
                secret: str,
                access_token: str,
                mastodon_instance: str,
        ):
                """
                Create a object to interact with the Mastodon API.

                Args:
                        client_id (str): The App ID of the Mastodon App
                        secret (str): The Secret of your Mastodon App
                        access_token (str): The Access token of the Mastodon App
                        mastodon_instance (str):
                                The Mastodon Instance of your Mastodon Account
                                Ej: mastodon.social

                """
                self.app_id = client_id
                self.app_secret = secret
                self.token = access_token
                self.instance = mastodon_instance

        def connect(self):
                """Connect to the Mastodon Account."""
                load_dotenv()
                self.client = Mastodon(
                        client_id=os.getenv("APPLICATION_ID_MASTODON"),
                        access_token=os.getenv("ACCESS_TOKEN_MASTODON"),
                        api_base_url=os.getenv("MASTODON_INSTANCE"),
                        client_secret=os.getenv("SECRET_MASTODON"),
                )

        def publish_images(self, msg: str, files: list[str], alt_text: str):
                """
                Publish images in your Mastodon Account.

                Args:
                        msg (str): The text of the post
                        files (list[str]): A list of the paths of the images to publish
                        alt_text (str): The Alternative Text of the images post.

                """
                media_ids = []
                for each_file in files:
                        media = self.client.media_post(
                                media_file=each_file,
                                description=alt_text,
                                mime_type="image/jpg",
                        )
                        media_ids.append(media.id)
                self.client.status_post(status=msg, media_ids=media_ids)

        def publish_text(self, msg):
                """
                Publish a post text-only post in Mastodon.

                Args:
                        msg (str): The text of the post

                """
                self.client.toot(status=msg)

        def publish_video(self, msg, file, alt_text):
                """
                Publish a video in the Mastodon Account.

                Args:
                        msg (str): The text of the post.
                        file (str): The path of the video file.
                        alt_text: The Alternative Text of the video.

                """
                video = self.client.media_post(
                        media_file=file, description=alt_text, mime_type="video/mp4"
                )
                info_media = self.client.media(video)

                while info_media["url"] is None:
                        time.sleep(5)
                        info_media = self.client.media(video)

                self.client.status_post(status=msg, media_ids=video.id)

        def view_preview(self, msg, file, alt_text):
                """Non Implemented."""
                return super().view_preview(msg, file, alt_text)
