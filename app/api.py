from typing import List

from fastapi import FastAPI, status, HTTPException
from starlette.responses import RedirectResponse

import app.models as models
import app.database as db

app = FastAPI(
    title="FCA code assessment",
    version="1.0"
)


@app.get("/", include_in_schema=False)
def index():
    return RedirectResponse(f"/docs")


@app.get("/query/search", response_model=List[models.SearchByAuthorAndTitle], status_code=status.HTTP_200_OK)
async def search_by_author_title(author: str = None, title: str = None):
    return db.search_by_author_title(author, title)


@app.get("/query/rent_report", response_model=List[models.RentedBooks], status_code=status.HTTP_200_OK)
async def search_by_author_title():
    return db.query_rented_books()


@app.post("/wishlist/", response_model=models.WishList)
async def add_wishlist(item: models.WishList, status_code=status.HTTP_201_CREATED):
    try:
        return db.add_to_wishlist(item)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Unable to insert.")


@app.delete("/wishlist/", response_model=models.WishList)
async def remove_wishlist(item: models.WishList, status_code=status.HTTP_202_ACCEPTED):
    try:
        if db.remove_from_wishlist(item):
            return item
        else:
            raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unable to delete.")


@app.post("/borrowings/", response_model=models.Borrowings)
async def add_borrow(item: models.Borrowings, status_code=status.HTTP_201_CREATED):
    try:
        if db.add_borrowing(item):
            return item
        else:
            raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Unable to insert.")


@app.patch("/borrowings/", response_model=models.Borrowings)
async def return_borrow(item: models.Borrowings, status_code=status.HTTP_201_CREATED):
    try:
        if db.return_borrowing(item):
            return item
        else:
            raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unable to delete.")
