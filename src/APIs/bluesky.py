from atproto import Client
from atproto.exceptions import AtProtocolError
from atproto_client.models.app.bsky.embed.defs import AspectRatio
import os
from dotenv import load_dotenv
from APIs.api import Api 

class BlueSky(Api):
    client = Client()

    def __init__(self, account:str,token:str):
        self.account = account
        self.token = token
        pass
    def __str__(self):
        return f"{self.account,self.client}"


    def connect(self) -> bool:
        """
        Overrides Api.connect()
        """
        load_dotenv()
        try:
            print("Conectando...")
            self.client.login(self.account,self.token)
            print("Conexion exitosa")
            return True
        except AtProtocolError:
            print("Error en el inicio de sesión en BlueSky")
            return False
        except ValueError:
            print("Error a la hora de importar las credenciales")
            return None


    def publish_image(self, msg: str, file: str, alt_text: str) -> bool:
        with open(file, "rb") as f:
            photo = f.read()
            aspect_ratio = AspectRatio(width=1280, height=720)
        try:
            self.client.send_image(
                text=msg, image=photo, image_alt=alt_text, image_aspect_ratio=aspect_ratio
            )
            return True
        except AtProtocolError:
            print("Error en ATProto, la imagen no ha sido publica")
            return False


    def publish_video(self,msg: str, file: str, alt_text: str) -> bool:
        with open(file, "rb") as v:
            video = v.read()
            aspect_ratio = AspectRatio(width=1280, height=720)

        try:
            self.client.send_video(
                text=msg, video=video, video_alt=alt_text, video_aspect_ratio=aspect_ratio
            )
            return True
        except AtProtocolError:
            print("Error en ATProto, el video no se ha publicado")
            return False
    def publish_text():
        pass

    def view_preview():
        pass