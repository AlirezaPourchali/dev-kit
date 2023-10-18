# pip install psycopg2 sqlalchemy 
# NOTE: DO NOT USE python:alpine IMAGE , it doesnt have the required packages for psycopg2
# use python:3.10 for example
from sqlalchemy import create_engine , text

# create engine
engine = create_engine("postgresql+psycopg2://<user(postgres)>:<password>@<hostname/ip>:5432/<existing_db_name(postgres)>")

# connect to database with the engine
# IMP: enable autocommit
db = engine.connect().execution_options(isolation_level="AUTOCOMMIT")

# list all databases
db.execute(text("SELECT datname FROM pg_database WHERE datistemplate = false")).fetchall() 
database_names = [row[0] for row in re]

# check if db exists
name = "ali"
db.execute(text(f"SELECT datname FROM pg_database WHERE datname = '{name}' ")).fetchone()

# create database
db.execute(text("create database database"))

# list tables
db.execute(text(f"SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")).fetchall()

# check if table exists
from sqlalchemy import inspect                                                                
                                                                                              
inspect(engine).has_table("<table_name>") #==> true or false                                  
   
# create table with autoincrement column and primary key
db.execute(text(f"create table test (id serial primary key , name varchar(255))"))

## insert data into table 
query = text(f"insert into test (name) values (:name)")

param = {"name": "alireza"}

db.execute(query,param)

# create uuid                                                                                                                                                                                 
uuid = db.execute(text("select uuid()")).fetchall()                                                                                                                                           
print(uuid[0][0]) 

## select from table where name = alireza
name = "alireza"
db.execute(text(f"select * from test where name = \'{name}\'")).fetchall() #==> 2d array


## CLOSE THE CONNECTION AFTER YOU ARE DONE 

db.close()


