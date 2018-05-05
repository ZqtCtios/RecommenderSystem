import pymysql
from sklearn.cluster import KMeans
db = pymysql.connect(
    "localhost",
    "root",
    "Zqt_1997",
    "test",
    use_unicode=True,
    charset="utf8")
cursor = db.cursor()


def get_data():
    data = []
    sql = 'select * from user'
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        data.append(row[1:-2])
#    print(data)
    return data


def k_mean(data):
    kmeans = KMeans(n_clusters=10)  # n_clusters:number of cluster
    kmeans.fit(data)
    labels = list(kmeans.labels_)
    # print(labels)
    sql = 'select userid from user'
    cursor.execute(sql)
    rows = cursor.fetchall()
    for i in range(len(rows)):
        userid = rows[i][0]
        kind = labels[i]
        print(userid, kind)
        sql2 = 'update user set kind=%s where userid=%s'
        cursor.execute(sql2, (int(kind), str(userid)))
        db.commit()


if __name__ == '__main__':
    data = get_data()
    k_mean(data)
