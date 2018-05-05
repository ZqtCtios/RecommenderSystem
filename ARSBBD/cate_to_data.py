import pymysql
import threading
db = pymysql.connect(
    "localhost",
    "root",
    "Zqt_1997",
    "Train",
    use_unicode=True,
    charset="utf8")
cursor = db.cursor()

sql = 'select * from hostname_classification'
cursor.execute(sql)
web_cates = cursor.fetchall()


def get_cate(hostname):
    hostname = str(hostname)
    maxlen = 0
    cate_list = 'Uncategorized'
    for row in web_cates:
        add = hostname.find(str(row[1]))
        if add >= 0 and add > maxlen:
            maxlen = add
            cate_list = row[2]
    return cate_list


def readData():
    sql = 'select id,hostname from data'
    cursor.execute(sql)
    data = cursor.fetchall()
    return data


def classify(data, l, r):
    db_temp = pymysql.connect(
        "localhost",
        "root",
        "Zqt_1997",
        "Train",
        use_unicode=True,
        charset="utf8")
    cursor_temp = db_temp.cursor()
    sql = 'update data set tag=%s where id=%s'
    for i in range(l, r):
        row = data[i]
        id = row[0]
        hostname = row[1]
        cate = get_cate(hostname)
        cursor_temp.execute(sql, (cate, id))
        db_temp.commit()
    db_temp.close()


def work():
    data = readData()
    dataLen = len(data)
    threadNum = 20
    x = dataLen // threadNum
    Thead = []
    print('Get User Categorization')
    for r in range(0, threadNum-1):
        t = threading.Thread(target=classify, args=(data, r * x, r * x + x))
        print('Thread-{} is working....'.format(r+1))
        Thead.append(t)
    r = threadNum-1
    t = threading.Thread(target=classify, args=(data, r * x, dataLen))
    print('Thread-{} is working....'.format(threadNum))
    Thead.append(t)
    for t in Thead:
        t.start()

    for t in Thead:
        t.join()
    print('Done!')


if __name__ == '__main__':
    work()
