from switch_media_downloader.APIs.twitter import Twitter


def test_twiiter_connection():
    client = Twitter(
        "TWITTER_PRIMARY_API_KEY",
        "TWITTER_PRIMARY_API_SECRET_KEY",
        "TWITTER_PRIMARY_ACCESS_TOKEN",
        "TWITTER_PRIMARY_ACCESS_TOKEN_SECRET",
        "TWITTER_BEARER_TOKEN",
    )
    assert client.connect() is True


def test_twiiter_publish_image():
    client = Twitter(
        "TWITTER_PRIMARY_API_KEY",
        "TWITTER_PRIMARY_API_SECRET_KEY",
        "TWITTER_PRIMARY_ACCESS_TOKEN",
        "TWITTER_PRIMARY_ACCESS_TOKEN_SECRET",
        "TWITTER_BEARER_TOKEN",
    )
    client.connect()
    assert (
        client.publish_image(
            msg="Imagen usada como test desde mi GitHub",
            file="./tests/test_media/placeholder_testing.jpg",
            alt_text="Alt Text",
        )
        is True
    )


def test_twiiter_publish_video():
    client = Twitter(
        "TWITTER_PRIMARY_API_KEY",
        "TWITTER_PRIMARY_API_SECRET_KEY",
        "TWITTER_PRIMARY_ACCESS_TOKEN",
        "TWITTER_PRIMARY_ACCESS_TOKEN_SECRET",
        "TWITTER_BEARER_TOKEN",
    )
    client.connect()
    assert (
        client.publish_video(
            msg="Video usado como test desde mi GitHub",
            file="./tests/test_media/video_testing.mp4",
            alt_text="Alt Text",
        )
        is True
    )
