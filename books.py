from fastapi import FastAPI,Body # type: ignore
from books_data import BOOKS

app = FastAPI()

@app.get("/books/")
async def get_all_books():
     return BOOKS   
 
#  search by author using qurey parammeters

@app.get("/books/{book_author}")
def search_author(book_author: str = None, limit: int = 3):
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold():
            return{"Search Results ": book , " Limit" : limit}
 
@app.get("/books/{book_title}")
def get_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book




