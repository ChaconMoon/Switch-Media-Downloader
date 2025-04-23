from APIs.bluesky import BlueSky
from APIs.twitter import Twitter
from APIs.mastodonAPI import MastodonAPI
from APIs.api import Api
from dotenv import load_dotenv


def selectAPIs(option="") -> Api:
    load_dotenv()
    if option == "":
        option = input("Donde deseas publicar: Bluesky(B)/Twitter(T)/Mastodon(M): ")
    match option:
        case "B":
            bluesky = BlueSky("BLUESKY_SECUNDARY_NAME", "BLUESKY_SECUNDARY_API_KEY")
            bluesky.connect()
            print("Conexión conseguida: con BlueSky")
            return bluesky
        case "T":
            twitter = Twitter(
                "TWITTER_PRIMARY_API_KEY",
                "TWITTER_PRIMARY_API_SECRET_KEY",
                "TWITTER_PRIMARY_ACCESS_TOKEN",
                "TWITTER_PRIMARY_ACCESS_TOKEN_SECRET",
                "TWITTER_BEARER_TOKEN",
            )
            print(f"Conexión conseguida: {twitter.connect()}")
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
                f"Conexión estalecida: {mastodon.client.account_verify_credentials().username}"
            )
            return mastodon
