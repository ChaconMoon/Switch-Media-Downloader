from switch_media_downloader.controllers.selenium.firefox import Firefox


def test_start_selenium_connection_firefox():
        firefox_connection = Firefox()

        assert firefox_connection.start_selenium() is True


def test_exit_selenium_connection_firefox():
        firefox_connection = Firefox()
        firefox_connection.start_selenium()
        assert firefox_connection.exit_selenium() is True
