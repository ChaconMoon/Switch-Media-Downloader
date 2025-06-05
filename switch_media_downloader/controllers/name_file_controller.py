"""
Module: name_file_controller.py.

Description: Module that gets the downloaded file info.
Author: Carlos Chacón
Date: 29-05-2025.
"""

import re


def get_game_id(file_name: str) -> str | None:
        """
        Get the ID of a Game media file if the name of the file is correct.

        Args:
                file_name (str): The name of the File to get the ID.

        Returns:
                The ID of the Game if it Exists.

        """
        if re.search("\\d{16}-\\w{32}[.]{1}\\w{3}", file_name):
                return file_name.split("-")[-1].split(".")[0]
        return None


def get_file_name(url_file: str) -> str | None:
        """
        Get the name of the file to download if the url downloads a media file.

        Args:
                url_file: the url of the file.

        Returns:
                the name of the file if it correct.

        """
        if url_file is None:
                return None
        if (url_file.startswith(("http://", "https://"))) and (
                url_file.endswith((".mp4", ".jpg"))
        ):
                return url_file.split("/")[-1]
        return None
