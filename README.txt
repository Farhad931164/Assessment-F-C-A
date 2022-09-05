FCA code assessment
This application written based on using FastAPI, SQLite3, Pydantic models and SQLAlchmey ORM.

You need python 3.8 available to run this application.
For VM, I am using pipenv.
To run this application, install pipenv first and then type pipenv install in the root directory of this project.
This will set up your environment. When your environment is ready, type 'pipenv shell'.
Now your command prompt is inside your VM. 
To run your application, type 'Python main.py'

All APIs are now easily accessible by opening http://127.0.0.1:8080

GET method: /query/search to search database by author/book title
GET method: /query/rent_report to get the book title, author and the number of days that the book was rented
POST method: /wishlist/ to add a wishlist to the DB
DELETE method: /wishlist/ to remove a wishlist from DB
POST method: /borrowings/ to add a new borrowing
PATCH method: /borrowings/ to record a book return

There are two views in the sqlite database alongside the following tables:
AmazonIDs
Authors
Books
Customers
CustomersBorrowings
CustomerWishlist
Languges
Librarian

also, you can use SQLlite Studio to browse the DB.

Thank you
Farhad


