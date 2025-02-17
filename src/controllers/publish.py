from APIs.bluesky import BlueSky
from APIs.twitter import Twitter
from APIs.api import Api
from dotenv import load_dotenv
import os


def selectAPIs() -> Api:
    load_dotenv()
    match input("Donde deseas publicar: Bluesky(B)/Twitter(T): "):
        case "B":
            bluesky = BlueSky("BLUESKY_SECUNDARY_NAME", "BLUESKY_SECUNDARY_API_KEY")
            bluesky.connect()
            return bluesky
        case "T":
            twitter = Twitter(
                os.getenv("TWITTER_PRIMARY_API_KEY"),
                os.getenv("TWITTER_PRIMARY_API_SECRET_KEY"),
                os.getenv("TWITTER_PRIMARY_ACCESS_TOKEN"),
                os.getenv("TWITTER_PRIMARY_ACCESS_TOKEN_SECRET"),
                os.getenv("TWITTER_BEARER_TOKEN"),
            )
            twitter.connect()
            return twitter
