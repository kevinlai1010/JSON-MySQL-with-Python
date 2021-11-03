import json
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_test"
)
mycursor = mydb.cursor()


def get_data():
    with open('json_example.json') as json_data:
        data = json.load(json_data)
        for channel in data.values():
            return channel

def test():
    tables = get_data()
    for table_entry in tables:
        record_data = table_entry.items()
        for k, v in record_data:
            if isinstance(v, list):
                create_table(k, [key for key in v[0]])
                keys = []
                for record in v:
                    query = "insert into " + k + " ("
                    for key in record:
                        query = query + key + ","
                    query = query[:-1] + ") values ( '"

                    # keys = [key for key in record]
                    for value in record.values():
                        query = query + value + "','"
                    query = query[:-2] + ")"
                    # values = [value for value in record.values()]

                    # query = "insert into {} ({}) values ({})".format(k, keys, values)
                    mycursor.execute(query)
                    mydb.commit()


def create_table(table_name, keys):
    query = "create table if not exists " + table_name + "("
    for key in keys:
        query = query + key + " VARCHAR(255),"
    query = query[:-1] + ")"
    mycursor.execute(query)


test()
