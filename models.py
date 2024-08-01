from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os

DATABASE_URL = (f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
                f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}")

Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class User(Base):
    # Таблица Пользователей
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    username = Column(String, index=True)
    email = Column(String)
    address = Column(JSON)
    phone = Column(String)
    website = Column(String)
    company = Column(JSON)


class Post(Base):
    # Таблица Постов
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey('users.id'), index=True)
    title = Column(String)
    body = Column(String)
    user = relationship("User", back_populates="posts")


class Comment(Base):
    # Таблица Комментариев
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, index=True)
    postId = Column(Integer, ForeignKey('posts.id'), index=True)
    name = Column(String)
    email = Column(String)
    body = Column(String)
    post = relationship("Post", back_populates="comments")


class Album(Base):
    # Таблица Альбомов
    __tablename__ = 'albums'
    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey('users.id'), index=True)
    title = Column(String)
    user = relationship("User", back_populates="albums")


class Todo(Base):
    # Таблица Задач
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey('users.id'), index=True)
    title = Column(String)
    completed = Column(Boolean)
    user = relationship("User", back_populates="todos")


class Photo(Base):
    # Таблица Фотографий
    __tablename__ = 'photos'
    id = Column(Integer, primary_key=True, index=True)
    albumId = Column(Integer, ForeignKey('albums.id'), index=True)
    album = relationship("Album", back_populates="photos")
    title = Column(String)
    url = Column(String)
    thumbnailUrl = Column(String)


User.posts = relationship("Post", order_by=Post.id, back_populates="user")
User.albums = relationship("Album", order_by=Post.id, back_populates="user")
User.todos = relationship("Todo", order_by=Post.id, back_populates="user")
Post.comments = relationship("Comment", order_by=Comment.id, back_populates="post")
Album.photos = relationship("Photo", order_by=Post.id, back_populates="album")

Base.metadata.create_all(bind=engine)
