from myPortal.alchemy_configg import engine
from authentication.models import Base

# Create all tables in the database based on the models defined
Base.metadata.create_all(engine)

print("Tables created successfully.")
