import datetime
from datetime import date
from typing import Optional

from pydantic import BaseModel


class SearchByAuthorAndTitle(BaseModel):
    AuthorFullName: str
    Language: str
    ISBN: str
    Title: str
    TotalAvailability: int
    AvailableToBorrow: int

    class Config:
        orm_mode = True


class RentedBooks(BaseModel):
    AuthorFullName: str
    Title: str
    TotalDaysOut: int

    class Config:
        orm_mode = True


class WishList(BaseModel):
    CustomerID: int
    BookID: int

    class Config:
        orm_mode = True


class Borrowings(BaseModel):
    CustomerID: int
    BookID: int
    BorrowDate: date = date.today()
    ReturnDate: date = date.today() + datetime.timedelta(days=7)
    ActualReturnDate: date
    Returned: bool = False

    class Config:
        orm_mode = True
