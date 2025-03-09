import os
from dotenv import load_dotenv
from switch_media_downloader.APIs.twitter import Twitter


def test_twiiter_connection():
    load_dotenv()
    client = Twitter(
        os.getenv("TWITTER_PRIMARY_API_KEY"),
        os.getenv("TWITTER_PRIMARY_API_SECRET_KEY"),
        os.getenv("TWITTER_PRIMARY_ACCESS_TOKEN"),
        os.getenv("TWITTER_PRIMARY_ACCESS_TOKEN_SECRET"),
        os.getenv("TWITTER_BEARER_TOKEN"),
    )
    assert client.connect() is True


def test_twiiter_publish_image():
    client = Twitter(
        os.getenv("TWITTER_PRIMARY_API_KEY"),
        os.getenv("TWITTER_PRIMARY_API_SECRET_KEY"),
        os.getenv("TWITTER_PRIMARY_ACCESS_TOKEN"),
        os.getenv("TWITTER_PRIMARY_ACCESS_TOKEN_SECRET"),
        os.getenv("TWITTER_BEARER_TOKEN"),
    )
    client.connect()
    assert (
        client.publish_image(
            "Asi me imagino la gente cuando le digo que me gusta Just Dance",
            "./img/test_warioware.jpg",
        )
        is True
    )
