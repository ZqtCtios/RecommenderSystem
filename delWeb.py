import pymysql
db = pymysql.connect(
    "localhost",
    "root",
    "Zqt_1997",
    "test",
    use_unicode=True,
    charset="utf8")
cursor = db.cursor()
dic = {}


def find_last(string, str):
    last_position = -1
    while True:
        position = string.find(str, last_position + 1)
        if position == -1:
            return last_position
        last_position = position


def statistics():
    sql = 'select website from web where ok=1'
    cursor.execute(sql)
    ans = cursor.fetchall()
    print('find {} website'.format(len(ans)))
    for website in ans:
        website = website[0]
        x = find_last(website, '.')
        if x == -1:
            continue
        else:
            suffix = website[x + 1:]
            if len(suffix) > 5:
                continue
            dic[suffix] = 1

    print(dic)


# def deleteWebsite():


if __name__ == '__main__':
    statistics()
