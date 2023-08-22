import os
import psycopg2
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='../frontend/build')

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='todo',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn


@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/static/<path:path>')
def frontend_assets(path):
    return send_from_directory(app.static_folder, os.path.join('static', path))

@app.route('/api/todos')
def get_todos():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM todos')
    todos = cur.fetchall()
    cur.close()
    conn.close()
    return {'todos': todos}