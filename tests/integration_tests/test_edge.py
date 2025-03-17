from switch_media_downloader.controllers.selenium.edge import Edge


def test_start_selenium_connection_edge():
    edge_connection = Edge()

    assert edge_connection.start_selenium() is True


def test_exit_selenium_connection_edge():
    edge_connection = Edge()
    edge_connection.start_selenium()
    assert edge_connection.exit_selenium() is True
