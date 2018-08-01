import MySQLdb


try:
    conn = MySQLdb.connect(host='localhost', port=3306, db='test1', user='root', passwd='password', charset='utf8')
    cur = conn.cursor()
    sname = input("请输入学生姓名：")
    params = [sname]
    count = cur.execute('insert into students(sname) values(%s)', params)  # 指定sql语句，将需要更新的数据已参数化的形式传入;
    """
    也是防sql注入的一种形式
    """
    print(count)
    conn.commit()
    cur.close()
    conn.close()
except Exception as e:
    print(e)
