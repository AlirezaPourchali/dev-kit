# pip install mariadb sqlalchemy 
# NOTE: DO NOT USE python:alpine IMAGE , it doesnt have the required packages for mariadb
# use python:3.10 for example

from sqlalchemy import create_engine , text

# create engine

engine = create_engine("mariadb+mariadbconnector://<user(root)>:<password>@<hostname/ip>:3306/<existing_db_name>")

# connect to database with the engine

mariadb = engine.connect() 

# now you can execute every sql command in this way

mariadb.execute(text("<SQL_COMMAND>"))

# if you want to get the output of the command (select or show command) 

list = mariadb.execute(text("show tables")).fetchall() #==> you will get a 2d list 

for i in range(len(a)):
    print(a[i][0])
 

# check if tables exist 

from sqlalchemy import inspect

inspect(engine).has_table("<table_name>") #==> true or false


# create uuid
mariadb.execute(text("select uuid()")).fetchall()


## create table with primary key

table = "test"
mariadb.execute(text(f"create table {table} (id varchar(40) primary key , username varchar(255) , email varchar(255) , avatar varchar(255) )"))

# autoincrement column and primary key and not null
mariadb.execute(text("create table test6 (id int not null AUTO_INCREMENT primary key , name varchar(255))"))


## insert data into table 

query = text(f"insert into {table} (id , username , email , avatar) values (:id, :username , :email , :avatar)")

param = {"id": "id" , "username": "username", "email": "email", "avatar": "avatar"}

mariadb.execute(query,param)
mariadb.commit() #==> if you dont commit the data will not be inserted and after you close connection the data will be lost


## select from table where email = email
test = "email"
mariadb.execute(text(f"select * from reza where email = \"{test}\"")).fetchall() #==> 2d array


## CLOSE THE CONNECTION AFTER YOU ARE DONE 

mariadb.close()


