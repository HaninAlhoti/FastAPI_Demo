# Basic imports needed for our application
from fastapi import FastAPI, Depends, HTTPException, status
from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime
# Import libraries for SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Initialize FastAPI app
app = FastAPI()

# Basic Task model
class Task(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    priority: int = 1

# Database configuration
DATABASE_URL = "postgresql://postgres:postgres@localhost/taskdb"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define SQLAlchemy model
class TaskDB(Base):
    """Database model for tasks"""
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String, nullable=True)
    due_date = Column(DateTime, nullable=True)
    priority = Column(Integer, default=1)

# Create tables
Base.metadata.create_all(bind=engine)

# Database dependency
def get_db():
    """Dependency for database sessions"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 3. Basic CRUD Operations with SQLAlchemy
