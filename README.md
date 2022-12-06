# yamdb_final
![yamdb_workflow](https://github.com/seerez/yamdb_final/actions/workflows/yamdb_workflow.yaml/badge.svg)

## Описание
Сайт является - базой отзывов о фильмах, книгах и музыке.
Пользователи могут оставлять рецензии на произведения, а также комментировать эти рецензии.
Администрация добавляет новые произведения и категории (книга, фильм, музыка и т.д.)
Также присутствует файл docker-compose, позволяющий , быстро развернуть контейнер базы данных (PostgreSQL), контейнер проекта django + gunicorn и контейнер nginx

## Адрес сайта
http://51.250.85.31/redoc/

## Как запустить

## Необходимое ПО

Docker: https://www.docker.com/get-started <br />
Docker-compose: https://docs.docker.com/compose/install/

## Инструкция по запуску

Для запуска необходимо из корневой папки проекта ввести в консоль команду:
```
docker-compose up --build
```
Затем узнать id контейнера, для этого вводим
```
docker container ls
```
В ответ получаем примерно следующее
```
CONTAINER ID   IMAGE                     COMMAND                  CREATED         STATUS         PORTS                    NAMES
ab8cb8741e4a   nginx:1.19.0              "/docker-entrypoint.…"   7 minutes ago   Up 2 minutes   0.0.0.0:80->80/tcp       nginx_1
f78cc8f246fb   mamontovdn/yamdb:latest   "/bin/sh -c 'gunicor…"   7 minutes ago   Up 2 minutes   0.0.0.0:8000->8000/tcp   web_1
a68243a0a5e2   postgres:12.4             "docker-entrypoint.s…"   7 minutes ago   Up 2 minutes   5432/tcp                 db_1
```
Нас интересует контейнер web_1, заходим в него командой
```
docker exec -it <CONTAINER ID> sh
```
И делаем миграцию БД, и сбор статики
```
python manage.py migrate
python manage.py collectstatic
```
При желании можно загрузить тестовую бд с контентом
```
python manage.py loaddata fixtures.json
```