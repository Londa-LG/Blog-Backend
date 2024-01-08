from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Post_Model(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True,nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
    category: Mapped[str] = mapped_column(nullable=False)
    created_updated: Mapped[str] = mapped_column(nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)

class Comment_Model(Base):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(primary_key=True,nullable=False)
    post_id: Mapped[int] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    date_created: Mapped[str] = mapped_column(nullable=False)

class User_Model(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True,nullable=False)
    admin: Mapped[bool] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
