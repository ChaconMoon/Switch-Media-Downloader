# Getting Started

Este documento contiene una guia sobre la instalación y uso basico del programa.

## Requisitos:

Sistema con Windows y Python de 3.12.5 a 3.13 (No funciona en Linux por problemas de privilegios debido a que para trabajar con las interfaces de red en Linux hacen falta privilegios de administrador y no quiero pedir un superusuario para este programa).

Poetry versión 2.1.1 o superior [Enlace de instalación](https://python-poetry.org/docs/)

Una conexión a redes mediante Wi-Fi (Para conectarte con la Nintendo Switch)

(Opcional) Una conexión por red cableada como secundaria de la red Wi-Fi.

## Instalación con Poetry (Recomendado)

Clona este repositorio (Con HTTPS):
```bash
git clone https://github.com/ChaconMoon/Switch-Media-Downloader.git
```

OR

Clona este repositorio (Con SSH):
```bash
git clone git@github.com:ChaconMoon/Switch-Media-Downloader.git
```

Muevete a la carpeta del repositorio:
```bash
cd Switch-Media-Downloader
```

Activa el entorno virtual de Poetry.
```bash
poetry env activate
```

Ejecuta el fichero que devuelve el comando:

__Ejemplo__

```bash
C:\Users\Pc\AppData\Local\pypoetry\Cache\virtualenvs\switch-media-downloader-jPGjUOqm-py3.13\Scripts\Activate.ps1
```

Instala las dependencias del proyecto:
```bash
poetry install
```

Ejecuta el progrma como un modulo de Python.
```bash
python -m switch_media_downloader
```

## Instalación usando el pip

Descarga la ultima versión del paquete en las Realeses de GitHub.

Instala el paquete usando pip.

```bash
python -m pip install .\switch_media_downloader-0.1.0-py3-none-any.whl
```

Ejecuta el progrma como un modulo de Python.
```bash
python -m switch_media_downloader
```

## Ejecución.
Este programa puede usarse con parametros para automatizar su ejecución o con un menú dentro de este.

### Con parametros.
Estos son los parametros que se le pueden pasar al programa para automatizar su funcionamiento.

```
| Parámetro          | Descripción                                                  |
|--------------------|--------------------------------------------------------------|
| `-h`, `--help`     | Muestra los parámetros disponibles                           |
| `-p`, `--password` | Contraseña de la red Wi-Fi                                   |
| `-v`, `--video`    | Descarga un video (mutuamente excluyente con `--image`)      |
| `-i`, `--image`    | Descarga imágenes (mutuamente excluyente con `--video`)      |
| `--post`, `--msg`  | Texto del post para redes sociales                           |
| `-m`, `--mastodon` | Publica en Mastodon                                          |
| `-t`, `--twitter`  | Publica en Twitter (X)                                       |
| `-b`, `--bluesky`  | Publica en Bluesky                                           |
| `--hashtag`        | Hashtag a incluir en la publicación si está definido         |

```

Ejemplo de uso:

```bash
python -m switch_media_downloader -p dif875n7 -v --post "Poco a poco voy aprendiendo a luchar mejor, es mejor no jugarsela en un duelo de piedra-papel-tijera" -b --hashtag
```

Este ejemplo establece que la contraseña de la switch es dif875n7, que tiene que descargar un video y que debe publicarla en bluesky con el siguiente texto: Poco a poco voy aprendiendo a luchar mejor, es mejor no jugarsela en un duelo de piedra-papel-tijera #Nombredeljuego

![](../.github/img/examples/Execution_With_Params_Example.png)
### Sin parametros.

Si prefieres hacer una ejecución manual puedes ejecutar el modulo sin parametros y deberas insertar todos los parametros manualemnte durante la ejecución.

![](../.github/img/examples/Execution_Without_Params_Example.png)

Si se desea insertar algún parametro en la ejecución como la contraseña se puede hacer y ese parametro se insertara automaticcamente en lugar de pedirlo al usuario.

![](../.github/img/examples/Example_With_Password_Param.png)
