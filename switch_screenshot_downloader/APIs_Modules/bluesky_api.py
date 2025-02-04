from atproto import Client
from atproto.exceptions import AtProtocolError
from atproto_client.models.app.bsky.embed.defs import AspectRatio
import os
from dotenv import load_dotenv


def connect_bluesky() -> Client:
    load_dotenv()
    try:
        print("Conectando...")
        client = Client()
        client.login("chaconmoon.bsky.social", os.getenv("BLUESKY_API_KEY"))
        return client
    except AtProtocolError:
        print("Error en el inicio de sesión en BlueSky")
        return None


def publish_image(msg: str, file: str, alt_text: str, client: Client) -> bool:
    """
    Publish an image in the BlueSky Account

    Args:
        msg: The text of the post
        file: The path of the nintendo switch's image
        alt: The alterative text of the nintendo switch's image
        client: The ATProto client with the BlueSky session
    Returns:
        If the image is published
    """
    with open(file, "rb") as f:
        photo = f.read()
        aspect_ratio = AspectRatio(width=1280, height=720)
    try:
        client.send_image(
            text=msg, image=photo, image_alt=alt_text, image_aspect_ratio=aspect_ratio
        )
        return True
    except AtProtocolError:
        print("Error en ATProto, la imagen no ha sido publica")
        return False


def publish_video(msg: str, file: str, alt_text: str, client: Client) -> bool:
    """
    Publish a video in the BlueSky Account

    Args:
        msg: The text of the post
        file: The path of the nintendo switch's video
        alt: The alterative text of the nintendo switch's video
        client: The ATProto client with the BlueSky session
    Returns:
        If the video is published
    """
    with open(file, "rb") as v:
        video = v.read()
        aspect_ratio = AspectRatio(width=1280, height=720)

    try:
        client.send_video(
            text=msg, video=video, video_alt=alt_text, video_aspect_ratio=aspect_ratio
        )
        return True
    except AtProtocolError:
        print("Error en ATProto, el video no se ha publicado")
        return False
