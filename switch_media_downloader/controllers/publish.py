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
                "TWITTER_PRIMARY_API_KEY",
                "TWITTER_PRIMARY_API_SECRET_KEY",
                "TWITTER_PRIMARY_ACCESS_TOKEN",
                "TWITTER_PRIMARY_ACCESS_TOKEN_SECRET",
                "TWITTER_BEARER_TOKEN",
            )
            print(f"Conexion conseguida: {twitter.connect()}")
            return twitter
