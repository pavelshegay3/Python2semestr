import psycopg2
from configparser import ConfigParser


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


def connect_and_insert_from_console(contact_id, contact_name, contact_num):
    conn = None
    try:
        params = config()
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        cur.execute("INSERT INTO pb (contact_id, contact_name, contact_num) VALUES (%s, %s, %s)",
                    (contact_id, contact_name, contact_num))

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    contact_id = input("Enter contact ID: ")
    contact_name = input("Enter contact name: ")
    contact_num = input("Enter contact number: ")
    connect_and_insert_from_console(contact_id, contact_name, contact_num)
