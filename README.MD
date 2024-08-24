# SDA Backend tutorial

## Setup

### Nastavenie virtual env

Pridaj package do projektu
```bash
poetry add <package>
...
poetry add django
```

Nainstaluj dependencies
```bash
poetry install
```

Sprav migracie
```bash
python manage.py migrate
```

Aktivuje sa virtual environment
```bash
poetry shell
```

Jednorazove spustenie prikazu pod virtual environmentom
```bash
poetry run <command>
```

## Django commands

Vytvorenie projektu
```bash
django-admin startproject <mysite>
```

Vytvorenie aplikacie
```bash
python manage.py startapp <appname>
```

Spustenie serveru
```bash
python manage.py runserver
```

Vytvorenie migracnych suborov
```bash
python manage.py makemigrations ?<appname>
```

Migracia db na zaklade migracnych suborov
```bash
python manage.py migrate ?<appname>
```

Revert migracie
```bash
python manage.py migrate <appname> <id_migracie>
```

Revert migracie az na inicialny stav
```bash
python manage.py migrate <appname> zero
```

Zobrazenie aplikovanych migracii
```bash
python manage.py showmigrations
```

Vytvorenie super usera (admina)
```bash
python manage.py createsuperuser
```

Dump databazy do `.json` suboru
```bash
python manage.py dumpdata viewer --output fixtures.json
```

Nacitanie databazy z `.json` suboru
```bash
python manage.py loaddata fixtures.json
```

Interaktivny rezim, ktory ma naloadovane django prostredie
```bash
python manage.py shell
```
