import pymysql
import requests
import threading
dict = {'vivo': 'vivo',
        'x600': 'letv',
        'MIUI': 'MIUI', 'MI': 'MIUI', 'HM': 'MIUI', 'NOMI': 'MIUI',
        'CFNetwork': 'iPhone', 'iPhone': 'iPhone', 'OS': 'iPhone', 'CaptiveNetworkSupport': 'iPhone', 'Apple': 'iPhone',
        'm2 note Build': 'MEIZU', 'MEIZU': 'MEIZU',
        'R7Plus': 'oppo', 'oppo': 'oppo', 'A51': 'oppo',
        'HUAWEI': 'HUAWEI', 'Che1': 'HUAWEI',
        'GT': 'samsung', 'samsung': 'samsung', 'SM': 'samsung',
        'lenovo': 'lenovo',
        'Coolpad': 'Coolpad',
        'ZTE': 'ZTE'
        }
dict_cost = {'iPhone': 4,
             'samsung': 3, 'HUAWEI': 3,
             'oppo': 2, 'vivo': 2, 'MIUI': 2,
             'lenovo': 1, 'Coolpad': 1, 'letx': 1, 'ZTE': 1
             }

dict_age = {'HUAWEI': 4, 'samsung': 4,
            'iPhone': 3, 'MIUI': 3,
            'vivo': 2, 'oppo': 2,
            'lenovo': 1, 'Coolpad': 1, 'ZTE': 1, 'letx': 1
            }

dict_sex = {'iPhone': 3, 'sumsung': 3,
            'MIUI': 2, 'HUAWEI': 2, 'lenovo': 2, 'Coolpad': 2, 'ZTE': 2, 'letx': 2,
            'oppo': 1, 'vivo': 1
            }


def readData():
    db = pymysql.connect(
        "localhost",
        "root",
        "Zqt_1997",
        "Train",
        use_unicode=True,
        charset="utf8")
    cursor = db.cursor()
    sql = 'select useraddress,userAgent from data'
    cursor.execute('truncate table user_attribute')
    db.commit()
    cursor.execute(sql)
    data = cursor.fetchall()
    db.close()
    return data


def classify(all_userAgent):
    db = pymysql.connect(
        "localhost",
        "root",
        "Zqt_1997",
        "Train",
        use_unicode=True,
        charset="utf8")
    cursor = db.cursor()
    sql2 = 'insert into user_attribute(useraddress,type,consumption_level,age,sex) values (%s,%s,%s,%s,%s)'
    for row in all_userAgent:
        id = row[1]
        for name in dict.keys():
            if id.find(name) >= 0:
                useraddress = row[0]
                phone_type = dict[name]
                try:
                    cost = dict_cost[name]
                    sex = dict_sex[name]
                    age = dict_age[name]
                except:
                    cost = 0
                    sex = 0
                    age = 0
                cursor.execute(sql2, (useraddress, phone_type, cost, age, sex))
                break

        db.commit()
    db.close()


def work():
    data = readData()
    dataLen = len(data)
    print(dataLen)
    threadNum = 20
    x = dataLen // threadNum
    Thead = []
    print('Get UserAgent_classify')
    for r in range(0, threadNum-1):
        t = threading.Thread(target=classify, args=(data[r * x:r * x + x],))
        print('Thread-{} is working....'.format(r+1))
        Thead.append(t)
    r = threadNum-1
    t = threading.Thread(target=classify, args=(data[r * x:r * x + x],))
    print('Thread-{} is working....'.format(threadNum))
    Thead.append(t)
    for t in Thead:
        t.start()

    for t in Thead:
        t.join()
    print('Done!')


if __name__ == '__main__':
    work()
