from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

password="***"
user="***"
engine=create_engine(f"mysql+mysqlconnector://{user}:{password}@localhost/task2",echo = True)



SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()