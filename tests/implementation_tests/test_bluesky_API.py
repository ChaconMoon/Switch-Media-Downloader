import os
from switch_media_downloader.APIs.bluesky import BlueSky


def test_bluesky_connection_credential_error():
    client = BlueSky("BLUESKY_SECUNDARY_NAME", "BLUESKY_SECUNDARY_API_KEY")
    assert client.connect() is not None


def test_bluesky_connection_atprotocol_error():
    client = BlueSky("BLUESKY_SECUNDARY_NAME", "BLUESKY_SECUNDARY_API_KEY")
    assert client.connect() is not False


def test_bluesky_publish_image():
    client = BlueSky("BLUESKY_SECUNDARY_NAME", "BLUESKY_SECUNDARY_API_KEY")
    client.connect()
    assert (
        client.publish_image(
            msg="Esta imagen esta siendo usada con fines de testeo desde mi GitHub.",
            file="./tests/test_media/placeholder_testing.jpg",
            alt_text="Esta imagen esta usado con fines de testeo desde mi GitHub.",
        )
        is True
    )


def test_bluesky_publish_image_none():
    client = BlueSky("BLUESKY_SECUNDARY_NAME", "BLUESKY_SECUNDARY_API_KEY")
    client.connect()
    assert (
        client.publish_image(
            msg=None,
            file=None,
            alt_text=None,
        )
        is False
    )


def test_bluesky_publish_video():
    client = BlueSky(
        os.getenv("BLUESKY_SECUNDARY_NAME"), os.getenv("BLUESKY_SECUNDARY_API_KEY")
    )
    client.connect()
    assert (
        client.publish_video(
            "Este video esta siendo usado con fines de testeo desde mi GitHub.",
            file="./tests/test_media/video_testing.mp4",
            alt_text="Este video esta siendo usado con fines de testeo desde mi GitHub.",
        )
        is True
    )


def test_bluesky_publish_video_none():
    client = BlueSky(
        os.getenv("BLUESKY_SECUNDARY_NAME"), os.getenv("BLUESKY_SECUNDARY_API_KEY")
    )
    client.connect()
    assert (
        client.publish_video(
            None,
            None,
            None,
        )
        is False
    )
