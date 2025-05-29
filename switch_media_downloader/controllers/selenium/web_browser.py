"""
Module: web_browser.py.

Description: Web Browser Abstact Method
Author: Carlos Chacón
Date: 29-05-2025.
"""

# --- Import Abstact Class Module ---
from abc import ABC, abstractmethod


class WebBrowser(ABC):
        """Interface to create modules to connect to a Web Browser."""

        @abstractmethod
        def start_selenium(self):
                """Open the Web Browser with Selenium on the Switch Screenshot site."""

        @abstractmethod
        def exit_selenium(self):
                """Close Web Browser."""
