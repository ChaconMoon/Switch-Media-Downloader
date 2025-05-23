from switch_media_downloader.controllers.hashtag_controller import set_game_hashtag

# METHOD SET_GAME_HASHTAG_TEST


# VALIDE ID TEST
def test_hashtag_get_valid_name():
        assert set_game_hashtag("B6CE40797459B0890BF7CEF68A4CE587") == "#PokemonPurpura"


# INVALIDE ID TEST
def test_hashtag_get_invalide_name():
        assert set_game_hashtag("AAAAAAAAAAAAAA") is None


# NULL TEST
def test_hashtag_get_name_none():
        assert set_game_hashtag(None) is None
