from atproto import Client
from atproto_client.models.app.bsky.embed.defs import AspectRatio


def publish_photo(msg: str, file: str, alt_text: str):
    print("Conectando...")
    client = Client()
    client.login("chaconmoon.bsky.social", "")
    with open(file, "rb") as f:
        photo = f.read()
        aspect_ratio = AspectRatio(width=1280, height=720)
    client.send_image(
        text=msg, image=photo, image_alt=alt_text, image_aspect_ratio=aspect_ratio
    )
