"""Shared API dependencies."""
from fastapi import Depends
from sqlalchemy.orm import Session
from ..db.database import get_db

def get_database_session():
    """Dependency for database session."""
    return Depends(get_db)

