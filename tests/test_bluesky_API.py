import pytest
from src.APIs.bluesky import connect_bluesky, publish_image, publish_video
from atproto import Client


def test_bluesky_connection():
    assert type(connect_bluesky()) is type(Client())


def test_bluesky_publish_photo():
    assert (
        publish_image(
            msg="Esta imagen esta siendo usada con fines de testeo.",
            file="./img/placeholder_testing.jpg",
            alt_text="Esta imagen esta usado con fines de resteo.",
            client=connect_bluesky(),
        )
        is True
    )


def test_bluesky_publish_video():
    assert (
        publish_video(
            "Este video esta siendo usado con fines de testeo.",
            file="./video/video_testing.mp4",
            alt_text="Este video esta siendo usado con fines de testeo.",
            client=connect_bluesky(),
        )
        is True
    )
