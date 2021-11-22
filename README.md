# 엘리스 3기 도서관 대출 서비스 프로젝트

<p align="center">
  <img src="https://wakatime.com/badge/user/a1389358-644f-4cbf-80e6-9eeb4261e9f2/project/bf9ae3d9-8a78-45ad-91f8-b7a20afc568b.svg?style=for-the-badge">
  <br><br><br>
  <a href="https://elice-book-rental.herokuapp.com/">DEMO</a>
  <br><br><br>
</p>

## TOC

- [엘리스 3기 도서관 대출 서비스 프로젝트](#엘리스-3기-도서관-대출-서비스-프로젝트)
  - [TOC](#toc)
  - [사용 스택](#사용-스택)
  - [디렉터리 구조](#디렉터리-구조)
  - [설치](#설치)
    - [환경변수](#환경변수)
  - [배포](#배포)
    - [헤로쿠에 배포하기](#헤로쿠에-배포하기)
  - [문서](#문서)

<br>


## 사용 스택

|       범주       |            기술             |
| :--------------: | :-------------------------: |
|       배포       |           Heroku            |
|       개발       |  Python, Flask, SQLAlchemy  |
| 의존성 관리 도구 |           Pipenv            |
|  데이터 베이스   |    MySQL, SQLite (Test)     |
|    프론트엔드    |     JavaScript, jQuery      |
|      백엔드      | Flask, Gunicorn, SQLAlchemy |

<br>

## 디렉터리 구조

```zsh
root
├── app
│   ├── auth # -> auth view
│   ├── main # -> main view
│   ├── mybook #-> mybook view
│   ├── models # -> db crud 로직 구현 코드
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
│   │   ├── macro # -> 자주 사용하는 진자 템플릿 함수
│   │   └── mybook # -> 대여기록, 대여한책
│   └── utility # -> helper 함수
├── docs
│   └── resource
│       └── book_image_resource
├── migrations # db migrations
│   └── versions
├── tests # -> 테스트 코드
└── utility
```

<br>

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

```

### 환경변수

```ini
# Secret Key
SECRET_KEY='시크릿 키'

# ( 개발 DB  (data-dev.sqlite) | 테스트 DB (data-test.sqlite) | 배포 DB (data.sqlite) )
DEV_DATABASE_URL='DB 경로'
TEST_DATABASE_URL='DB 경로'
DATABASE_URL='DB 경로'

# 설정 ( development | testing | production )
FLASK_CONFIG='development'
FLASK_APP='run.py'
```

<br>

## 배포

### 헤로쿠에 배포하기

```zsh
FLASK_CONFIG=production
DATABASE_URL=mysql+pymysql://id:pw@host:3306/database
SECRET_KEY=yoursecretkey

# dyno formation
web gunicorn -c ./gunicorn.config.py
```

## 문서

[프로젝트 구현 상황](/docs/todo.md)

[일일 회고](/docs/review.md)

[참고한 문서](/docs/reference.md)

<br>
