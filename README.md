# prac-django

장고 첫 사용

1. 개발서버 만듬
2. 앱을 만들고 프로젝트 레벨에서 앱 레벨로 경로설정을 했음
   - django-admin startapp rolls
3. 앱 레벨 `urls.py` 에서 뷰로 진행
4. mysql 연동
   - pip install mysqlclient
   - pip install python-dotenv
   - `python manage.py migrate`
5. Model 생성 그리고 연동
   - python manage.py makemigrations polls
   - python manage.py migrate
