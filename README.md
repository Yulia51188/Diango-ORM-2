# Bank security control system

Bank security control system is a web-site realized with Django that provides security database view and analyze. It warns the security if someone is being in storage too long or passcard is inactive.

### How to install

You need to set some keys as environment variable that are:
- security database information: engine, name, host, port number, username and password as  `DB_ENGINE`, `DB_NAME`,`DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`;
- secret key as `SECRET_KEY`.

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```

### How to launch

Run local web server to try it from command line with `python` or `python3`:

```bash
$ python manage.py runserver 0.0.0.0:8000
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).