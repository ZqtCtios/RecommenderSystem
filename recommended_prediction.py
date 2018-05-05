import pymysql
import operator
import threading
db = pymysql.connect(
    "localhost",
    "root",
    "Zqt_1997",
    "Data",
    use_unicode=True,
    charset="utf8")
cursor = db.cursor()

def getUserData():
    sql = 'select * from user'
    cursor.execute(sql)
    userData = cursor.fetchall()
    return userData


def getDistance(a, b):
    tmp = [val for val in a if val in b]
    if len(tmp) == 0:
        return 0
    dis = len(tmp) / (len(a) * len(b))**0.5
    return dis


def getItem(data):
    item = []
    for i in range(len(data)):
        if float(data[i]) >= 0.25:
            item.append(i)
    return item


def calDistance(userdata):
    db_temp = pymysql.connect(
        "localhost",
        "root",
        "Zqt_1997",
        "Data",
        use_unicode=True,
        charset="utf8")
    cursor_temp = db_temp.cursor()
    sql = 'INSERT INTO recommended_prediction(Predict_causes,Predict_outcomes) VALUES (%s,%s)'
    for user in userdata:
        user_distance = {}
        all_data_2 = {}
        data_1 = getItem(user[2:])
        for user_2 in userdata:
            if user[0] == user_2[0]:
                continue
            data_2 = getItem(user_2[2:])
            dis = getDistance(data_1, data_2)
            user_distance[user_2[0]] = dis
            all_data_2[user_2[0]] = data_2
        sortUserDistance = sorted(
            user_distance.items(),
            key=lambda item: item[1],
            reverse=True)
        items = []
        for i in range(15):
            userid = sortUserDistance[i][0]
            items.append(all_data_2[userid])
        rec = getOneRec(items)
        rec_set = [x for x in rec if x not in data_1]
        cursor_temp.execute(sql, (str(data_1), str(rec_set[:1])))
        db_temp.commit()
    cursor_temp.close()


def getOneRec(distance):
    dic = {}
    for line in distance:
        for item in line:
            if item not in dic.keys():
                dic[item] = 0
            dic[item] += 1

    sortedDic = sorted(
        dic.items(),
        key=lambda item: item[1],
        reverse=True)
    ans = [x[0] for x in sortedDic]
    return ans



    
    
    
        

def work():
    import time
    t1=time.time()
    userData = getUserData()
    dataLen = len(userData)
    x = dataLen // 5
    Thead = []
    print('Cata to Data....')
    for r in range(0, 5):
        t = threading.Thread(target=calDistance,
                             args=(userData[r * x:r * x + x],))
        print('Thread-{} is working....'.format(r))
        Thead.append(t)

    t = threading.Thread(target=calDistance, args=(userData[x * 5:dataLen],))
    print('Thread-{} is working....'.format(5))
    Thead.append(t)
    for t in Thead:
        t.start()

    for t in Thead:
        t.join()
    print(time.time()-t1)
    

if __name__ == '__main__':
    work()
    cursor.close()
