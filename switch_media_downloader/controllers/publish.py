from dotenv import load_dotenv

from switch_media_downloader.APIs.api import Api
from switch_media_downloader.APIs.bluesky import BlueSky
from switch_media_downloader.APIs.mastodonAPI import MastodonAPI
from switch_media_downloader.APIs.twitter import Twitter
from switch_media_downloader.controllers.string_localization import StringLocalization


def selectAPIs(option="") -> Api:
        load_dotenv()
        match option:
                case "B":
                        bluesky = BlueSky(
                                "BLUESKY_PRINCIPAL_NAME", "BLUESKY_PRINCIPAL_API_KEY"
                        )
                        bluesky.connect()
                        print(
                                StringLocalization().get_localizated_string(
                                        "bluesky_succesful_connection_text"
                                )
                        )
                        return bluesky
                case "T":
                        twitter = Twitter(
                                "TWITTER_PRIMARY_API_KEY",
                                "TWITTER_PRIMARY_API_SECRET_KEY",
                                "TWITTER_PRIMARY_ACCESS_TOKEN",
                                "TWITTER_PRIMARY_ACCESS_TOKEN_SECRET",
                                "TWITTER_BEARER_TOKEN",
                        )
                        print(
                                StringLocalization()
                                .get_localizated_string(
                                        "twitter_succesful_connection_text"
                                )
                                .format(twitter.connect())
                        )
                        return twitter
                case "M":
                        mastodon = MastodonAPI(
                                client_id="APPLICATION_ID_MASTODON",
                                secret="SECRET_MASTODON",
                                access_token="ACCESS_TOKEN_MASTODON",
                                mastodon_instance="MASTODON_INSTANCE",
                        )
                        mastodon.connect()
                        print(
                                StringLocalization()
                                .get_localizated_string(
                                        "twitter_succesful_connection_text"
                                )
                                .format(
                                        mastodon.client.account_verify_credentials().username
                                )
                        )
                        return mastodon
