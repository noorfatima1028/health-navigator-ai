from app.database.session import SessionLocal

db = SessionLocal()

print("Database connection successful!")

db.close()