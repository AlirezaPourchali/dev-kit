# pip install mysql-connector-python sqlalchemy 
# use python:3.10 image

from sqlalchemy import create_engine , text

# create an engine for write and create another for read queries

write_engine = create_engine("mysql+mysqlconnector://<user(root)>:<password>@<hostname/ip>:3306/<existing_db_name(my_database)>")

read_engine = create_engine("mysql+mysqlconnector://<user(root)>:<password>@<hostname/ip>:3306/<existing_db_name(my_database)>")
# connect to database with the engine
# NOTE: YOU NEED TO RENEW YOUR READ CONNECTION AFTER EVERY WRITE , OTHERWISE YOU WONT GET THE NEW DATA'S
mysqldb_write = write_engine.connect()
mysqldb_read = read_engine.connect() 

# now you can execute every sql command in this way

mysqldb_read.execute(text("<SQL_COMMAND>"))

# if you want to get the output of the command (select or show command) 

list = mysqldb_read.execute(text("show tables")).fetchall() #==> you will get a 2d list 

for i in range(len(a)):
    print(a[i][0])
 

# check if tables exist 

from sqlalchemy import inspect

inspect(read_engine).has_table("<table_name>") #==> true or false


# create uuid
mysqldb_read.execute(text("select uuid()")).fetchall()


## create table with primary key

table = "test"
mysqldb_write.execute(text(f"create table {table} (id varchar(40) primary key , username varchar(255) , email varchar(255) , avatar varchar(255) )"))

# autoincrement column and primary key and not null
mysqldb_write.execute(text("create table test6 (id int not null AUTO_INCREMENT primary key , name varchar(255))"))


## insert data into table 

query = text(f"insert into {table} (id , username , email , avatar) values (:id, :username , :email , :avatar)")

param = {"id": "id" , "username": "username", "email": "email", "avatar": "avatar"}

mysqldb_write.execute(query,param)
mysqldb_write.commit() #==> if you dont commit the data will not be inserted and after you close connection the data will be lost


## select from table where email = email
test = "email"
mysqldb_read.execute(text(f"select * from test where email = \"{test}\"")).fetchall() #==> 2d array


## CLOSE THE CONNECTION AFTER YOU ARE DONE 

mysqldb_read.close()
mysqldb_write.close()


