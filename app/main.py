from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db, Base, engine
from app.models import Book

# Создаём таблицы при старте
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Каталог личной библиотеки")

@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в каталог библиотеки!"}

@app.get("/books", response_model=List[dict])
def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()

@app.post("/books", response_model=dict)
def create_book(title: str, author: str, year: int, db: Session = Depends(get_db)):
    book = Book(title=title, author=author, year=year)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

@app.get("/health")
def health_check():
    return {"status": "healthy"}