"""
Module: twitter.py.

Description: Module to interact with the Twitter API
Author: Carlos Chacón
Date: 09-03-2025.
"""

# --- Import Operative System Module
import os

# --- Import Path libary ---
from pathlib import Path

# --- Api Twitter Depencence ---
import tweepy

# --- Import Dependece to intect with Twitter media
import tweepy.errors

# --- load the enviroment variables dependeces ---
from dotenv import load_dotenv

# --- Import Twitter API Dependence ---
from tweepy import Client
from tweepy.models import Media

# --- Import API Abstract Class ---
from switch_media_downloader.APIs.api import Api

# --- Import String Localization Module ---
from switch_media_downloader.controllers.string_localization import StringLocalization


class Twitter(Api):
        """
        Class to Interact with the Twitter API.

        Methods:
            connect(): Defines the method to connect to Twitter
            publish_image(): Defines the method used to publish a image Twitter
            publish_video(): Defines the method used to publish a video in Twitter.
            publish_text(): Defines the method to publish a only-text post in Twitter.
            view_preview(): Defines the method to preview the post before publish it.

        """

        # --- Create a Client to interact with the Twitter Client
        client = Client()

        # Init the keys to the Twitter API
        def __init__(
                self,
                primary_key: str,
                secret_key: str,
                token: str,
                token_secret: str,
                barrer_token: str,
        ):
                """
                Create an object to post on Twitter.

                Args:
                        primary_key (str): The environment variable name for the Twitter API primary key.
                        secret_key (str): The environment variable name for the Twitter API secret key.
                        token (str): The environment variable name for the Twitter API access token.
                        token_secret (str): The environment variable name for the Twitter API access token secret.
                        barrer_token (str): The environment variable name for the Twitter API bearer token.

                """  # noqa: E501
                load_dotenv()
                self.primary_key = os.getenv(primary_key)
                self.secret_key = os.getenv(secret_key)
                self.token = os.getenv(token)
                self.secret_token = os.getenv(token_secret)
                self.barren_token = os.getenv(barrer_token)

        def connect(self) -> bool:
                """
                Connect to your Twitter accounnt.

                Returns:
                    If the connection was Successful or the exception

                """
                try:
                        print(
                                StringLocalization().get_localizated_string(
                                        "twitter_connection_text"
                                )
                        )
                        self.client = tweepy.Client(
                                consumer_key=self.primary_key,
                                consumer_secret=self.secret_key,
                                access_token=self.token,
                                access_token_secret=self.secret_token,
                        )

                        self.auth = tweepy.OAuth1UserHandler(
                                consumer_key=self.primary_key,
                                consumer_secret=self.secret_key,
                                access_token=self.token,
                                access_token_secret=self.secret_token,
                        )
                        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)
                        print(self.api.verify_credentials().screen_name)
                        return True
                except tweepy.errors.Unauthorized as e:
                        return print(e)

        def publish_images(self, msg: str, files: list[str], alt_text: str):  # noqa: ARG002
                """
                Publish an image in your Twitter Profile or the exception.

                Args:
                    msg (str): The text of the post
                    files (list[str]): The path of the nintendo switch's images
                    alt_text (str): The alterative text of the nintendo switch's image
                Returns:
                    If the image is published

                """
                try:
                        photos_ids = []
                        for file in files:
                                media = self.update_media(file)
                                photos_ids.append(media.media_id)
                        self.client.create_tweet(text=msg, media_ids=photos_ids)
                        print(
                                StringLocalization().get_localizated_string(
                                        "twitter_succesful_posting"
                                )
                        )
                        return True
                except TypeError:
                        print(
                                StringLocalization().get_localizated_string(
                                        "typeError_text"
                                )
                        )
                        return False
                except AttributeError as e:
                        print(f"AttributeError {e}")
                        return False

        def publish_text():
                """Not implemented."""

        def publish_video(self, msg: str, file: str, alt_text: str):  # noqa: ARG002
                """
                Publish a video your Twitter profile.

                Args:
                    msg (str): The text of the post
                    file (str): The path of the nintendo switch's video
                    alt_text (str): The alterative text of the nintendo switch's video
                Returns:
                    If the video is published

                """
                try:
                        video = self.update_media(file)
                        self.client.create_tweet(text=msg, media_ids=[video.media_id])
                        return True
                except TypeError:
                        print(
                                StringLocalization().get_localizated_string(
                                        "typeError_text"
                                )
                        )
                        return False
                except AttributeError as e:
                        print(f"AttributeError {e}")
                        return False

        def view_preview():
                """Not implemented."""

        def update_media(self, file: str) -> Media:
                """
                Upload a media to your Twitter account.

                Args:
                    file (str): path of the file

                Returns:
                    The media reference of the uploaded file.

                """
                try:
                        if Path(file).exists() is False or (
                                file.endswith(".mp4") is False
                                and file.endswith(".jpg") is False
                        ):
                                return None
                        return self.api.media_upload(
                                filename=file
                        )  # Returns media of twitter
                except TypeError:
                        return None
