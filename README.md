# pokerfacowaty.com

This is the Django-based pokerfacowaty.com website. This repository does not include the SQLite database file holding most of the website's content.

## Dependecies:
- `Django >= 4.2`
- `paml2html >= 0.1.1`
- `python-dotenv >= 1.0.0`

## Installation:
- With Docker
    - Make sure Docker is installed on your system
    - Clone the repo with `git clone https://github.com/PokerFacowaty/django-pokerfacowaty-com` and enter its directory
    - Edit `docker-compose.yml` and setup environment variables and optionally attach volumes and change the port routing
        - An example environment variables config can be seen below:
        ```
        - ALLOWED_HOSTS=[".pokerfacowaty.com"]
        - CSRF_TRUSTED_ORIGINS=["https://*.pokerfacowaty.com"]
        - CSRF_COOKIE_SECURE=True
        - DEBUG=False
        - MC_LOG_DIR=/mc/server.log
        - PLAYLIST_CSV_DIR=/playlists/
        - SECRET_KEY=3ZV$HLGUqJj8Lh#dgb86dke$TSF7R&J*R@3F49m^k#sVpJNFX&
        - SESSION_COOKIE_SECURE=True
        - STATIC=static/
        - STATIC_ROOT=/static/
        ```
    - Run `docker compose up -d` to build and run the container in detached mode or omit the `-d` option to attach to it once it's running

 Remember that **you need a web server (NGINX, Apache or other) to serve static files** from STATIC_ROOT onto the STATIC location of your domain in a production environment (Django only serves static files with DEBUG set to True).

- With Poetry:
    - Make sure you have [Poetry](https://python-poetry.org/) installed
    - Clone the repo with `git clone https://github.com/PokerFacowaty/django-pokerfacowaty-com` and enter its directory
    - Set up environment variables as seen in the Docker example or make a `.env` file at the repo's root directory and list them there
    - Run `poetry install --no-root`
    - Once it's installed, migrate all the models into the database with `poetry run python3 manage.py migrate` and move all the static files to STATIC_ROOT with `poetry run python3 manage.py collectstatic --no-input --clear`
        - `python3` might be named differently on your system
    - Start the server by running `poetry run python3 manage.py runserver 0.0.0.0:8000` replacing `8000` with the port you want to run the server on