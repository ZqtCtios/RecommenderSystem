import pymysql
db = pymysql.connect(
    "localhost",
    "root",
    "Zqt_1997",
    "test",
    use_unicode=True,
    charset="utf8")
cursor = db.cursor()


def load_data():
    users = {}
    sql = 'select * from user'
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        userid = row[0]
        data = row[1:-3]
        kind = row[-1]
        users[userid] = {'data': data, 'kind': kind}
    return users


def show(users, kind, size):
    show_list = []
    for userid in users.keys():
        user_kind = users[userid]['kind']
        if user_kind == kind:
            user_data = users[userid]['data']
            show_list.append({'userid': userid, 'data': user_data})
    for i in range(size):
        userid = show_list[i]['userid']
        data = show_list[i]['data']


if __name__ == '__main__':
    users = load_data()
