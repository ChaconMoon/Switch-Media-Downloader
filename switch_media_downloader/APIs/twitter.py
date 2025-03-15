"""
Module: twitter.py
Description: Module to interact with the Twitter API
Author: Carlos Chacón
Date: 09-03-2025
"""

# --- Api Twitter Depencence ---
import tweepy

# --- Import Twitter API Dependence ---
from tweepy import Client

# --- Import Dependece to intect with Twitter media
from tweepy.models import Media

# --- Import Operative System Dependecies
import os

# --- load the enviroment variables dependeces ---
from dotenv import load_dotenv

# --- Import API interface module
from APIs.api import Api


class Twitter(Api):
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
        load_dotenv()
        self.primary_key = os.getenv(primary_key)
        self.secret_key = os.getenv(secret_key)
        self.token = os.getenv(token)
        self.secret_token = os.getenv(token_secret)
        self.barren_token = os.getenv(barrer_token)

    def connect(self) -> bool:
        """
        Connect to your Twitter accounnt

        Returns:
            If the connection was Successful or the exception

        """
        try:
            print("Conectando con Twitter (X)")
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
        except Exception as e:
            return print(e)

    def publish_image(self, msg: str, file: str, alt_text: str):
        """
        Publish an image in your Twitter Profile or the exception

        Args:
            msg (str): The text of the post
            file (str): The path of the nintendo switch's image
            alt (str): The alterative text of the nintendo switch's image
        Returns:
            If the image is published
        """

        try:
            photo = self.update_media(file)
            self.client.create_tweet(text=msg, media_ids=[photo.media_id])
            return True
        except TypeError as e:
            print(e)
            return False

    def publish_text():
        pass

    def publish_video(self, msg: str, file: str, alt_text: str):
        """
        Publish a video your Twitter profile

        Args:
            msg (str): The text of the post
            file (str): The path of the nintendo switch's video
            alt (str): The alterative text of the nintendo switch's video
        Returns:
            If the video is published
        """
        try:
            video = self.update_media(file)
            self.client.create_tweet(text=msg, media_ids=[video.media_id])
            return True
        except TypeError:
            print("Error de tipo")
            return False

    def view_preview():
        pass

    def update_media(self, file: str) -> Media:
        """
        Upload a media to your Twitter account
        Args:
            file (str): path of the file
        Returns:
            The media reference of the uploaded file
        """
        try:
            if (
                os.path.exists(file) is False
                or file.endswith(".mp4") is False
                or file.endswith(".jpg")
            ):
                return None
            media = self.api.media_upload(filename=file)
            return media
        except TypeError:
            return None
