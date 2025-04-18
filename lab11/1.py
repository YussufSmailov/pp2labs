import psycopg2
import psycopg2
import csv
conn = psycopg2.connect(
    database="phone_book",
    host="localhost",
    user="postgres",
    password="12345",
    port="5432"
)




def create_phone_book():
    command="CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR(50), surname VARCHAR(50), phone_number VARCHAR(50))"
    with conn.cursor() as cur:
        cur.execute(command)
        conn.commit()



def insert_console(name, surname, phone_number):
    command="INSERT INTO  users(name, surname, phone_number)  VALUES (%s, %s, %s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (name, surname, phone_number)) 
            conn.commit()
            
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def insert_from_csv(filename):
    command = f"""INSERT INTO users(name, surname, phone_number) VALUES(%s, %s, %s)"""
    try:
        with conn.cursor() as cur:
            with open(filename, "r") as csvfile:
                csvreader = csv.reader(csvfile, delimiter=',')
                _ = next(csvreader) 
                for row in csvreader:
                    
                    name, surname, telephone = row
                    
                    cur.execute(command, (name, surname, telephone))
                    conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)



def change_name(old, new):
    command=f"UPDATE users SET name=%s WHERE name=%s"
    print("we")
    try:
        with conn.cursor() as cur:
            cur.execute(command, (new, old))
            conn.commit()
            print(f"Name '{old}' successfully changed to '{new}'")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def change_number(old, new):
    command=f"UPDATE users SET phone_number=%s WHERE phone_number=%s"
    print("we")
    try:
        with conn.cursor() as cur:
            cur.execute(command, (new, old))
            conn.commit()
            print(f"Number '{old}' successfully changed to '{new}'")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
def show():
    cur = conn.cursor()
    cur.execute("SELECT * FROM users" )
    rows = cur.fetchall()
    for row in rows:
        print(row)
def query_by_name(name):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users WHERE name = %s", (name,))
        rows = cur.fetchall()
        for row in rows:
            print(row)
def query_by_surname(surname):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users WHERE surname = %s", (surname,))
        rows = cur.fetchall()
        for row in rows:
            print(row)
def query_by_name_legnth():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users WHERE LENGTH(name)>5")
        rows = cur.fetchall()
        for row in rows:
            print(row)
def delete_by_name_(name):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM users WHERE name=%s", (name,))
def delete():
    with conn.cursor() as cur:
        cur.execute("DELETE FROM users")






while True:
    print("Welcome to my PhoneBook! This is the menu I created:")
    print("Choose 0, if you want to create a phone book")
    print("Choose 1, if you want add contact through Console")
    print("Choose 2, if you want add contact through csv file")
    print("Choose 3, if you want to update contacts name or phone")
    print("Choose 4, if you want to make query by name")
    print("Choose 5, if you want to make query by surname")
    print("Choose 6, if you want to make query by name length")
    print("Choose 7, if you want to delete a phone number by name")
    print("Choose 8, if you want to show all")
   
    a=int(input())
    if a==0:
        create_phone_book()
    if a==1:
        name=input(" input Name")
        surname=input("input the surname")
        phone_number=input("input the phone number")
        insert_console(name, surname, phone_number)
    if a==2:
        insert_from_csv("contacts.csv")
    if a==3:
        b=int(input("What do you wanna change \npress 1 for name \npress 2 for phone number\n"))
        if b==1:
            old=input("What name you want to change?")
            new=input("What is new name?")
            change_name(old, new)
        if b==2:
            old=input("What number you want to change?")
            new=input("What is new number?")
            change_number(old, new)
    if a==4:
        name=input("what name")
        query_by_name(name)
    if a==5:
        surname=input("what surnme")
        query_by_surname(surname)
    if a==6:
        query_by_name_legnth()
    if a==7:
        name=input("what name you want to delete?")
        delete_by_name_(name)
    if a==8:
        show()
    if a==9:
        delete()