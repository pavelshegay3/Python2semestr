import os.path

import psycopg2
import csv
from configparser import ConfigParser

general_path = "SQL files"

def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    db_params = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db_params[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db_params


def connect_and_insert_from_csv(csv_file_path):
    conn = None
    try:
        params = config()
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        with open(csv_file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                cur.execute("INSERT INTO pb (contact_id, contact_name, contact_num) VALUES (%s, %s, %s)", row)

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    file_name = input("Enter the name of your CSV file (make sure it is located in \"SQL files\" folder: ")
    csv_file_path = os.path.join(general_path, file_name)
    connect_and_insert_from_csv(csv_file_path)