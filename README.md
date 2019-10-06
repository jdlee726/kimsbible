# KIMSBIBLE Application

This contains the KIMSBIBLE Application in development.
This app is mainly based on the Flask and the ETCBC 4C Database.

For the details of the Database set, please see the following link: [ETCBC 4C(Processed by Text-Fabric)](https://etcbc.github.io/text-fabric-data/features/hebrew/etcbc4c/0_home.html)

# Links
- https://app.alphalef.com
- https://github.com/kungsik/kimsbible
- https://alphalef.slack.com

# Build from source code
- install python3, pycharm
- 환경변수 `PYTHONPATH=D:\work\proj_other` 추가
- `cd %PYTHONPATH%`
- `kimsbible` 이라는 이름으로 flask project 생성
- `cd kimsbible`
- `git clone https://github.com/jdlee726/text-fabric-data.git`
- `git clone https://github.com/kungsik/kimsbible.git .`
- `git clone https://github.com/jdlee726/kimsbible.git .` (forked version)
- pip install
```
pip install text-fabric
pip install flask-login
```
- rename lib/config.sample.py to lib/config.py
