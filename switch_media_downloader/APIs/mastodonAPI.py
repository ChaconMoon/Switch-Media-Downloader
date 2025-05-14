import time
from mastodon import Mastodon

from dotenv import load_dotenv

import os

from switch_media_downloader.APIs.api import Api


class MastodonAPI(Api):
    def __init__(
        self, client_id: str, secret: str, access_token: str, mastodon_instance: str
    ):
        self.app_id = client_id
        self.app_secret = secret
        self.token = access_token
        self.instance = mastodon_instance

    def connect(self):
        load_dotenv()
        self.client = Mastodon(
            client_id=os.getenv("APPLICATION_ID_MASTODON"),
            access_token=os.getenv("ACCESS_TOKEN_MASTODON"),
            api_base_url=os.getenv("MASTODON_INSTANCE"),
            client_secret=os.getenv("SECRET_MASTODON"),
        )

    def publish_images(self, msg, files: list[str], alt_text):
        image = self.client.media_post(
            media_file=files[0], description=alt_text, mime_type="image/jpg"
        )
        self.client.status_post(status=msg, media_ids=image.id)

    def publish_text(self, msg):
        self.client.toot(status=msg)

    def publish_video(self, msg, file, alt_text):
        video = self.client.media_post(
            media_file=file, description=alt_text, mime_type="video/mp4"
        )
        info_media = self.client.media(video)

        while info_media["url"] is None:
            time.sleep(5)
            info_media = self.client.media(video)

        self.client.status_post(status=msg, media_ids=video.id)

    def view_preview(self, msg, file, alt_text):
        return super().view_preview(msg, file, alt_text)
