import tweepy
from tweepy import Client
from tweepy.models import Media
from APIs.api import Api
import os


class Twitter(Api):
    client = Client()

    def __init__(
        self,
        primary_key: str,
        secret_key: str,
        token: str,
        token_secret: str,
        barrer_token: str,
    ):
        self.primary_key = primary_key
        self.secret_key = secret_key
        self.token = token
        self.secret_token = token_secret
        self.barren_token = barrer_token

    def connect(self) -> bool:
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
        except BaseException as e:
            return print(e)

    def publish_image(self, msg: str, file: str, alt_text: str):
        try:
            photo = self.update_media(file)
            self.client.create_tweet(text=msg, media_ids=[photo.media_id])
            return True
        except BaseException as e:
            return print(e)

    def publish_text():
        pass

    def publish_video(self, msg: str, file: str, alt_text: str):
        try:
            video = self.update_media(file)
            self.client.create_tweet(text=msg, media_ids=[video.media_id])
            return True
        except BaseException as e:
            return print(e)

    def view_preview():
        pass

    def update_media(self, file: str) -> Media:
        media = self.api.media_upload(filename=file)
        return media
