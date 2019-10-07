# KIMSBIBLE Application

This contains the KIMSBIBLE Application in development.
This app is mainly based on the Flask and the ETCBC 4C Database.

For the details of the Database set, please see the following link: [ETCBC 4C(Processed by Text-Fabric)](https://etcbc.github.io/text-fabric-data/features/hebrew/etcbc4c/0_home.html)

# Links
- https://app.alphalef.com
- https://github.com/kungsik/kimsbible
- https://alphalef.slack.com

# Build from source code
- prerequisites
  - mysql server, create tables
  - install python3, pycharm
  - 환경변수 `PYTHONPATH=D:\work\proj_python` 추가
- `cd %PYTHONPATH%`
- `git clone https://github.com/jdlee726/kimsbible.git`
- `cd kimsbible`
- `git clone https://github.com/jdlee726/text-fabric-data.git`
- pip install
```
pip install text-fabric
pip install flask-login flask_mail flask_dance
pip install bs4 whoosh
```
- create and edit lib/config.py from lib/config.sample.py
- edit oauth.py
- start flask server
