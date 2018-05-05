import pymysql
db = pymysql.connect(
    "localhost",
    "root",
    "Zqt_1997",
    "Data",
    use_unicode=True,
    charset="utf8")
cursor = db.cursor()
def delete():
    sql='select * from recommended_prediction'
    cursor.execute(sql)
    data=cursor.fetchall()
    dic={}
    for line in data:
        user_id=str(line[1])
        if user_id not in dic.keys():
            a=[]
            a.append(line[2])
            dic[user_id]=a
        else:
            dic[user_id].append(line[2])
    sql2='TRUNCATE recommended_prediction'
    cursor.execute(sql2)
    sql = 'INSERT INTO recommended_prediction(Predict_causes,Predict_outcomes) VALUES (%s,%s)'
    for key in dic.keys():
        a=dic[key]
        maxn=0
        ans=''
        for x in a:
            if maxn<a.count(x):
                maxn=a.count(x)
                ans=x
        cursor.execute(sql,(key,ans))
        db.commit()

if __name__ == '__main__':
    delete()
    