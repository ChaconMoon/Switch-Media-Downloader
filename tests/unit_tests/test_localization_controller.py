from switch_media_downloader.controllers.string_localization import StringLocalization


def test_localization():
        test_string = StringLocalization().get_localizated_string(
                "bluesky_connection_text_1"
        )

        assert test_string == "Connecting..." or test_string == "Connectando..."
