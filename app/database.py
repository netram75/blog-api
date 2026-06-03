from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# We need to fill this in!
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Netram%408619@localhost:5433/blog_api"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()