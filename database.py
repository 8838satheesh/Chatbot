import sqlite3

def create_connection():
    return sqlite3.connect("users.db", check_same_thread=False)

def init_db():
    conn = create_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    role TEXT DEFAULT 'user')''')
    c.execute('''CREATE TABLE IF NOT EXISTS chat_history (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    question TEXT,
                    answer TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY(user_id) REFERENCES users(id))''')
    conn.commit()
    conn.close()

def insert_user(username, password, role='user'):
    conn = create_connection()
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
    conn.commit()
    conn.close()

def get_user(username, password):
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    conn.close()
    return user

def save_chat(user_id, question, answer):
    conn = create_connection()
    c = conn.cursor()
    c.execute("INSERT INTO chat_history (user_id, question, answer) VALUES (?, ?, ?)", (user_id, question, answer))
    conn.commit()
    conn.close()

def get_user_history(user_id):
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT question, answer, timestamp FROM chat_history WHERE user_id=?", (user_id,))
    history = c.fetchall()
    conn.close()
    return history
