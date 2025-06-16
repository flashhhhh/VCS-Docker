from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get database connection string from environment variables
# Default to a local development database if not set
SQLALCHEMY_DATABASE_URL = f"postgresql://{os.getenv('PG_USER', 'postgres')}:{os.getenv('PG_PASSWORD', '12345678')}@{os.getenv('PG_HOST', 'localhost')}:{os.getenv('PG_PORT', '5432')}/{os.getenv('PG_DB', 'post_db')}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

# Function to create tables
def create_tables():
	Base.metadata.create_all(bind=engine)