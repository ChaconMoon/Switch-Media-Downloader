### Configuración para publicar en BlueSky.

Dirijase a la [configuración de privacidad y seguiridad de tu perfil de Bluesky.](https://bsky.app/settings/privacy-and-security)

Acceda a la sección de App passwords y genera una nueva clave.
![alt text](../.github/img/Generate_API_Key_Bluesky.png)

Copia esa clave y pegala en el fichero .env_example junto con su nombre de usuario y cambia su nombre a .env.

![alt text](../.github/img/Copy_API_Key_Bluesky.png)

En el fichero .env_example pega este Token en BLUESKY_PRINCIPAL_API_KEY y en BLUESKY_PRINCIPAL_NAME pega tu nombre de usuario de bluesky sin el arroba.

![alt text](../.github/img/Paste_API_KEY_BlueSky.png)

Si quieres probar la conexión puedes usar las variables de entorno BLUESKY_SECUNDARY_API_KEY y en BLUESKY_SECUNDARY_NAME y ejecutar los test de bluesky parqa enviar un test a tu cuenta, son otras claves por si para hacer tests quieres usar otra cuenta para los tests.

```bash
poetry run pytest -v tests/implementation_tests/test_bluesky_API.py
```


