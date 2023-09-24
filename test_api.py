from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL connection details
mysql_config = {
    'host': 'test-poc-database.cdt6pnyv13my.ca-central-1.rds.amazonaws.com',
    'user': 'admin',
    'password': 'admin123',
    'database': 'testing_poc_data'
}

@app.route('/hello', methods=['GET'])
def hello_world():
	return "Hello world!"

@app.route('/create_table', methods=['GET'])
def create_table():
    try:
        conn = mysql.connector.connect(**mysql_config)
        cursor = conn.cursor()
        cursor.execute('USE testing_poc_data')
        cursor.execute('CREATE TABLE IF NOT EXISTS testing_poc_table (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))')
        conn.close()
        return 'Table created successfully'
    except mysql.connector.Error as err:
        return f'Error: {err}'

@app.route('/add_data', methods=['POST'])
def add_data():
    try:
        conn = mysql.connector.connect(**mysql_config)
        cursor = conn.cursor()
        cursor.execute('USE testing_poc_data')
        data = request.get_json()
        name = data['name']
        cursor.execute('INSERT INTO testing_poc_table (name) VALUES (%s)', (name,))
        conn.commit()
        conn.close()
        return 'Data added successfully'
    except mysql.connector.Error as err:
        return f'Error: {err}'

@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        conn = mysql.connector.connect(**mysql_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute('USE testing_poc_data')
        cursor.execute('SELECT * FROM testing_poc_table')
        data = cursor.fetchall()
        conn.close()
        return jsonify(data)
    except mysql.connector.Error as err:
        return f'Error: {err}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)

