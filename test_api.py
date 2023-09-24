from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL connection details
mysql_config = {
    'host': 'testing-db.crgow1kn1spf.us-east-1.rds.amazonaws.com',
    'user': 'admin',
    'password': 'admin123',
    'database': 'your_database_name'
}

@app.route('/create_table', methods=['GET'])
def create_table():
    try:
        conn = mysql.connector.connect(**mysql_config)
        cursor = conn.cursor()
        cursor.execute('USE your_database_name')
        cursor.execute('CREATE TABLE IF NOT EXISTS your_table_name (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))')
        conn.close()
        return 'Table created successfully'
    except mysql.connector.Error as err:
        return f'Error: {err}'

@app.route('/add_data', methods=['POST'])
def add_data():
    try:
        conn = mysql.connector.connect(**mysql_config)
        cursor = conn.cursor()
        cursor.execute('USE your_database_name')
        data = request.get_json()
        name = data['name']
        cursor.execute('INSERT INTO your_table_name (name) VALUES (%s)', (name,))
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
        cursor.execute('USE your_database_name')
        cursor.execute('SELECT * FROM your_table_name')
        data = cursor.fetchall()
        conn.close()
        return jsonify(data)
    except mysql.connector.Error as err:
        return f'Error: {err}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
