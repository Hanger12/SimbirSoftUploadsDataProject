1.	Установите Docker и Docker Compose.
2.  Скачайте Приложение с сайта github: https://github.com/Hanger12/SimbirSoftUploadsDataProject.git.
3.	Выполните команду docker-compose up --build -d для сборки и запуска контейнеров Docker
4.	Проверьте, что контейнеры запущены: docker ps
5.	Приложение автоматически скачает данные из REST API и сохранит их в базе данных PostgreSQL.
6.	Проверьте данные в базе данных с помощью DBeaver или другого инструмента.
