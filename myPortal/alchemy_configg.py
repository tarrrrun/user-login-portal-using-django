from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db_url='mysql+pymysql://root:nimbus2000@localhost:3306/myPortal'
engine=create_engine(db_url)
Session=sessionmaker(bind=engine)
session=Session()
