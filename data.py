import pymysql
import requests
import threading
import time


def testWeb(url, userAgent):
    headers = {
        'User-Agent': userAgent
    }
    try:
        s = requests.get(url, headers=headers, timeout=1).status_code
        # print(s)
        if s == 200:
            return True
        else:
            return False
    except BaseException:
        return False


def test(start, end):
    print(start, '->', end)
    db = pymysql.connect(
        "localhost",
        "root",
        "Zqt_1997",
        "test",
        use_unicode=True,
        charset="utf8")
    cursor = db.cursor()
    sql = 'select website,userAgent from web limit %s,%s'
    sql2 = 'update web set ok=1 where website=%s'
    cursor.execute(sql, (start, end))

    ans = cursor.fetchall()
    for x in ans:
        url = x[0]
        userAgent = x[1]
        if testWeb(url, userAgent):
            cursor.execute(sql2, (url))
            db.commit()


if __name__ == '__main__':
    Thread = []
    for i in range(0, 80000, 1000):
        t1 = time.time()
        test(i, i + 1000)
        t2 = time.time() - t1
        print('Time:', t2)
