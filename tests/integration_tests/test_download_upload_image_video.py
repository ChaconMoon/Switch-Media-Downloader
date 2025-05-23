from switch_media_downloader.APIs.bluesky import BlueSky
from switch_media_downloader.APIs.twitter import Twitter
from switch_media_downloader.controllers.downloads import get_absolute_path
from switch_media_downloader.switch.downloaders.image import get_image
from switch_media_downloader.switch.downloaders.video import get_video


def test_upload_media_download():
        client = Twitter(
                "TWITTER_PRIMARY_API_KEY_TESTS",
                "TWITTER_PRIMARY_API_SECRET_KEY_TESTS",
                "TWITTER_PRIMARY_ACCESS_TOKEN_TESTS",
                "TWITTER_PRIMARY_ACCESS_TOKEN_SECRET_TESTS",
                "TWITTER_BEARER_TOKEN_TESTS",
        )
        client.connect()
        image_list = []
        image_list.append(
                "https://raw.githubusercontent.com/ChaconMoon/TESTING/main/Switch_Media_Downloader/2024100319575600-DB679239AE5C0DC0D5E47C22D6492D98.jpg"
        )
        photo_path = get_image(image_list[0])
        image = client.update_media(photo_path)
        print(get_absolute_path(photo_path))
        assert image.media_id is not None


def test_download_upload_bluesky_correct_image():
        client = BlueSky("BLUESKY_SECUNDARY_NAME", "BLUESKY_SECUNDARY_API_KEY")

        client.connect()
        image_list = []
        image_list.append(
                "https://raw.githubusercontent.com/ChaconMoon/TESTING/main/Switch_Media_Downloader/2024100319575600-DB679239AE5C0DC0D5E47C22D6492D98.jpg"
        )
        photo_path = get_image(image_list[0])
        list_images = []
        list_images.append(photo_path)
        assert (
                client.publish_images(
                        msg="Esto es un test de integración",
                        files=list_images,
                        alt_text="Esto es un texto alternativo",
                )
                is True
        )


def test_download_upload_bluesky_correct_video():
        client = BlueSky("BLUESKY_SECUNDARY_NAME", "BLUESKY_SECUNDARY_API_KEY")
        client.connect()
        image_list = []
        image_list.append(
                "https://raw.githubusercontent.com/ChaconMoon/TESTING/main/Switch_Media_Downloader/video_testing.mp4"
        )
        video_path = get_video(image_list[0])
        assert (
                client.publish_video(
                        msg="Esto es un test de integración",
                        file=video_path,
                        alt_text="Esto es un texto alternativo",
                )
                is True
        )
