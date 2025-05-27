### Configuration to post on BlueSky

Go to your [Bluesky profile’s privacy and security settings.](https://bsky.app/settings/privacy-and-security)

Access the "App passwords" section and generate a new key.  
![alt text](../.github/img/Generate_API_Key_Bluesky.png)

Copy that key and paste it into the `.env_example` file along with your username. Paste the API key into __BLUESKY_PRINCIPAL_API_KEY__ and your Bluesky username (without the @) into __BLUESKY_PRINCIPAL_NAME__, then rename the file to `.env`.

![alt text](../.github/img/Copy_API_Key_Bluesky.png)

![alt text](../.github/img/Paste_API_KEY_BlueSky.png)

If you want to test the connection, you can use the environment variables __BLUESKY_SECUNDARY_API_KEY__ and __BLUESKY_SECUNDARY_NAME__, and run the Bluesky tests on your account. These are alternative credentials in case you want to use a different account for testing.

```bash
poetry run pytest -v tests/implementation_tests/test_bluesky_API.py
```
