from backend.db.database import Base, engine
from backend.db.models import User

Base.metadata.create_all(bind=engine)
print("✅ Database initialized")
