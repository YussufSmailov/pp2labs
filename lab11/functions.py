import psycopg2
import psycopg2
conn = psycopg2.connect(
    database="phone_book",
    host="localhost",
    user="postgres",
    password="12345",
    port="5432"
)

create_func_select_by_pat_name="""
    CREATE OR REPLACE FUNCTION select_by_pat_name(letter VARCHAR(1))
    RETURNS TABLE (id INTEGER, name VARCHAR(50), surname VARCHAR(50), phone_number VARCHAR(50))
    AS
    $$
    BEGIN
    RETURN QUERY 
    SELECT * FROM users WHERE LEFT(users.name, 1) = letter;
    END;
    $$
    LANGUAGE plpgsql;
"""

create_func_select_by_pat_surname="""
    CREATE OR REPLACE FUNCTION select_by_pat_surname(letter VARCHAR(1))
    RETURNS TABLE (id INTEGER, name VARCHAR(50), surname VARCHAR(50), phone_number VARCHAR(50))
    AS
    $$
    BEGIN
    RETURN QUERY 
    SELECT * FROM users WHERE LEFT(users.surname, 1) = letter;
    END;
    $$
    LANGUAGE plpgsql;
"""
create_func_select_by_pat_phone_num="""
    CREATE OR REPLACE FUNCTION select_by_pat_phone_num(letter VARCHAR(3))
    RETURNS TABLE (id INTEGER, name VARCHAR(50), surname VARCHAR(50), phone_number VARCHAR(50))
    AS
    $$
    BEGIN
    RETURN QUERY 
    SELECT * FROM users WHERE LEFT(users.phone_number, 3) = letter;
    END;
    $$
    LANGUAGE plpgsql;
"""

create_func_select_by_offset="""
    CREATE OR REPLACE FUNCTION select_by_offset(beg INT, en INT)
    RETURNS TABLE (id INT, name VARCHAR(50), surname VARCHAR(50), phone_number VARCHAR(50))
    AS
    $$
    BEGIN
    RETURN QUERY
    SELECT * FROM users  LIMIT beg OFFSET en;
    END;
    $$
    LANGUAGE plpgsql
"""



create_proc_insert="""
    CREATE OR REPLACE PROCEDURE insert_new(name VARCHAR(50), surname VARCHAR(50), phone_number VARCHAR(50))
    AS
    $$
    BEGIN
    INSERT INTO users(name, surname, phone_number) VALUES(name, surname, phone_number);
    END;
    $$
    LANGUAGE plpgsql
"""

create_proc_upd="""
    CREATE OR REPLACE PROCEDURE upd(n VARCHAR(50), s VARCHAR(50), ph VARCHAR(50))
    AS
    $$
    BEGIN
    UPDATE users SET phone_number=ph WHERE name=n;
    END;
    $$
    LANGUAGE plpgsql
"""

create_proc_del="""
    CREATE OR REPLACE PROCEDURE del(n VARCHAR(50))
    AS
    $$
    BEGIN
    DELETE FROM users WHERE name=n;
    END;
    $$
    LANGUAGE plpgsql
"""



def check_exists(name):
    command="SELECT * FROM users WHERE name=%s"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (name, ))
            return bool(cur.fetchall())
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)




def call_f(func_name, letter):
    try:
        with conn.cursor() as cur:
            cur.callproc(func_name, letter)
            return cur.fetchall()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)




def call_ins(name, surname, phone_number):
    command="CALL insert_new(%s, %s, %s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (name,surname, phone_number))
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)




def call_upd(name, surname, phone_number):
    command="CALL upd(%s, %s, %s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (name,surname, phone_number))
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)




def off(func_name, beg, end):
    try:
        with conn.cursor() as cur:
            cur.callproc(func_name, (beg, end))
            return cur.fetchall()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)




def call_del(name):
    command="CALL del(%s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (name, ))
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)




def execute_query(query):
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)




#execute_query(create_func_select_by_pat_name)
#execute_query(create_func_select_by_pat_surname)
#execute_query(create_func_select_by_offset)
#execute_query(create_func_select_by_pat_phone_num)
#execute_query(create_proc_insert)
#execute_query(create_proc_upd)
#execute_query(create_proc_del)



print(call_f('select_by_pat_name', ('R',)))



print("="*10)
print(call_f('select_by_pat_surname', ('K',)))



print("="*10)
print(call_f('select_by_pat_phone_num', ('777',)))



print("="*10)
print(off("select_by_offset", 2, 4))



a=int(input("press 1 if you wanna insert or update user via procedure 2 to delete"))

if a==1:
    name=input("name: ")
    surname=input("surname: ")
    phone_num=input("phone_num: ")
    flag=check_exists(name)
    if not flag:
        call_ins(name, surname, phone_num)
    else:
        call_upd(name, surname, phone_num)
if a==2:
    name=input("name: ")
    call_del(name)


