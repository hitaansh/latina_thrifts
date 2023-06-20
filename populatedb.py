import psycopg2
from dotenv import load_dotenv
load_dotenv()
import os

conn, cur = None, None

try:
    conn = psycopg2.connect(
            host = os.getenv('hostname'),
            dbname = os.getenv('database'),
            user = os.getenv('username'),
            password = os.getenv('pass'),
            port = os.getenv('port_id')
    )

    cur = conn.cursor()

    create_script = ''' CREATE TABLE IF NOT EXISTS product (
                            id      varchar(150) PRIMARY KEY,
                            name    varchar(150) NOT NULL,
                            size    varchar(3) NOT NULL,
                            brand   varchar(100) NOT NULL,
                            condition varchar(100) NOT NULL,
                            style   varchar(100) NOT NULL,
                            color   varchar(100) NOT NULL,
                            description    varchar(1000) NOT NULL,
                            hashtags varchar(500) NOT NULL,
                            photos   TEXT [] NOT NULL
    );
    '''
    cur.execute(create_script)

    insert_script = 'INSERT INTO product (id, name, size, brand, condition, style, color, description, hashtags, photos) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    insert_value = ('test-blue-dress','vintange-blue-dress','L','Nike','Good','Dress','Blue','Its a lit dress', '#lit, #blue', ['cnn.com'])
    cur.execute(insert_script, insert_value)
    conn.commit()

except Exception as error:
    print(error)

finally:
    if cur != None:
        cur.close()
    if conn != None:
        conn.close()




