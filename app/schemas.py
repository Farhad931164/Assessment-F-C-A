# coding: utf-8
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, Numeric, Table, text, String
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Author(Base):
    __tablename__ = 'Authors'

    ID = Column(Integer, primary_key=True)
    AuthorFullName = Column(Numeric, nullable=False)


t_AvailabilityView = Table(
    'AvailabilityView', metadata,
    Column('AuthorFullName', String),
    Column('Language', String),
    Column('ISBN', String),
    Column('Title', String),
    Column('TotalAvailability', Integer),
    Column('AvailableToBorrow', NullType)
)


class Customer(Base):
    __tablename__ = 'Customers'

    ID = Column(Integer, primary_key=True)
    FullName = Column(Numeric, nullable=False)
    Email = Column(Numeric, nullable=False)


class Language(Base):
    __tablename__ = 'Languages'

    ID = Column(Integer, primary_key=True, unique=True)
    Language = Column(Numeric, nullable=False)


class Librarian(Base):
    __tablename__ = 'Librarian'

    ID = Column(Integer, primary_key=True)
    FullName = Column(Numeric, nullable=False)


t_sqlite_sequence = Table(
    'sqlite_sequence', metadata,
    Column('name', NullType),
    Column('seq', NullType)
)


class Book(Base):
    __tablename__ = 'Books'

    ID = Column(Integer, primary_key=True, unique=True)
    ISBN = Column(Numeric, nullable=False)
    Title = Column(Numeric, nullable=False)
    PublicationYear = Column(Integer, nullable=False)
    Availability = Column(Integer, nullable=False, server_default=text("0"))
    AutherID = Column(ForeignKey('Authors.ID'))
    LanguageID = Column(ForeignKey('Languages.ID'))

    Author = relationship('Author')
    Language = relationship('Language')
    Customers = relationship('Customer', secondary='CustomersWishlist')


class AmazonID(Base):
    __tablename__ = 'AmazonIDs'

    ID = Column(Integer, primary_key=True)
    BookID = Column(ForeignKey('Books.ID'), nullable=False)
    AmazonID = Column(Numeric, nullable=False)

    Book = relationship('Book')


t_CustomersBorrowings = Table(
    'CustomersBorrowings', metadata,
    Column('CustomerID', ForeignKey('Customers.ID'), nullable=False),
    Column('BookID', ForeignKey('Books.ID'), nullable=False),
    Column('BorrowDate', Date, nullable=False),
    Column('ReturnDate', Date, nullable=False),
    Column('ActualReturnDate', Date),
    Column('Returned', Boolean, nullable=False, server_default=text("false"))
)

t_CustomersWishlist = Table(
    'CustomersWishlist', metadata,
    Column('CustomerID', ForeignKey('Customers.ID'), primary_key=True),
    Column('BookID', ForeignKey('Books.ID'), primary_key=True)
)

t_BookRentReport = Table(
    'BookRentReport', metadata,
    Column('Title', String),
    Column('AuthorFullName', String),
    Column('TotalDaysOut', NullType)
)

