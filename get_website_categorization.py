import website_categorization_API as wc
import pymysql
db = pymysql.connect(
    "localhost",
    "root",
    "Zqt_1997",
    "Data",
    use_unicode=True,
    charset="utf8")
cursor = db.cursor()


def start():
    sql = 'select hostname from website_lcs where length(tag_1)<5'
    sql2 = 'update website_lcs set tag_1=%s,tag_2=%s where hostname=%s'
    cursor.execute(sql)
    ans = cursor.fetchall()
    print("Lengh:",len(ans))
    for url in ans:
        url = url[0]
        c = wc.find_categories(url)
        print(url,":",c)
        cursor.execute(sql2, (c[0], c[1], url))
        db.commit()
    print('ok')

def get_categorizations():
    sql3 = 'select tag_1 from website_lcs group by tag_1'
    cursor.execute(sql3)
    ans = cursor.fetchall()
    print(len(ans))
    sql4 = 'INSERT into categorizations(name) VALUES (%s)'
    for row in ans:
        print(row[0])
        cursor.execute(sql4, (row[0]))
        db.commit()   

if __name__ == '__main__':
    get_categorizations()
