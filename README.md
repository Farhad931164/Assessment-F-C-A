# Code assessment

This application written based on using FastAPI, SQLite3, Pydantic models and SQLAlchemy.

# Install and Run

You need Python 3.8 available. I am using pipenv for the VM.
To run this application, install pipenv first and then type `pipenv install` in the root directory of this project. 
This will set up your environment. When your environment is ready, type `pipenv shell`. 
Now your command prompt is inside your VM. To run your application, type `Python main.py`

All APIs are now easily accessible by opening http://127.0.0.1:8080

1) GET method: /query/search to search database by author/book title 
2) GET method: /query/rent_report to get the book title, author and the number of days that the book was rented 
3) POST method: /wishlist/ to add a wishlist to the DB 
4) DELETE method: /wishlist/ to remove a wishlist from DB POST method: /borrowings/ to add a new borrowing
5) PATCH method: /borrowings/ to record a book return

There are two views in the sqlite database alongside the following tables: `AmazonIDs` `Authors` `Books` `Customers` `CustomersBorrowings` `CustomerWishlist` `Languges` `Librarian`

All the database communication is through SQLAlchemy ORM and all API data communication has a pydantic model.

Thank you
