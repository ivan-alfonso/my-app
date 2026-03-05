import enum
from typing import List, Optional
from sqlalchemy import (
    create_engine, Column, ForeignKey, Table, Text, Boolean, String, Date, 
    Time, DateTime, Float, Integer, Enum
)
from sqlalchemy.orm import (
    column_property, DeclarativeBase, Mapped, mapped_column, relationship
)
from datetime import datetime as dt_datetime, time as dt_time, date as dt_date

class Base(DeclarativeBase):
    pass

# Definitions of Enumerations
class Genre(enum.Enum):
    Adventure = "Adventure"
    Romance = "Romance"
    Philosophy = "Philosophy"
    Technology = "Technology"
    Thriller = "Thriller"
    Poetry = "Poetry"
    Fantasy = "Fantasy"
    History = "History"
    Cookbooks = "Cookbooks"
    Horror = "Horror"


# Tables definition for many-to-many relationships
books = Table(
    "books",
    Base.metadata,
    Column("library", ForeignKey("library.id"), primary_key=True),
    Column("books", ForeignKey("book.id"), primary_key=True),
)
books_1 = Table(
    "books_1",
    Base.metadata,
    Column("authors", ForeignKey("author.id"), primary_key=True),
    Column("books", ForeignKey("book.id"), primary_key=True),
)

# Tables definition
class Author(Base):
    __tablename__ = "author"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    birth: Mapped[dt_date] = mapped_column(Date)

class Library(Base):
    __tablename__ = "library"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    web_page: Mapped[str] = mapped_column(String(100))
    address: Mapped[str] = mapped_column(String(100))
    telephone: Mapped[str] = mapped_column(String(100))

class Book(Base):
    __tablename__ = "book"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    pages: Mapped[int] = mapped_column(Integer)
    stock: Mapped[int] = mapped_column(Integer)
    price: Mapped[float] = mapped_column(Float)
    release: Mapped[dt_date] = mapped_column(Date)
    genre: Mapped[Genre] = mapped_column(Enum(Genre))


#--- Relationships of the author table
Author.books: Mapped[List["Book"]] = relationship("Book", secondary=books_1, back_populates="authors")

#--- Relationships of the library table
Library.books: Mapped[List["Book"]] = relationship("Book", secondary=books, back_populates="library")

#--- Relationships of the book table
Book.library: Mapped[List["Library"]] = relationship("Library", secondary=books, back_populates="books")
Book.authors: Mapped[List["Author"]] = relationship("Author", secondary=books_1, back_populates="books")

# Database connection
DATABASE_URL = "sqlite:///Class_Diagram.db"  # SQLite connection
engine = create_engine(DATABASE_URL, echo=True)

# Create tables in the database
Base.metadata.create_all(engine, checkfirst=True)