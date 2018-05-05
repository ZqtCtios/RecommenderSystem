import pymysql
db = pymysql.connect(
    "localhost",
    "root",
    "Zqt_1997",
    "test",
    use_unicode=True,
    charset="utf8")
cursor = db.cursor()

sql = 'select * from website_lcs_lv1'
cursor.execute(sql)
web_cates = cursor.fetchall()


def get_cate(hostname):
    hostname = str(hostname)
    maxlen = 0
    for row in web_cates:
        add = hostname.find(str(row[0]))
        if add == 0:
            return row[1]
    return 'Uncategorized'


def work():
    sql = 'select id,hostname from data_2'
    sql2 = 'update data_2 set tag_1=%s where id=%s'
    cursor.execute(sql)
    ans = cursor.fetchall()
    for row in ans:
        id = row[0]
        print(id)
        hostname = row[1]
        cate = get_cate(hostname)

        cursor.execute(sql2, (cate, id))
        db.commit()


if __name__ == '__main__':
    work()
