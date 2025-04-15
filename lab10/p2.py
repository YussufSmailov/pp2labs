import psycopg2

current_user = ""


conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    host='localhost',
    password="12345",
    port=5432
)


query_create_table_users = """
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        username VARCHAR(255) UNIQUE
    )
"""

query_create_table_user_scores = """
    CREATE TABLE IF NOT EXISTS user_scores(
        id SERIAL PRIMARY KEY,
        username VARCHAR(255),
        score INTEGER,
        level INTEGER
    )
"""

def execute_query(query):
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
    except Exception as error:
        print("DB Error:", error)

def input_user():
    global current_user
    current_user = input("Enter your username: ").strip()
    if not check_existence(current_user):
        add_user(current_user)
        print(f"New user '{current_user}' created.")
    else:
        print(f"Welcome back, {current_user}!")

def add_user(name):
    command = "INSERT INTO users(username) VALUES(%s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (name,))
            conn.commit()
    except Exception as error:
        print(error)

def check_existence(name):
    command = "SELECT * FROM users WHERE username=%s"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (name,))
            result = cur.fetchall()
            return bool(result)
    except Exception as error:
        print(error)

def add_new_score(score):
    level = max(1, score // 4) 
    command = "INSERT INTO user_scores(username, score, level) VALUES(%s, %s, %s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (current_user, score, level))
            conn.commit()
    except Exception as error:
        print(error)

def process_score(score):
    if not check_existence(current_user):
        add_user(current_user)
    add_new_score(score)


#if __name__ == '__main__':
 #   execute_query(query_create_table_users)
  #  execute_query(query_create_table_user_scores)
