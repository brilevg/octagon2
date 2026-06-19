from db.db import engine
from db.db import SessionLocal

from db.models import Base

from db.crud import create_category
from db.crud import create_book


Base.metadata.create_all(engine)

session = SessionLocal()

programming = create_category(session, "Programming")

database = create_category(session, "Databases")

create_book(
    session,
    "Python Crash Course",
    "Python for beginners",
    35.5,
    "",
    programming,
)

create_book(
    session,
    "Fluent Python",
    "Advanced Python",
    60,
    "",
    programming,
)

create_book(
    session,
    "PostgreSQL Guide",
    "SQL database",
    42,
    "",
    database,
)

create_book(
    session,
    "Mastering SQL",
    "Complete SQL",
    39,
    "",
    database,
)

session.close()

print("Database initialized")