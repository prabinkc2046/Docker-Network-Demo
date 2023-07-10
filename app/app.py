from flask import Flask
import mysql.connector

app = Flask(__name__)

# MySQL configurations
db_config = {
    'host': 'mysql_host',
    'user': 'flask',
    'password': 'prabin123',
    'database': 'mydatabase'
}

# Create MySQL connection
conn = mysql.connector.connect(**db_config)


@app.route('/')
def index():
    # Check if the connection to MySQL is successful
    if conn.is_connected():
        return 'Successfully connected to the MySQL server!'
    else:
        return 'Failed to connect to the MySQL server.'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
