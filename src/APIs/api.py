from abc import ABC, abstractmethod
from atproto import Client as ATClient
from tweepy import Client as TWClient
class Api(ABC):
    @abstractmethod
    def connect(self) -> bool:
        """
        Connect to your this social media account

        Returns:
            The Client of the this social media connection

        """
        pass

    @abstractmethod
    def publish_image(self, msg: str, file: str, alt_text: str, client: ATClient | TWClient) -> bool:
        """
        Publish an image in this social media account

        Args:
            msg: The text of the post
            file: The path of the nintendo switch's image
            alt: The alterative text of the nintendo switch's image
            client: The social media client with the session
        Returns:
            If the image is published
        """
        pass

    @abstractmethod
    def publish_video(self,msg: str, file: str, alt_text: str, client: ATClient | TWClient) -> bool:
        """
        Publish a video in this social media account

        Args:
            msg: The text of the post
            file: The path of the nintendo switch's video
            alt: The alterative text of the nintendo switch's video
            client: The ATProto client with the BlueSky session
        Returns:
            If the video is published
        """
        pass

    @abstractmethod
    def publish_text(self, msg: str) -> bool:
        """
        Publish a single post text-only in this social media

        Args:
            msg: The text of the post
        Returns:
            if the post is published
        """
        pass

    @abstractmethod
    def view_preview(self, msg: str, file: str, alt_text: str) -> bool:
        """
        Print a preview of the post before publish it.

        Args:
            msg: The text of the post's preview
            file: The file of the post's preview
            alt_text: the text of the file of the post
        """
        pass