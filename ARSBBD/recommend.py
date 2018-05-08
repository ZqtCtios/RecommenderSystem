import pymysql

def userAgent_classify():
    db = pymysql.connect(
        "localhost",
        "root",
        "Zqt_1997",
        "Data",
        use_unicode=True,
        charset="utf8")
    cursor = db.cursor()
    sql1 = 'select id,useid from user'
    cursor.execute(sql1)
    type = cursor.fetchall()
    print(type)
if __name__ == '__main__':
    userAgent_classify()


