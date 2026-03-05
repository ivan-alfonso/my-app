from datetime import datetime, date, time
from typing import Any, List, Optional, Union, Set
from enum import Enum
from pydantic import BaseModel, field_validator


############################################
# Enumerations are defined here
############################################

class Genre(Enum):
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

############################################
# Classes are defined here
############################################
class AuthorCreate(BaseModel):
    birth: date
    name: str
    books: List[int]  # N:M Relationship


class LibraryCreate(BaseModel):
    telephone: str
    name: str
    web_page: str
    address: str
    books: List[int]  # N:M Relationship


class BookCreate(BaseModel):
    pages: int
    price: float
    title: str
    stock: int
    genre: Genre
    release: date
    library: List[int]  # N:M Relationship
    authors: List[int]  # N:M Relationship

    @field_validator('pages')
    @classmethod
    def validate_pages_1(cls, v):
        """OCL Constraint: constraint_Book_0_1"""
        if not (v > 10):
            raise ValueError('pages must be > 10')
        return v

