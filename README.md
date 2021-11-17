# 3기 도서관 대출 서비스 프로젝트

![waka](https://wakatime.com/badge/user/a1389358-644f-4cbf-80e6-9eeb4261e9f2/project/bf9ae3d9-8a78-45ad-91f8-b7a20afc568b.svg?style=for-the-badge)

## 사용 스택

|       범주       |            기술             |
| :--------------: | :-------------------------: |
|       배포       |           Heroku            |
|       개발       |  Python, Flask, SQLAlchemy  |
| 의존성 관리 도구 |           Pipenv            |
|  데이터 베이스   |    MySQL, SQLite (Test)     |
|    프론트엔드    |     JavaScript, jQuery      |
|      백엔드      | Flask, Gunicorn, SQLAlchemy |

## 설치

```zsh
# FLASK_APP 환경변수 추가
$ export FLASK_APP=run.py
 
# 미리 생성된 책 데이터 추가하기
$ flask init
```

## 환경변수

```ini
# Secret Key
SECRET_KEY='시크릿 키'

# ( 개발 DB  (data-dev.sqlite) | 테스트 DB (data-test.sqlite) | 배포 DB (data.sqlite) )
DEV_DATABASE_URL='DB 경로'
TEST_DATABASE_URL='DB 경로'
DATABASE_URL='DB 경로'

# 설정 ( development | testing | production )
FLASK_CONFIG='development'
```
