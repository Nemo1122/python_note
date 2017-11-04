import pymysql


def mysql_data(config, sql):
    """通过数据库获取数据，返回参数sql语句所能查出的所有数据
    :param
    config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'db': 'ecshop',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor  # 加上这个参数会将查询结果变为[{"字段名":"字段值",...},{}]的形式
    }
    sql = "SELECT * FROM ecs_article_cat"
    :return
    count, 语句执行的条数
    all_data, fetchall，也就是通过sql语句能查出的所有数据((),()),是一个二维元组
    """

    db = pymysql.connect(**config)
    try:
        cur = db.cursor()
        cur.execute(sql)
        all_data = cur.fetchall()
    except pymysql.err.DatabaseError as de:
        print(de)
        all_data = None
    finally:
        db.close()
    return all_data
