from abc import ABC, abstractmethod


class WebBrowser(ABC):
    @abstractmethod
    def start_selenium(self):
        pass

    @abstractmethod
    def exit_selenium(self):
        pass
