from unittest.mock import MagicMock, patch

from atproto.exceptions import AtProtocolError

from switch_media_downloader.APIs.bluesky import BlueSky


# Función a parcher, se parchea de arriba a abjo en orden inverso a los @patch
@patch("switch_media_downloader.APIs.bluesky.Client.login")
def test_connection_is_none_if_atprotocolerror(mock_client: MagicMock):
        # Provoca que la funcion mockeada salte una excepción
        mock_client.side_effect = AtProtocolError
        connector_bluesky = BlueSky("BLUESKY_SECUNDARY_NAME", "BLUESKY_SECUNDARY_API_KEY")
        assert connector_bluesky.connect() is False
