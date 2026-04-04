from sqlalchemy import Integer, String, DateTime, Float
from sqlalchemy.orm import Mapped, mapped_column

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