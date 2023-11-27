import psycopg2
import os
from dotenv import load_dotenv


# Connection with DB

load_dotenv()

try:
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        host=os.getenv('HOST'),
        port=os.getenv('PORT')
    )
    print('Successful connection')
except psycopg2.OperationalError as e:
    print(f"Unable to connect to the database: {e}")

# Create a cursor object
#os.getenv().cursor()
# Parsing files

# Sending commands