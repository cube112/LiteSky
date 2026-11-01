from sqlalchemy import Date, DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .exts import db


# ===========
# 文件ORM模型
# ===========
class Files(db.Model):
    __tablename__ = "files"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    origin_filename: Mapped[str] = mapped_column(String(255), nullable=False)
    store_filename: Mapped[str] = mapped_column(String(255), nullable=False)
    file_extension: Mapped[str] = mapped_column(String(10), nullable=False)
    file_size: Mapped[float] = mapped_column(Float(4, 2), nullable=False)
    upload_time: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    delete_time: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    download_code: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)

    user_id: Mapped[int] = mapped_column(
        Integer, db.ForeignKey("users.id"), nullable=False
    )
    user: Mapped["Users"] = relationship(back_populates="files")

    def __repr__(self) -> str:
        return f"<Files(id={self.id}, origin_filename={self.origin_filename}, store_filename={self.store_filename})>"


# ===========
# 用户ORM模型
# ===========
class Users(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    created_at: Mapped[Date] = mapped_column(Date, nullable=False)

    files: Mapped[list["Files"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"<Users(id={self.id}, username={self.username}, email={self.email})>"
