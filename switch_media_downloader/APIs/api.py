"""
Module: api.py.

Description: Interface to the different API modules.
Author: Carlos Chacón
Date: 09-03-2025.
"""

# --- Interface Dependence ---
from abc import ABC, abstractmethod


class Api(ABC):
        """
        Defines the methods for all the different APIs.

        Methods:
            connect(): Defines the method to connect to the API
            publish_image(): Define the method used to publish a image in the social media
            publish_video(): Define the method used to publish a video in social media.
            publish_text(): Define a method to publish a text post in the social media.
            view_preview(): Define the method to preview the post before publish it.

        """

        @abstractmethod
        def connect(self) -> bool:
                """
                Connect to your this social media account.

                Returns:
                    If the connection was Successful

                """

        @abstractmethod
        def publish_images(self, msg: str, files: list[str], alt_text: str) -> bool:
                """
                Publish an image in this social media account.

                Args:
                    msg (str): The text of the post
                    files (list[str]): The path of the nintendo switch's image
                    alt_text (str): The alterative text of the nintendo switch's image
                Returns:
                    If the image is published

                """

        @abstractmethod
        def publish_video(self, msg: str, files: str, alt_text: str) -> bool:
                """
                Publish a video in this social media account.

                Args:
                    msg (str): The text of the post
                    files (list[str]): The path of the nintendo switch's video
                    alt_text (str): The alterative text of the nintendo switch's video
                Returns:
                    If the video is published

                """

        @abstractmethod
        def publish_text(self, msg: str) -> bool:
                """
                Publish a single post text-only in this social media.

                Args:
                    msg (str): The text of the post
                Returns:
                    if the post is published

                """

        @abstractmethod
        def view_preview(self, msg: str, file: str, alt_text: str) -> bool:
                """
                Print a preview of the post before publish it.

                Args:
                    msg (str): The text of the post's preview
                    file (str): The file of the post's preview
                    alt_text (str): the text of the file of the post

                """
