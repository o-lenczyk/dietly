#from google.cloud.sql.connector import Connector, IPTypes
import ssl
import os
from sqlalchemy import create_engine, MetaData, Column, Table, ForeignKey, Integer, Sequence, String, Date, Float, BIGINT, select, engine

db_user=os.environ['db_user']
db_pass=os.environ['db_pass']
db_host=os.environ['db_host']
db_port=os.environ['db_port']
db_name=os.environ['db_name']

connect_args = {}

db_root_cert = "keys/server-ca.pem"  # e.g. 'keys/server-ca.pem'
db_cert = "keys/client-cert.pem"  # e.g. 'keys/client-cert.pem'
db_key = "keys/client-key.pem"  # e.g. 'keys/client-key.pem'

ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_REQUIRED
ssl_context.load_verify_locations(db_root_cert)
ssl_context.load_cert_chain(db_cert, db_key)
connect_args["ssl_context"] = ssl_context

pool = create_engine(
    engine.url.URL.create(
        drivername="postgresql+pg8000",
        username=db_user,
        password=db_pass,
        host=db_host,
        port=db_port,
        database=db_name,
    ),
    connect_args=connect_args,
)

meta = MetaData()

meals = Table('meals', meta,
    Column('ID', Integer, primary_key=True, autoincrement=True),
    Column('date', String(20)),
    Column('mealName', String(60)),
    Column('menuMealName', String(600)),
    Column('weight', Float),
    Column('calories', Float),
    Column('fat', Float),
    Column('protein', Float),
    Column('carbohydrate', Float),
    Column('dietaryFiber', Float),
    Column('sugar', Float),
    Column('salt', Float),
    Column('saturatedFattyAcids', Float),
    Column('ingredients', String(6000)),
    Column('rate', Integer)

)
# create table
#meals.create(pool)

def insert(
        date,
        mealName, 
        menuMealName, 
        weight, 
        calories, 
        fat, 
        protein, 
        carbohydrate, 
        dietaryFiber, 
        sugar, 
        salt, 
        saturatedFattyAcids,
        ingredients
    ):

    ins = meals.insert().values(
        date=date,
        mealName=mealName, 
        menuMealName=menuMealName, 
        weight = weight, 
        calories=calories, 
        fat=fat, 
        protein=protein, 
        carbohydrate=carbohydrate, 
        dietaryFiber=dietaryFiber, 
        sugar=sugar, 
        salt=salt, 
        saturatedFattyAcids=saturatedFattyAcids,
        ingredients=ingredients
    )

    with pool.connect() as db_conn:

        db_conn.execute(ins)
        db_conn.commit()

        # for row in result:
        #     print(row)

# close Cloud SQL Connector
#connector.close()
def isEntry(date, mealName):
    with pool.connect() as db_conn:
        stmt = select(meals).where(meals.c.date==date).where(meals.c.mealName==mealName)

        result = db_conn.execute(stmt)
        if result.rowcount==0:
            return False
        else:
            return True

#print(isEntry("2024-01-11","Śniadanie"))