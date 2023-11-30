# project_supbot

# 목차
1.[목표와 기능](#1-목표와-기능)<br>
2.[개발 환경 및 배포 URL](#2-개발-환경-및-배포-URL)<br>
3.[요구사항 명세와 기능 명세](#3-요구사항-명세와-기능-명세)<br>
4.[프로젝트 구조와 개발 일정](#4-프로젝트-구조와-개발-일정)<br>
5.[와이어프레임 / UI / BM](#5-와이어프레임-/-UI-/-BM)<br>
6.[데이터베이스 모델링 ERD](#6-데이터베이스-모델링-ERD)<br>
7.[아키텍쳐](#7-아키텍쳐)<br>
8.[메인기능](#8-메인기능)<br>
9.[트러블슈팅](#9-트러블슈팅)<br>
10.[개발하며 느낀점](#10-개발하며-느낀점)

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

## 2.3 URL 구조

### APPS

- main
- accounts
- 

# 3. 요구사항 명세와 기능 명세

## 3.1 프로젝트 시각화 다이어그램
![image](https://github.com/abcdqwer1/project_chatbot/assets/68181016/8bf9c8cc-b6cf-4537-a265-6529095b5a81)
[다이어그램](https://www.mindmeister.com/app/map/3048013454)

## 3.2 API 기능 명세
![image](https://github.com/abcdqwer1/project_chatbot/assets/68181016/31043df8-e23b-4016-a4db-6f4e93a9796a)



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

# 5. 와이어프레임 / UI / BM

# 6. 데이터베이스 모델링 ERD
![image](https://github.com/abcdqwer1/project_chatbot/assets/68181016/e5b7caa7-2fcf-461e-ad37-802a859f0b0c)

[project_supbot ERD](https://dbdiagram.io/d/6568a3ba3be1495787104795)

# 7. 아키텍쳐

# 8. 메인기능

# 9. 트러블슈팅

# 10. 개발하며 느낀점
