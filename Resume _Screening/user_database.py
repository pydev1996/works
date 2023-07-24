
# create database user;
#create table user(username varchar(250),password varchar(250),repassword varchar(250));
import mysql.connector
from mysql.connector import Error
import string
import random
def db_connection():
            try:
                connection = mysql.connector.connect(host='localhost',
                                                     database='user',
                                                     user='root',
                                                     password='Aleesha#143')
                if connection.is_connected():
                    db_Info = connection.get_server_info()
                    print("Connected to MySQL Server version ", db_Info)
                    cur = connection.cursor()
                    return connection,cur
            except Error as e:
                print(e)
#db_connection()
def register_user(username ,password,repassword):
    
    connection,cur=db_connection()
    query=("insert into user(username,password,repassword) values(%s,%s,%s)" )
    cur.execute(query,(username ,password,repassword))
    connection.commit()
def user_data():
    connection,cur=db_connection()
    query="select username,password from user"
    cur.execute(query)
    data=cur.fetchall()
    
    return data
#user_data()