# 提取网址的主干
import pymysql
import threading
db = pymysql.connect(
    "localhost",
    "root",
    "Zqt_1997",
    "Data",
    use_unicode=True,
    charset="utf8")
cursor = db.cursor()
"""[连接数据库]



"""


def is_int(x):
    """[判断是否是纯数字]

    Arguments:
        x {str} -- 待识别的字符创

    Returns:
        Boolean -- 结果
    """
    try:
        int(x)
    except ValueError:
        return False
    return True


def clear_all_num():
    """[删除所有的ip地址类的网站]
    """
    sql = 'select hostname from hostname'
    sql2 = 'delete from hostname where hostname=%s'
    cursor.execute(sql)
    ans = cursor.fetchall()
    for x in ans:
        url = x[0].replace('.', '').replace(':', '')
        if is_int(url):
            cursor.execute(sql2, (x[0]))
            print('delete', x[0])
            db.commit()


def find_weblcs(s1, s2):
    """[find_weblcs]

    [找到两个网址之间的最长公共部分]

    Arguments:
        s1 {[str]} -- [网址一]
        s2 {[str]} -- [网址二]

    Returns:
        [str] -- [最长公共部分]
    """
    s1 = s1[::-1]
    s2 = s2[::-1]
    length = min(len(s1), len(s2))
    x = 0
    y = 0
    for i in range(length):
        if s1[i] != s2[i]:
            break
        if s1[i] == '.':
            y += 1
            if y == 3:
                x += 1
                break
        x += 1
    if x == 0:
        return ""
    else:
        return s1[0:x][::-1]


def del_web_port(website):
    """
    [去除网址端口]

    """
    if ':' in website:
        x = website.find(':')
        return website[:x]
    else:
        return website


def find_all_lscHostname():
    sql = 'select hostname from hostname'
    sql2 = 'INSERT into website_lcs(hostname) VALUES (%s)'
    cursor.execute(sql)
    ans = cursor.fetchall()
    length = len(ans)
    sql2 = 'INSERT into website_lcs(hostname) VALUES (%s)'
    webs = {}
    for i in range(length):
        for j in range(length):
            x = del_web_port(ans[i][0])
            y = del_web_port(ans[j][0])
            lcs = find_weblcs(x, y)
            if len(lcs) <= 4 or lcs[0] != '.':
                continue
            lcs = lcs[1:]
            webs[lcs] = 1
    webs = list(webs.keys())
    webs.sort(key=lambda x: len(x))
    for web in webs:
        print("Find :",web)
        cursor.execute(sql2,(web))
        db.commit()
    

if __name__ == '__main__':
    print('StartWorking....')
    find_all_lscHostname()
