import sqlite3
conn = sqlite3.connect(":memory:")
conn.execute(
    """
    create table catalog(
        id integer,
        pid integer,
        name varchar(10),
        nickname text NULL)""")
for t in ((0,10,'abc','Yu'),(1,20,'cba','Xu'),(0,10,'abc','Yu')):
    conn.execute("insert into catalog values (?,?,?,?)", t)
cu = conn.cursor()
cu.execute("select id, group_concat(name) from catalog group by id")
print(cu.fetchall())
cu.close()
conn.close()
