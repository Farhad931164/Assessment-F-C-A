from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import app.schemas as schema
import app.models as models

engine = create_engine(
    "sqlite:///./database/LibraryDB", connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()
print("session")


def search_by_author_title(author: str = None, title: str = None):
    filters = []
    if author:
        filters.append(schema.t_AvailabilityView.c.AuthorFullName == author)
    if title:
        filters.append(schema.t_AvailabilityView.c.Title == title)

    return session.query(schema.t_AvailabilityView).filter(*filters).all()


def add_to_wishlist(item: models.WishList):
    insert_stmnt = schema.t_CustomersWishlist.insert(item.dict())
    session.execute(insert_stmnt)
    session.commit()
    return item


def remove_from_wishlist(item: models.WishList):
    delete_stmnt = schema.t_CustomersWishlist.delete().where(schema.t_CustomersWishlist.c.BookID == item.BookID,
                                                             schema.t_CustomersWishlist.c.CustomerID == item.CustomerID)
    result = session.execute(delete_stmnt)
    session.commit()
    return result.rowcount


def add_borrowing(item: models.Borrowings):
    item.ActualReturnDate = None
    item.Returned = False
    insert_stmnt = schema.t_CustomersBorrowings.insert(item.dict())
    result = session.execute(insert_stmnt)
    session.commit()
    return result.rowcount


def return_borrowing(item: models.Borrowings):
    item.Returned = True
    if item.ActualReturnDate is None:
        item.ActualReturnDate = date.today()
    insert_stmnt = schema.t_CustomersBorrowings.update().where(schema.t_CustomersBorrowings.c.BookID == item.BookID,
                                                               schema.t_CustomersBorrowings.c.CustomerID == item.CustomerID).values(
        item.dict())
    result = session.execute(insert_stmnt)
    session.commit()
    return result.rowcount


def query_rented_books():
    return session.query(schema.t_BookRentReport).all()
