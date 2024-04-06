from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine


STORAGE_URL = "postgresql://plants:pass@localhost:5431/plants"


def get_session():
    engine = create_engine(STORAGE_URL)

    session = scoped_session(sessionmaker(bind=engine))

    try:
        yield session
    finally:
        session.close()
