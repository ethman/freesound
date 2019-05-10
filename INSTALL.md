Installing FreeSound for QBV work at IAL
----------------------------------------


1. Create a settings file. There must be a file called `freesound/local_settings.py`. There is an example one at `freesound/local_settings.example.py`.

    1. Add a secret key to `local_settings.py`.
    2. Comment out the `dsn` entry in `RAVEN_CONFIG`.

2. Create a logger file. There must be a file called `freesound/logger.py` that contains a dictionary named `LOGGER`. There is an example one at `freesound/logger.example.py`.

    1. Add a valid path to a logging file to `logger.LOGGING['handlers']['file']['filename']`.
    
3. Create a similarity settings file. There must be a file called `similarity/similarity_settings.py`. There is an example one at `similarity/similarity_settings.example.py`.

4. Create a tag recommendation settings file. There must be a file called `tagrecommendation/tagrecommendation_settings.py`. There is an example one at `tagrecommendation/tagrecommendation_settings.example.py`.

5. Install `postgres v9.5`. Linux: `sudo apt-get install postgres-9.5`, Mac: `brew install postgres` (or install from the website).

6. Run `python manage.py makemigrations`.

7. Run `python manage.py migrate`.

8. To run the server use this command: `python manage.py runserver 127.0.0.1:8000`.