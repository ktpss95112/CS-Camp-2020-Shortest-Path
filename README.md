* setup: `pip3 install Flask gunicorn`
* run: `gunicorn --bind 0.0.0.0:8786 -w 8 wsgi:app`
