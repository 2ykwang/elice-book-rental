# 엘리스 3기 도서관 대출 서비스 프로젝트

![wakatime](https://wakatime.com/badge/user/a1389358-644f-4cbf-80e6-9eeb4261e9f2/project/bf9ae3d9-8a78-45ad-91f8-b7a20afc568b.svg?style=for-the-badge)

프로젝트 데모

[![heroku-img](https://img.shields.io/badge/-HEROKU-430098?logo=Heroku&style=for-the-badge)](https://elice-book-rental.herokuapp.com)

[![azure-img](https://img.shields.io/badge/-Azure-0078D4?logo=Microsoft-Azure&style=for-the-badge)](http://elice-kdt-3rd-vm-083.koreacentral.cloudapp.azure.com/)

REST API 문서

[![mdn-img](https://img.shields.io/badge/-REST_API_DOCS-000000?logo=MDN-Web-Docs&style=for-the-badge)](https://elice-book-rental.herokuapp.com/api)

---

## TOC

- [엘리스 3기 도서관 대출 서비스 프로젝트](#엘리스-3기-도서관-대출-서비스-프로젝트)
  - [TOC](#toc)
  - [개발 스택](#개발-스택)
    - [사용한 라이브러리](#사용한-라이브러리)
  - [디렉터리 구조](#디렉터리-구조)
  - [설치](#설치)
    - [환경변수](#환경변수)
  - [배포](#배포)
    - [헤로쿠에 배포하기](#헤로쿠에-배포하기)
  - [문서](#문서)

## 개발 스택

| 범주             |               기술                |
| :--------------- | :-------------------------------: |
| 배포 환경        |  Heroku, Ubuntu, Docker, Jenkins  |
| 개발             |           Python, Flask           |
| 의존성 관리 도구 |              Pipenv               |
| 데이터 베이스    |     MySQL, SQLite, SQLAlchemy     |
| 프론트엔드       |       JavaScript, bootstrap       |
| 백엔드           | Nginx, Gunicorn, Flask, Flask Cli |

### 사용한 라이브러리

| production       | development |
| :--------------- | :---------- |
| flask            | requests    |
| flask-wtf        | flake8      |
| flask-sqlalchemy | black       |
| sqlalchemy       | isort       |
| flask-login      |             |
| flask-migrate    |             |
| flask-restx      |             |
| gunicorn         |             |
| python-dotenv    |             |
| email-validator  |             |
| pymysql          |             |


## 디렉터리 구조

```zsh
root
├── app
│   ├── api # -> RESTApi 구현 코드
│   │   └── errors
│   ├── auth # -> auth view
│   ├── main # -> main view
│   ├── mybook #-> mybook view
│   ├── models # -> DB 모델
│   ├── services # -> 비즈니스로직 구현 코드
│   ├── static
│   │   ├── css
│   │   ├── images
│   │   ├── js
│   │   └── media
│   ├── templates
│   │   ├── auth # -> 로그인, 가입 템플릿
│   │   ├── errors # -> 404,500, ... 에러 페이지 템플릿
│   │   ├── layout # -> 웹 레이아웃
│   │   ├── macro # -> 자주 사용하는 jinja2 템플릿 함수
│   │   └── mybook # -> 대여기록, 대여한책
│   └── utility # -> helper 함수
├── docs # -> 프로젝트 개발에 관한 문서
├── migrations # db migrations
├── tests # -> 테스트 코드
└── utility
```

## 설치

```zsh
# FLASK_APP 환경변수 추가
$ export FLASK_APP=run.py

# 미리 생성된 책 데이터 추가하기
$ flask init

# 가상환경

# pipenv 사용
$ pipenv install
$ pipenv shell
$ pipenv update

# venv 사용
$ python3 -m venv .venv
$ pip install -r requirements.txt

# 실행
$ export FLASK_APP=run.py
$ flask run

# 테스트
$ python -m unittest
```

### 환경변수

```ini
# Secret Key
SECRET_KEY='secret key here'

# ( 개발 DB  (data-dev.sqlite) | 테스트 DB (data-test.sqlite) | 배포 DB (data.sqlite) )
# ex:) sqlite://path , mysql+pymysql://
DEV_DATABASE_URL='db path here'
TEST_DATABASE_URL='db path here'
DATABASE_URL='db path here'

FLASK_CONFIG='development' # 설정 ( development | testing | production )
FLASK_APP='run.py'
SERVER_NAME='server host here'
```

## 배포

### 헤로쿠에 배포하기

```zsh
FLASK_CONFIG=production
DATABASE_URL=mysql+pymysql://id:pw@yourdatabasehosthere:3306/database
SECRET_KEY=yoursecretkey
SERVER_NAME='your heroku domain' # ex:) naver.com, github.com
```


## 문서

[프로젝트 문서](/docs/)

[구현 상황](/docs/todo.md)

[일일 회고](/docs/review.md)

[참고한 문서](/docs/reference.md)
