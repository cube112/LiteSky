from typing import List

from sqlalchemy import Integer, String, DateTime, Float, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .exts import db

# 定义一张表，包含的字段有：id、origin_filename、save_filename、file_size、deadline
class Files(db.Model):
    __tablename__ = 'files'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    origin_filename: Mapped[str] = mapped_column(String(255), nullable=False)
    store_filename: Mapped[str] = mapped_column(String(255), nullable=False)
    save_path: Mapped[str] = mapped_column(String(255), nullable=False)
    file_size: Mapped[str] = mapped_column(String(255), nullable=False)
    upload_time: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    delete_time: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    download_code: Mapped[str] = mapped_column(String(255), nullable=True, unique=True)

    user_id: Mapped[int] = mapped_column(Integer, db.ForeignKey('users.id'), nullable=True, index=True)
    user: Mapped['User'] = relationship('User', back_populates='files')



class User(db.Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    created_at: Mapped[Date] = mapped_column(Date, nullable=False)
    
    files: Mapped[List['Files']] = relationship('Files', back_populates='user', cascade='all, delete-orphan')