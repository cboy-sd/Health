#! /usr/bin/env python
import MySQLdb
from decouple import config, Csv

host = "db"
passwd = config('MYSQL_PASSWORD')
user = config('MYSQL_USER')
dbname = config('MYSQL_DATABASE')

db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=dbname)
cursor = db.cursor()

cursor.execute("ALTER DATABASE `%s` CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci'" % dbname)

sql = "SELECT DISTINCT(table_name) FROM information_schema.columns WHERE table_schema = '%s'" % dbname
cursor.execute(sql)

results = cursor.fetchall()

for row in results:
    try:
        sql = "ALTER TABLE `%s` convert to character set DEFAULT COLLATE DEFAULT" % (row[0])
        cursor.execute(sql)
    except Exception as e:
        print('error: ', e)
db.close()
