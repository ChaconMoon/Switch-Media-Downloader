import unittest
from APIs_Modules.bluesky_api import connect_bluesky, publish_image
from atproto import Client


class TestBlueSkyAPI(unittest.TestCase):
    def test_bluesky_connection(self):
        self.assertEqual(
            type(connect_bluesky()), type(Client()), "Se ha podido iniciar sesión"
        )

    def test_publish_image(self):
        self.assertEqual(
            publish_image(
                msg="Esta imagen esta siendo usada con fines de testeo",
                file="./img/placeholder_testing.jpg",
                alt_text="Esta imagen esta siendo usada con fines de testeo.",
                client=connect_bluesky(),
            ),
            True,
            "La imagen se ha publicada correctamente.",
        )


if __name__ == "__main__":
    unittest.main()
