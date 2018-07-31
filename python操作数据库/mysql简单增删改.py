import MySQLdb

try:
    conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='password', db='ceshi', charset='utf8')
    cur = conn.cursor()
    sql_insert = "insert into test(name) values('xiaoming')"
    # sql_update = "update test set name='xiaohaong' where id=1"
    # sql_delete = "delete from test where id=1"
    cur.execute(sql_insert)
    # cur.execute(sql_update)
    # cur.execute(sql_delete)
    conn.commit()
    cur.close()
    conn.close()
except Exception as e:
    print(e)

