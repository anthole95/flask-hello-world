from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://lab_10_database_yrpp_user:TG46YdBQCWePmjwREmkUdOsu0eQP9LEM@dpg-cl2j5kg310os73b81c9g-a.oregon-postgres.render.com/lab_10_database_yrpp")
    conn.close()
    return "Database Connection Successful"

