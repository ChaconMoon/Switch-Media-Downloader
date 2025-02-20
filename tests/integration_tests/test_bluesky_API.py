import os
from APIs.bluesky import BlueSky
from dotenv import load_dotenv


def test_bluesky_connection_credential_error():
    load_dotenv()
    client = BlueSky(
        os.getenv("BLUESKY_SECUNDARY_NAME"), os.getenv("BLUESKY_SECUNDARY_API_KEY")
    )
    assert client.connect() is not None


def test_bluesky_connection_atprotocol_error():
    client = BlueSky(
        os.getenv("BLUESKY_SECUNDARY_NAME"), os.getenv("BLUESKY_SECUNDARY_API_KEY")
    )
    assert client.connect() is not False


def test_bluesky_publish_photo():
    client = BlueSky(
        os.getenv("BLUESKY_SECUNDARY_NAME"), os.getenv("BLUESKY_SECUNDARY_API_KEY")
    )
    client.connect()
    assert (
        client.publish_image(
            msg="Esta imagen esta siendo usada con fines de testeo.",
            file="./img/placeholder_testing.jpg",
            alt_text="Esta imagen esta usado con fines de resteo.",
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
            file="./video/video_testing.mp4",
            alt_text="Este video esta siendo usado con fines de testeo.",
        )
        is True
    )
