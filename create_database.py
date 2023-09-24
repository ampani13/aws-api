import mysql.connector
def create_database():
    endpoint = 'test-poc-database.cdt6pnyv13my.ca-central-1.rds.amazonaws.com'
    username = 'admin'
    password = 'admin123'
    try:
        connection = mysql.connector.connect(
            host=endpoint,
            user=username,
            password=password
        )
		if connection.is_connected():
            print('Connected to MySQL server')
			cursor = connection.cursor()
            db_name = 'testing_poc_data'
            cursor.execute(f'CREATE DATABASE {db_name}')
            print(f'Database {db_name} created successfully')
            cursor.close()
            connection.close()
        else:
            print('Unable to connect to MySQL server')

    except mysql.connector.Error as err:
        print(f'Error: {err}')

if __name__ == "__main__":
    create_database()
