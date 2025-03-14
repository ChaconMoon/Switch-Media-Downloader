import os
from switch_media_downloader.APIs.bluesky import BlueSky
from dotenv import load_dotenv


def test_bluesky_connection_credential_error():
    load_dotenv()
    client = BlueSky("BLUESKY_SECUNDARY_NAME", "BLUESKY_SECUNDARY_API_KEY")
    assert client.connect() is not None


def test_bluesky_connection_atprotocol_error():
    load_dotenv()
    client = BlueSky("BLUESKY_SECUNDARY_NAME", "BLUESKY_SECUNDARY_API_KEY")
    assert client.connect() is not False


def test_bluesky_publish_photo():
    client = BlueSky("BLUESKY_SECUNDARY_NAME", "BLUESKY_SECUNDARY_API_KEY")
    client.connect()
    assert (
        client.publish_image(
            msg="Esta imagen esta siendo usada con fines de testeo.",
            file="./tests/test_media/placeholder_testing.jpg",
            alt_text="Esta imagen esta usado con fines de resteo desde mi GitHub.",
        )
        is True
    )


def test_bluesky_publish_video():
    client = BlueSky(
        os.getenv("BLUESKY_SECUNDARY_NAME"), os.getenv("BLUESKY_SECUNDARY_API_KEY")
    )
    client.connect()
    assert (
        client.publish_video(
            "Este video esta siendo usado con fines de testeo.",
            file="./tests/test_media/video_testing.mp4",
            alt_text="Este video esta siendo usado con fines de testeo desde mi GitHub.",
        )
        is True
    )
