from switch_media_downloader.APIs.twitter import Twitter


def test_twiiter_connection():
        client = Twitter(
                "TWITTER_PRIMARY_API_KEY_TESTS",
                "TWITTER_PRIMARY_API_SECRET_KEY_TESTS",
                "TWITTER_PRIMARY_ACCESS_TOKEN_TESTS",
                "TWITTER_PRIMARY_ACCESS_TOKEN_SECRET_TESTS",
                "TWITTER_BEARER_TOKEN_TESTS",
        )
        assert client.connect() is True


def test_twiiter_publish_image():
        client = Twitter(
                "TWITTER_PRIMARY_API_KEY_TESTS",
                "TWITTER_PRIMARY_API_SECRET_KEY_TESTS",
                "TWITTER_PRIMARY_ACCESS_TOKEN_TESTS",
                "TWITTER_PRIMARY_ACCESS_TOKEN_SECRET_TESTS",
                "TWITTER_BEARER_TOKEN_TESTS",
        )
        client.connect()
        assert (
                client.publish_images(
                        msg="Imagen usada como test desde mi GitHub",
                        files=["./tests/test_media/placeholder_testing.jpg"],
                        alt_text="Alt Text",
                )
                is True
        )


def test_twiiter_publish_images():
        client = Twitter(
                "TWITTER_PRIMARY_API_KEY_TESTS",
                "TWITTER_PRIMARY_API_SECRET_KEY_TESTS",
                "TWITTER_PRIMARY_ACCESS_TOKEN_TESTS",
                "TWITTER_PRIMARY_ACCESS_TOKEN_SECRET_TESTS",
                "TWITTER_BEARER_TOKEN_TESTS",
        )
        client.connect()
        assert (
                client.publish_images(
                        msg="Imagen usada como test desde mi GitHub",
                        files=[
                                "./tests/test_media/placeholder_testing.jpg",
                                "./tests/test_media/placeholder_testing.jpg",
                                "./tests/test_media/placeholder_testing.jpg",
                                "./tests/test_media/placeholder_testing.jpg",
                        ],
                        alt_text="Alt Text",
                )
                is True
        )


def test_twiiter_publish_image_none():
        client = Twitter(
                "TWITTER_PRIMARY_API_KEY_TESTS",
                "TWITTER_PRIMARY_API_SECRET_KEY_TESTS",
                "TWITTER_PRIMARY_ACCESS_TOKEN_TESTS",
                "TWITTER_PRIMARY_ACCESS_TOKEN_SECRET_TESTS",
                "TWITTER_BEARER_TOKEN_TESTS",
        )
        client.connect()
        assert (
                client.publish_images(
                        msg=None,
                        files=None,
                        alt_text=None,
                )
                is False
        )


def test_twiiter_publish_video():
        client = Twitter(
                "TWITTER_PRIMARY_API_KEY_TESTS",
                "TWITTER_PRIMARY_API_SECRET_KEY_TESTS",
                "TWITTER_PRIMARY_ACCESS_TOKEN_TESTS",
                "TWITTER_PRIMARY_ACCESS_TOKEN_SECRET_TESTS",
                "TWITTER_BEARER_TOKEN_TESTS",
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


def test_twiiter_publish_video_none():
        client = Twitter(
                "TWITTER_PRIMARY_API_KEY_TESTS",
                "TWITTER_PRIMARY_API_SECRET_KEY_TESTS",
                "TWITTER_PRIMARY_ACCESS_TOKEN_TESTS",
                "TWITTER_PRIMARY_ACCESS_TOKEN_SECRET_TESTS",
                "TWITTER_BEARER_TOKEN_TESTS",
        )
        client.connect()
        assert (
                client.publish_video(
                        msg=None,
                        file=None,
                        alt_text=None,
                )
                is False
        )


def test_update_media():
        client = Twitter(
                "TWITTER_PRIMARY_API_KEY_TESTS",
                "TWITTER_PRIMARY_API_SECRET_KEY_TESTS",
                "TWITTER_PRIMARY_ACCESS_TOKEN_TESTS",
                "TWITTER_PRIMARY_ACCESS_TOKEN_SECRET_TESTS",
                "TWITTER_BEARER_TOKEN_TESTS",
        )
        client.connect()
        assert client.update_media("./tests/test_media/video_testing.mp4") is not None


def test_update_media_none():
        client = Twitter(
                "TWITTER_PRIMARY_API_KEY_TESTS",
                "TWITTER_PRIMARY_API_SECRET_KEY_TESTS",
                "TWITTER_PRIMARY_ACCESS_TOKEN_TESTS",
                "TWITTER_PRIMARY_ACCESS_TOKEN_SECRET_TESTS",
                "TWITTER_BEARER_TOKEN_TESTS",
        )
        client.connect()
        assert client.update_media(None) is None


def test_update_media_not_valid():
        client = Twitter(
                "TWITTER_PRIMARY_API_KEY_TESTS",
                "TWITTER_PRIMARY_API_SECRET_KEY_TESTS",
                "TWITTER_PRIMARY_ACCESS_TOKEN_TESTS",
                "TWITTER_PRIMARY_ACCESS_TOKEN_SECRET_TESTS",
                "TWITTER_BEARER_TOKEN_TESTS",
        )
        client.connect()
        assert client.update_media("./tests/test_media/video_testing") is None
