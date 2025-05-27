## Program Structure
```
Switch-Media-Downloader
    ├── LICENSE # LICENCE Document
    ├── README.md # README
    ├── poetry.lock # Poetry Lock file
    ├── pyproject.toml # Project Config
    ├── pytest.ini # Pytest config
    ├── switch_media_downloader # Module Folder
    │   ├── APIs # Social Media APis Module
    │   │   ├── __init__.py
    │   │   ├── api.py
    │   │   ├── bluesky.py
    │   │   ├── mastodonAPI.py
    │   │   └── twitter.py
    │   ├── __init__.py
    │   ├── __main__.py # Project Main Module
    │   ├── controllers # File Downloader controller
    │   │   ├── __init__.py
    │   │   ├── downloads.py
    │   │   ├── hashtag_controller.py
    │   │   ├── name_file_controller.py
    │   │   ├── publish.py
    │   │   └── selenium # Selenium Module
    │   │       ├── __init__.py
    │   │       ├── edge.py
    │   │       ├── firefox.py
    │   │       └── web_browser.py
    │   ├── data # Game Data Folder
    │   │   ├── game_hashtag_en.json
    │   │   ├── game_hashtag_es.json
    │   │   └── game_titles.json
    │   └── switch # Switch Connector Modulw
    │       ├── __init__.py
    │       ├── connector.py
    │       └── downloaders
    │           ├── __init__.py
    │           ├── image.py
    │           └── video.py
    └── tests # Test Folder
        ├── implementation_tests
        │   ├── test_bluesky_API.py
        │   ├── test_downloads.py
        │   ├── test_edge.py
        │   ├── test_firefox.py
        │   ├── test_mastdodon_API.py
        │   ├── test_switch_connections.py
        │   └── test_twitter_API.py
        ├── integration_tests
        │   └── test_download_upload_image_video.py
        ├── test_media
        │   ├── 2024100319575600-DB679239AE5C0DC0D5E47C22D6492D98.jpg
        │   ├── Mario & Luigi Brothership 2024111516292701.mp4
        │   ├── placeholder_testing.jpg
        │   └── video_testing.mp4
        └── unit_tests
            ├── test_api_code.py
            ├── test_file_system.py
            ├── test_hashtag_controllers.py
            └── test_name_file_controller.py
```

