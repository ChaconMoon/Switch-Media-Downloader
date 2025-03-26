from mastodon import Mastodon

from dotenv import load_dotenv

import os

from APIs.api import Api


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

    def publish_image(self, msg, file, alt_text):
        image = self.client.media_post(
            media_file=file, description=alt_text, mime_type="image/jpg"
        )
        self.client.status_post(status=msg, media_ids=image.id)

    def publish_text(self, msg):
        self.client.toot(status=msg)

    def publish_video(self, msg, file, alt_text):
        return super().publish_video(msg, file, alt_text)

    def view_preview(self, msg, file, alt_text):
        return super().view_preview(msg, file, alt_text)
