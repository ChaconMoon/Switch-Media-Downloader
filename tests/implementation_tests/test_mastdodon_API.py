from switch_media_downloader.APIs.mastodonAPI import MastodonAPI


def test_mastodon_basic():
        api = MastodonAPI(
                client_id="APPLICATION_ID_MASTODON",
                secret="SECRET_MASTODON",
                access_token="ACCESS_TOKEN_MASTODON",
                mastodon_instance="MASTODON_INSTANCE",
        )

        api.connect()

        assert api.client.account_verify_credentials().username == "ChaconMoon"


def test_mastodon_publish_image():
        api = MastodonAPI(
                client_id="APPLICATION_ID_MASTODON",
                secret="SECRET_MASTODON",
                access_token="ACCESS_TOKEN_MASTODON",
                mastodon_instance="MASTODON_INSTANCE",
        )

        api.connect()

        api.publish_images(
                msg="Estoy trabajando en un proyecto en Python que permitira publicar imagenes de la switch en Twitter, BlueSky y Mastodon sin necesidad de hacer una medificación a la consola",
                files=[
                        "./tests/test_media/2024100319575600-DB679239AE5C0DC0D5E47C22D6492D98.jpg"
                ],
                alt_text="Que mono es 9-Volt",
        )


def test_mastodon_publish_video():
        api = MastodonAPI(
                client_id="APPLICATION_ID_MASTODON",
                secret="SECRET_MASTODON",
                access_token="ACCESS_TOKEN_MASTODON",
                mastodon_instance="MASTODON_INSTANCE",
        )

        api.connect()

        api.publish_video(
                msg="En teoria esto se tendria que publicar en cuanto la URL del video exista es decir ya soy capaz de saber cuando el video esta subido, en teoria",
                file="./tests/test_media/Mario & Luigi Brothership 2024111516292701.mp4",
                alt_text="Que buen golpe",
        )
