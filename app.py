import requests
import logging
import time

from models import (SessionLocal,
                    User,
                    Post,
                    Comment,
                    Album,
                    Photo,
                    Todo)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def fetch_data(url):
    logging.info(f"Fetching data from {url}")
    response = requests.get(url)
    return response.json()


def save_users(data, session):
    users = [
        User(
            id=item['id'],
            name=item['name'],
            username=item['username'],
            email=item['email'],
            address=item['address'],
            phone=item['phone'],
            website=item['website'],
            company=item['company']
        ) for item in data
    ]
    session.bulk_save_objects(users)
    session.commit()


def save_posts(data, session):
    posts = [Post(**item) for item in data]
    session.bulk_save_objects(posts)
    session.commit()


def save_comments(data, session):
    comments = [Comment(**item) for item in data]
    session.bulk_save_objects(comments)
    session.commit()


def save_albums(data, session):
    albums = [Album(**item) for item in data]
    session.bulk_save_objects(albums)
    session.commit()


def save_photos(data, session):
    photos = [Photo(**item) for item in data]
    session.bulk_save_objects(photos)
    session.commit()


def save_todos(data, session):
    todos = [Todo(**item) for item in data]
    session.bulk_save_objects(todos)
    session.commit()


def main():
    logging.info("Starting data processing")

    # Задержка для обеспечения времени на запуск базы данных
    time.sleep(10)

    session = SessionLocal()

    try:
        # Загрузка и сохранение Пользователей
        users_data = fetch_data("https://jsonplaceholder.typicode.com/users")
        save_users(users_data, session)

        # Загрузка и сохранение Постов
        posts_data = fetch_data("https://jsonplaceholder.typicode.com/posts")
        save_posts(posts_data, session)

        # Загрузка и сохранение Комментариев
        comments_data = fetch_data("https://jsonplaceholder.typicode.com/comments")
        save_comments(comments_data, session)

        # Загрузка и сохранение Альбомов
        albums_data = fetch_data("https://jsonplaceholder.typicode.com/albums")
        save_albums(albums_data, session)

        # Загрузка и сохранение Фотографий
        photos_data = fetch_data("https://jsonplaceholder.typicode.com/photos")
        save_photos(photos_data, session)

        # Загрузка и сохранение Задач
        todos_data = fetch_data("https://jsonplaceholder.typicode.com/todos")
        save_todos(todos_data, session)

        logging.info("Data processing completed")
    except Exception as e:
        logging.error(f"Error processing data: {e}")
        session.rollback()
    finally:
        session.close()


if __name__ == "__main__":
    main()
