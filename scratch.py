import sqlite3
from jinja2 import Template

conn = sqlite3.connect(':memory:')
conn.row_factory = sqlite3.Row
conn.execute('CREATE TABLE t (id INT, val TEXT)')
conn.execute("INSERT INTO t VALUES (1, 'hello')")
row = conn.execute('SELECT * FROM t').fetchone()

print(Template('Jinja says: {{ r.id }}').render(r=row))
