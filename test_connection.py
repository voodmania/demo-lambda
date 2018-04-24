from handler import INSERT
from connection import Connection

conn = Connection({'CONN_STRING': 'dbname=test host=test.xxxxxxxxxx.eu-west-1.rds.amazonaws.com port=5432 user=xxxxxxxx password=xxxxxxxxx'})
conn.execute(INSERT, ('test-1', 'test-2', 'test-3'))
