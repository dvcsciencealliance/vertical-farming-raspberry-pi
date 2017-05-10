import json
import datetime
import psycopg2


class Database:
    timeFormat = '%Y-%m-%d %H:%M:%S'
    cur = None
    conn = None
    def __init__(self):
        with open('config/db.json') as data_file:
            cfg = json.load(data_file)
        username = cfg['username']
        password = cfg['password']
        host = cfg['host']
        databasename = cfg['databasename']
        self.conn = psycopg2.connect(host = host, user = username, password = password, dbname = databasename)
        self.cur = self.conn.cursor()

    def insert(self, data, name):
        if len(data) < 1:
            return

        now = datetime.datetime.now()
        keys = 'time'
        values = [now.strftime(self.timeFormat)]
        replacement = '%s'
        for key, value in data.items():
            keys += ', ' + key
            values += [value]
            replacement += ', %s'
        query = "INSERT INTO %s (%s) VALUES (%s)" % (name, keys, replacement)
        print(query, values)
        self.cur.execute(query, values)
        self.conn.commit()

    def __exit__(self, exc_type, exc_value, traceback):
        self.cur.close()
        self.conn.close()
    