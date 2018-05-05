import pymysql
db = pymysql.connect(
    "localhost",
    "root",
    "Zqt_1997",
    "Data",
    use_unicode=True,
    charset="utf8")
cursor = db.cursor()


def creat_table():
    print('Creat User Data Table.....')
    sql = 'select name from lables'
    cursor.execute(sql)
    cates = []
    for row in cursor.fetchall():
        cates.append(row[0])
    sql = 'CREATE TABLE user ( userid TEXT NOT NULL '
    dic = {}
    for cate in cates:
        sql += ',{} DOUBLE NOT NULL'.format(cate[:3])
        dic[cate] = 0
    sql += ') ENGINE = InnoDB'
    print(sql)
    try:
        cursor.execute(sql)
        db.commit()
        print('Done!')
    except BaseException:
        print('Fail!')
    return dic


def make_data(dic):
    print('Format User_Data..')
    sql = 'SELECT useraddress FROM data GROUP BY useraddress'
    cursor.execute(sql)
    rows = cursor.fetchall()
    useraddress = []
    user_data = {}
    for row in rows:
        useraddress.append(row[0])
    sql2 = 'select tag from data where useraddress=%s'
    for user in useraddress:
        user_data[user] = dic.copy()
        cursor.execute(sql2, user)
        rows = cursor.fetchall()
        print(user)
        for row in rows:
            if str(row[0]) == 'Uncategorized':
                continue
            user_data[user][row[0]] += 1
        sum=0
        for key in user_data[user].keys():
            sum += user_data[user][key]
        if sum==0:
            continue
        for key in user_data[user].keys():
            user_data[user][key] /= sum
        print(user_data)
    print('Done!')
    return useraddress, user_data


def save_to_db(dic, useraddress, user_data):
    print('Sava UserData to db')
    sql='insert into user values(%s'
    for x in range(len(dic.keys())):
        sql += ',%s'
    sql += ')'
    print(sql)
    for user in useraddress:
        dic=user_data[user].copy()
        data=list(dic.values())
        data.insert(0, user)
        print(len(data), data)
        cursor.execute(sql, data)
        db.commit()
    print('Done!')

if __name__ == '__main__':
    dic=creat_table()
    useraddress, user_data=make_data(dic)
    save_to_db(dic, useraddress, user_data)
