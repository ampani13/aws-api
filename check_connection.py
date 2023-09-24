import mysql.connector

def test_mysql_aws_rds_connection():
    try:
        # Replace with your AWS RDS MySQL connection details
        connection = mysql.connector.connect(
            host='test-poc-database.cdt6pnyv13my.ca-central-1.rds.amazonaws.com',
            user='admin',
            password='admin123',
            database='testing_poc_data'
        )

        if connection.is_connected():
            print('Connected to MySQL AWS RDS')
            connection.close()
        else:
            print('Unable to connect to MySQL AWS RDS')

    except mysql.connector.Error as err:
        print(f'Error: {err}')

if __name__ == "__main__":
    test_mysql_aws_rds_connection()
