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

@app.route('/db_create')
    conn = psycopg2.connect("postgres://lab_10_database_yrpp_user:TG46YdBQCWePmjwREmkUdOsu0eQP9LEM@dpg-cl2j5kg310os73b81c9g-a.oregon-postgres.render.com/lab_10_database_yrpp")
    curr = conn.cursor()
    curr.execute('''
    CREATE TABLE IF NOT EXISTS Basketball{
        First varchar(255)
        Last varchar(255)
        City varchar(255)
        Name varchar(255)
        Number int
        );
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"

@app.route('/db_insert')
    conn = psycopg2.connect("postgres://lab_10_database_yrpp_user:TG46YdBQCWePmjwREmkUdOsu0eQP9LEM@dpg-cl2j5kg310os73b81c9g-a.oregon-postgres.render.com/lab_10_database_yrpp")
    curr = conn.cursor()
    curr.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"

@app.route('/db_select')
    conn = psycopg2.connect("postgres://lab_10_database_yrpp_user:TG46YdBQCWePmjwREmkUdOsu0eQP9LEM@dpg-cl2j5kg310os73b81c9g-a.oregon-postgres.render.com/lab_10_database_yrpp")
    curr = conn.cursor()
    curr.execute('''
        SELECT * FROM Basketball;
    ''')
    records = curr.fetchall()
    conn.close()
    response_string=""
    response_string+="<table>"
    for player in records:
        resposne_string+="<tr>"
        for info in player:
            response_string+="<td>{}</td>".format(info)
        response_string+="</tr>"
    response_string+="</table>"
    return response_string

@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect("postgres://lab_10_database_yrpp_user:TG46YdBQCWePmjwREmkUdOsu0eQP9LEM@dpg-cl2j5kg310os73b81c9g-a.oregon-postgres.render.com/lab_10_database_yrpp")
    curr = conn.cursor()
    curr.execute('''
        DROP TABLE Basketball;
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"


        