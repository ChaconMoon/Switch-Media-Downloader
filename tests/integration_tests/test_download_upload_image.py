from switch.downloaders.image import get_switch_images
from controllers.downloads import get_absolute_path
from APIs.twitter import Twitter


def test_upload_media_download():
    client = Twitter(
        "TWITTER_PRIMARY_API_KEY_TESTS",
        "TWITTER_PRIMARY_API_SECRET_KEY_TESTS",
        "TWITTER_PRIMARY_ACCESS_TOKEN_TESTS",
        "TWITTER_PRIMARY_ACCESS_TOKEN_SECRET_TESTS",
        "TWITTER_BEARER_TOKEN_TESTS",
    )
    client.connect()
    image_list = list()
    image_list.append(
        "https://raw.githubusercontent.com/ChaconMoon/TESTING/main/Switch_Media_Downloader/2024100319575600-DB679239AE5C0DC0D5E47C22D6492D98.jpg"
    )
    photo_path = get_switch_images(image_list)
    image = client.update_media(get_absolute_path(photo_path))
    assert image.media_id is not None


def test_download_upload_twitter_correct_image():
    client = Twitter(
        "TWITTER_PRIMARY_API_KEY_TESTS",
        "TWITTER_PRIMARY_API_SECRET_KEY_TESTS",
        "TWITTER_PRIMARY_ACCESS_TOKEN_TESTS",
        "TWITTER_PRIMARY_ACCESS_TOKEN_SECRET_TESTS",
        "TWITTER_BEARER_TOKEN_TESTS",
    )
    client.connect()
    image_list = list()
    image_list.append(
        "https://raw.githubusercontent.com/ChaconMoon/TESTING/main/Switch_Media_Downloader/2024100319575600-DB679239AE5C0DC0D5E47C22D6492D98.jpg"
    )
    photo_path = get_switch_images(image_list)
    assert (
        client.publish_image(
            msg="Esto es un test de integración",
            file=get_absolute_path(photo_path),
            alt_text="Esto es un texto alternativo",
        )
        is True
    )


def test_download_upload_twitter_correct_video():
    client = Twitter(
        "TWITTER_PRIMARY_API_KEY_TESTS",
        "TWITTER_PRIMARY_API_SECRET_KEY_TESTS",
        "TWITTER_PRIMARY_ACCESS_TOKEN_TESTS",
        "TWITTER_PRIMARY_ACCESS_TOKEN_SECRET_TESTS",
        "TWITTER_BEARER_TOKEN_TESTS",
    )
    client.connect()
    image_list = list()
    image_list.append(
        "https://raw.githubusercontent.com/ChaconMoon/TESTING/main/Switch_Media_Downloader/video_testing.mp4"
    )
    photo_path = get_switch_images(image_list)
    assert (
        client.publish_image(
            msg="Esto es un test de integración",
            file=get_absolute_path(photo_path),
            alt_text="Esto es un texto alternativo",
        )
        is True
    )
