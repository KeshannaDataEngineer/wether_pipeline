import mysql.connector

def create_connection():
    return mysql.connector.connect(
        host="your-database-host",
        user="your-username",
        password="your-password",
        database="your-database-name"
)