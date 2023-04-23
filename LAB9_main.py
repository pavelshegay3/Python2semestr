import psycopg2
import os.path
import csv
from configparser import ConfigParser

general_path = "SQL files"

while True:
    f = 0


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


    def main_menu():
        print("Type 1 to insert data through console\nType 2 to insert data with your CSV file\nType 3 to change your PhoneBook\nType 4 to delete a contact\nType 5 to search a contact\nType 0 to exit")
        x = int(input())
        return x


    def exit_menu():
        print("Session is finished\nType 1 to repeat\nType 0 to exit")
        x = int(input())
        return x


    def connect_and_insert_from_console(contact_id, contact_name, contact_num):
        # index 1
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
            global f
            f=1
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')


    def connect_and_insert_from_csv(csv_file_path):
        # index 2
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
            global f
            f = 1
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')


    def update(contact_id, new_contact_name, new_contact_num):
        # index 3
        conn = None
        try:
            params = config()
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)

            cur = conn.cursor()
            print('PostgreSQL database version:')
            cur.execute('SELECT version()')

            cur.execute("UPDATE pb SET contact_name = %s, contact_num = %s WHERE contact_id = %s",
                        (new_contact_name, new_contact_num, contact_id))

            conn.commit()
            cur.close()
            check_if_changed = cur.rowcount
            global f
            if check_if_changed == 0:
                f = 0
            else:
                f = 1
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')

    def delete(contact_id) :
        # index 4
        conn = None
        try:
            params = config()
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)

            cur = conn.cursor()
            print('PostgreSQL database version:')
            cur.execute('SELECT version()')
            cur.execute("DELETE FROM pb WHERE contact_id = %s", (contact_id,))
            check_if_deleted = cur.rowcount
            global f
            if check_if_deleted == 0:
                f = 0
            else:
                f = 1
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')

    def get_phone_book_record(pattern):
        # index 5
        conn = None
        try:
            params = config()
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)

            cur = conn.cursor()
            print('PostgreSQL database version:')
            cur.execute('SELECT version()')

            cur.execute("SELECT * FROM pb WHERE contact_name ILIKE %s OR contact_num ILIKE %s",
                        ('%' + pattern + '%', '%' + pattern + '%'))

            rows = cur.fetchall()
            global f
            if len(rows) == 0:
                f = 0
            else:
                for row in rows:
                    print(f"contact_id: {row[0]}, contact_name: {row[1]}, contact_num: {row[2]}")
                    f=1
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')



    if __name__ == '__main__':
        res = main_menu()
        if res == 1:
            contact_id = input("Enter contact ID: ")
            contact_name = input("Enter contact name: ")
            contact_num = input("Enter contact number: ")
            connect_and_insert_from_console(contact_id, contact_name, contact_num)
            if f == 1:
                print("Done!")
                exit = exit_menu()
                if exit == 1:
                    print("Restarting...")
                if exit == 0:
                    print("Exiting...")
                    break

            if f == 0:
                print("Oops! Something went wrong")
                exit = exit_menu()
                if exit == 1:
                    print("Restarting...")
                if exit == 0:
                    print("Exiting...")
                    break

        if res == 2:
            file_name = input("Enter the name of your CSV file (make sure it is located in \"SQL files\" folder): ")
            csv_file_path = os.path.join(general_path, file_name)
            connect_and_insert_from_csv(csv_file_path)
            if f == 1:
                print("Done! Data from", file_name, "located in", general_path, "has been transferred successfully.")
                exit = exit_menu()
                if exit == 1:
                    print("Restarting...")
                if exit == 0:
                    print("Exiting...")
                    break

            if f == 0:
                print("Oops! Something went wrong")
                exit = exit_menu()
                if exit == 1:
                    print("Restarting...")
                if exit == 0:
                    print("Exiting...")
                    break

        if res == 3:
            contact_id = input("Enter the contact_id you would like to change: ")
            new_contact_name =  input("Enter the new contact name: ")
            new_contact_num = input("Enter the new contact_num: ")
            update(contact_id, new_contact_name, new_contact_num)
            if f == 1:
                print("Done! Contact with contact_id", contact_id, "has been changed successfully.")
                print("New name is", new_contact_name)
                print("New number is", new_contact_num)
                exit = exit_menu()
                if exit == 1:
                    print("Restarting...")
                if exit == 0:
                    print("Exiting...")
                    break

            if f == 0:
                print("Oops! Something went wrong")
                exit = exit_menu()
                if exit == 1:
                    print("Restarting...")
                if exit == 0:
                    print("Exiting...")
                    break

        if res == 4:
            contact_id = input("Enter contact ID you would like to delete: ")
            delete(contact_id)
            if f == 1:
                print("Done! Contact with contact_id", contact_id, "has been deleted successfully.")
                exit = exit_menu()
                if exit == 1:
                    print("Restarting...")
                if exit == 0:
                    print("Exiting...")
                    break

            if f == 0:
                print("Oops! Something went wrong. Check if the contact_id input is correct.")
                print("contact_id", contact_id, "not found.")
                exit = exit_menu()
                if exit == 1:
                    print("Restarting...")
                if exit == 0:
                    print("Exiting...")
                    break

        if res == 5:
            pattern = input("Enter contact_name or contact_number you would like to search: ")
            get_phone_book_record(pattern)
            if f == 1:
                print("Done!")
                exit = exit_menu()
                if exit == 1:
                    print("Restarting...")
                if exit == 0:
                    print("Exiting...")
                    break

            if f == 0:
                print("Oops! Something went wrong")
                print("No contact has been found by the following search:", pattern)
                exit = exit_menu()
                if exit == 1:
                    print("Restarting...")
                if exit == 0:
                    print("Exiting...")
                    break
        if res == 0:
            print("Exiting...")
            break
