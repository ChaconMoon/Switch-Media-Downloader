import pytest
from APIs.bluesky import BlueSky
from unittest.mock import MagicMock, patch
from atproto.exceptions import AtProtocolError

# Función a parcher, se parchea de arriba a abjo en orden inverso a los @patch
@patch("APIs.bluesky.Client.login")
def test_connection_is_none_if_ATProtocolError(mock_client: MagicMock):

    #Provoca que la funcion mockeada salte una excepción
    mock_client.side_effect = AtProtocolError
    connector_bluesky = BlueSky()
    assert connector_bluesky.connect() is None    

