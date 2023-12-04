# project_supbot

# 목차
1.[목표와 기능](#1-목표와-기능)<br>
2.[개발 환경 및 배포 URL](#2-개발-환경-및-배포-URL)<br>
3.[요구사항 명세와 기능 명세](#3-요구사항-명세와-기능-명세)<br>
4.[프로젝트 구조와 개발 일정](#4-프로젝트-구조와-개발-일정)<br>
5.[와이어프레임 / UI / BM](#5-와이어프레임-/-UI-/-BM)<br>
6.[데이터베이스 모델링 ERD](#6-데이터베이스-모델링-ERD)<br>
7.[메인기능](#8-메인기능)<br>
8.[트러블슈팅](#9-트러블슈팅)<br>

# 1. 목표와 기능

## 1.1 목표
- 다양한 분야의 지식을 채팅 형식으로 간편하게 제공 받을 수 있는 서비스
- 필요한 정보를 문서 형식에 맞추어 정리해주는 서비스

## 1.2 기능
- ChatGPT를 이용한 인공지능 챗봇과 대화하기
- 개발 코드 작성 및 수정 기능
- 원하는 내용으로 문서 작성 기능

## 1.3 팀구성

- 이창현

# 2. 개발 환경 및 배포 URL

## 2.1 기술스택

 <div align=center>
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
<br>

<img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
<img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white">
<img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">
</div>

## 2.2 배포 URL
-

# 3. 요구사항 명세와 기능 명세

## 3.1 프로젝트 시각화 다이어그램
![image](https://github.com/abcdqwer1/project_chatbot/assets/68181016/8bf9c8cc-b6cf-4537-a265-6529095b5a81)
[다이어그램](https://www.mindmeister.com/app/map/3048013454)

## 3.2 API 기능 명세
![image](https://github.com/abcdqwer1/project_chatbot/assets/68181016/93e417cc-0ee3-45c3-849f-bca9ddead6e8)


# 4. 프로젝트 구조와 개발 일정

## 4.1 디렉토리 구조
```
📦project_chatbot
 ┣ 📂accounts
 ┃ ┣ 📂migrations
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂FE
 ┃ ┣ 📜index.html
 ┃ ┣ 📜main.html
 ┃ ┗ 📜signup.html
 ┣ 📂main
 ┃ ┣ 📂migrations
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜permissions.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂static
 ┣ 📂supbot
 ┃ ┣ 📜.env
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜__init__.py
 ┣ 📜.env
 ┣ 📜.gitignore
 ┣ 📜db.sqlite3
 ┣ 📜manage.py
 ┣ 📜README.md
 ┣ 📜requirements.txt
```

## 4.2 개발일정 WBS
![image](https://github.com/abcdqwer1/project_chatbot/assets/68181016/26411676-51d8-4474-a703-3aa86a343285)
[WBS](https://docs.google.com/spreadsheets/d/1HUmwb7SyYOoIv7Qe0IFBOewYOp_OuIi2c5rJhsXY69Y/edit#gid=0)

# 5. UI 

# 6. 데이터베이스 모델링 ERD
![image](https://github.com/abcdqwer1/project_chatbot/assets/68181016/e5b7caa7-2fcf-461e-ad37-802a859f0b0c)

[project_supbot ERD](https://dbdiagram.io/d/6568a3ba3be1495787104795)

# 7. 메인기능

- CRUD 기능 (main app에 viewsets으로 구현)
 <br>

- 회원가입
  - accounts app에 UserViewSet(viewsets.ModelViewSet)에 구현
![image](https://github.com/abcdqwer1/project_chatbot/assets/68181016/e453e175-71b7-44f6-b928-2c7007f04a18)
<br>

- jwt 토큰 (simplejwt 사용)
![image](https://github.com/abcdqwer1/project_chatbot/assets/68181016/fc0ab00a-b5e4-4338-8f03-1584f9b1e15a)
<br>

- swagger (drf_spectacular 사용)
<br>


# 8. 트러블슈팅

## 1번째. openai 구버전에서 사용하던 코드로 인한 에러


You tried to access openai.Completion, but this is no longer supported in openai>=1.0.0 - see the README at https://github.com/openai/openai-python for the API.  
You can run `openai migrate` to automatically upgrade your codebase to use the 1.0.0 interface.
Alternatively, you can pin your installation to the old version, e.g. `pip install openai==0.28`
A detailed migration guide is available here: https://github.com/openai/openai-python/discussions/742


### 해결 방법 1.
- gpt 연동시 에러가 발생하여 로그에 찍힌 내용대로 openai migrate 를 시도 해봤지만 아래와 같은 에러가 나오며 실패했다.

$> openai migrate
Error: Windows is not supported yet in the migration CLI


### 해결 방법 2. 
openai 버전을 낮추라는 말이 있었지만 버전을 낮추는건 좋지 않아보여 일단 github에 있는 openai readme.md를 확인해보니 사용 코드가 변경된 걸 발견했다.


문제로 보이는 부분을 아래와 같이 변경 한 후 정상으로 확인되었다.


openai.Completion.create -> client.chat.completions.create


## 2번째. OPTIONS 메소드, CORS (Cross-Origin Resource Sharing) 설정문제


post를 요청하면 로그에는 "OPTIONS /Conversation/chatbot/ HTTP/1.1" 200 0 만 찍히고 아무런 동작을 하지않아 문제였다.


확인해보니 프론트서버에서 백엔드서버로 리소스를 요청할때 CORS에 의해 발생하는 문제였다.


CORS에 대해 찾아보니 서로 다른 도메인 간 요청시 보안 정책으로 인해 프론트와, 백엔드가 같은 서버에 있더라도 사용하더라도 IP, 포트, 프로토콜가 전부 같지 않으면 해당 정책이 적용되는것으로 보였다.


- CORS? 리소스 공유 정책(Cross Origin Resource Sharing) 한 도메인의 웹 페이지가 다른 도메인 (도메인 간 요청)을 가진 리소스에 액세스 할 수 있게하는 보안 메커니즘이다.


### 해결 방법. 


클라이언트 요청시 해결 할 수 있는 방법이 있다고 하는데 가장 많이 사용하는 방법으로 보이는 CORS_ALLOW_ALL_ORIGINS = True 설정을  백엔드 서버에서 해주니 해결 되었다.


아래처럼 사용 할 수도 있다고 한다.

```
# URL 목록 입력
CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000",
]

# 정규 표현식 사용
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://\w+\.example\.com$",
]
```

## 3번째. djangorestframework-jwt 사용시 임포트 에러


ImportError: Could not import 'rest_framework_jwt.authentication.JSONWebTokenAuthentication' for API setting 'DEFAULT_AUTHENTICATION_CLASSES'. ImportError: cannot import name 'smart_text' from 'django.utils.encoding'


### 해결 방법.


djangorestframework-jwt 라이브러리는 장고 3.x 버전까지 지원하지만 이번 프로젝트에서 사용하는 장고 버전은 4.2.7라서 발생하는 에러였다.


대안으로 drf-jwt 라이브러리와 djangorestframework-simplejwt 라이브러리가 있다고하여 simplejwt를 사용하여 해결하였다.
