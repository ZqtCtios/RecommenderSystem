import pymysql
"""[summary]

[合并标签]
"""
db = pymysql.connect(
    "localhost",
    "root",
    "Zqt_1997",
    "Data",
    use_unicode=True,
    charset="utf8")
cursor = db.cursor()


def findInCate(hostname):
    """
    
    [查找hostname是否在categorization_2数据库中]
    
    Arguments:
        hostname {[str]} -- [主域名]
    
    Returns:
        [boolean] -- [结果]
    """
    sql = 'SELECT * from categorizations_2 where hostname=%s'
    cursor.execute(sql, (hostname))
    ans = cursor.fetchall()
    if len(ans) > 0:
        return False
    return True

def getHostname(hostname):
    a=[]
    for i in range(len(hostname)):
        if hostname[i]=='.':
            a.append(i)
    if len(a)==0:
        return hostname
    if len(a)==1:
        return hostname[:a[0]]
    if hostname[a[0]+1:a[1]]=='com':
        return hostname[0:a[0]]
    return hostname[a[0]+1:a[1]]
    
def readWebsiteLcsData():
    db = pymysql.connect(
    "localhost",
    "root",
    "Zqt_1997",
    "test",
    use_unicode=True,
    charset="utf8")
    cursor = db.cursor()
    sql = 'SELECT * FROM `test.website_lcs` WHERE tag_1<>\'Uncategorized\''
    cursor.execute(sql)
    ans = cursor.fetchall()
    for x in ans:
        hostname = getHostname(x[0])
        tag_1 = x[1]
        tag_2 = x[2]
        if findInCate(hostname):
            print(hostname,tag_1)
       
if __name__ == '__main__':
    readWebsiteLcsData()
    
