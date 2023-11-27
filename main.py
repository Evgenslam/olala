import datetime as datetime
import psycopg2
import os
from dotenv import load_dotenv
from datetime import datetime


# Connection with DB

load_dotenv()

# Data to be inserted
dataset = {
    'registered_at': datetime.now(),
    'updated_at': datetime.now(),
    'cam_url': 'https://moidom.citylink.pro/pub/89131',
    'timezone': 'UTC+3',
    'address': 'Р.Карелия, Суоярви, ул. Кайманова, д.2',
    'update_period': None,
    'consent': True,
    'parking_places': None,
    'last_connection': None,
}

columns = ', '.join(dataset)
values_to_insert = tuple(dataset.values())
#data_to_insert = ('value1', 'value2', 'value3')  # Replace with your data

# Your INSERT query
query = f"INSERT INTO camera ({columns}) VALUES ({', '.join(['%s'] * len(values_to_insert))})"

with psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        host=os.getenv('HOST'),
        port=os.getenv('PORT')) as conn:
    cur = conn.cursor()

    try:
        cur.execute(query, values_to_insert)
        conn.commit()

    except Exception as e:
        print(e)

    finally:
        cur.close()




# Parsing files

# Sending commands