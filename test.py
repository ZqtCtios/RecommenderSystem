import requests
import time
headers = {
    'Content-Type':
    'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':
    'adfbid2=0; NTKF_T2D_CLIENTID=guestFDD385A6-D3E5-572E-2415-138D17B77B0C; JSSearchModel=0; LastCity%5Fid=530; LastCity=%e5%8c%97%e4%ba%ac; urlfrom2=121126445; adfcid2=none; dywez=95841923.1521440380.10.6.dywecsr=sou.zhaopin.com|dyweccn=(referral)|dywecmd=referral|dywectr=undefined|dywecct=/jobs/searchresult.ashx; __utmz=269921210.1521440380.9.5.utmcsr=sou.zhaopin.com|utmccn=(referral)|utmcmd=referral|utmcct=/jobs/searchresult.ashx; LastSearchHistory=%7b%22Id%22%3a%22fbf583aa-bee5-44f6-a947-fccbca372fe1%22%2c%22Name%22%3a%22%e5%a4%a7%e6%95%b0%e6%8d%ae+%2b+%e4%b8%8a%e6%b5%b7%2b%e5%b9%bf%e5%b7%9e%2b%e6%b7%b1%e5%9c%b3%2b%e6%ad%a6%e6%b1%89%2b%e9%9d%92%e5%b2%9b%22%2c%22SearchUrl%22%3a%22http%3a%2f%2fsou.zhaopin.com%2fjobs%2fsearchresult.ashx%3fjl%3d%25e4%25b8%258a%25e6%25b5%25b7%2b%25e5%25b9%25bf%25e5%25b7%259e%2b%25e6%25b7%25b1%25e5%259c%25b3%2b%25e6%25ad%25a6%25e6%25b1%2589%2b%25e9%259d%2592%25e5%25b2%259b%26kw%3d%25e5%25a4%25a7%25e6%2595%25b0%25e6%258d%25ae%26p%3d1%26isadv%3d0%22%2c%22SaveTime%22%3a%22%5c%2fDate(1521455640116%2b0800)%5c%2f%22%7d; urlfrom=121126445; adfcid=none; adfbid=0; dywea=95841923.2707600650469464000.1520746324.1521453756.1522151971.12; dywec=95841923; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1521166289,1521437735,1521453756,1522151971; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1522151971; __utma=269921210.441461085.1520746324.1521453756.1522151972.11; __utmc=269921210; __utmt=1; Token=41a88c42bd644e68b48a49452c4b590a; RDsUserInfo=386b2e69567140655e700169436d5c6a516b47775c6f45355275216b24695671126501705c69146d086a366b10775e6f23353d75506b5b69507135652b700869416d5f6a5b6b4477546f423551755c6b51692a71236552700669586d596a5e6b5177526f4a355c75546b51692a713b65527005694e6d3e6a286b4c772f6f3c355875596b5c695c714f6559700c69406d5a6a526b2477316f4d355875586b59695071246526700869476d506a9; uiioit=213671340f69426b5c6a5c79426444740e35023250755e6d51683b742073493601340669476b586a597946644b7407350f328; at=41a88c42bd644e68b48a49452c4b590a; rt=961d478ab3c049b49a961d3f8650b4d9; companyCuurrentCity=703; nTalk_CACHE_DATA={uid:kf_9051_ISME9754_44251281,tid:1522152018393266}; festivalDay=1; stayTimeCookie=1522152019953; referrerUrl=https%3A//ihr.zhaopin.com/; dyweb=95841923.21.9.1522152270123; __utmb=269921210.21.9.1522152270129',
    'Host':
    'ihr.zhaopin.com',
    'Origin':
    'https://ihr.zhaopin.com',
    'Referer':
    'https://ihr.zhaopin.com/job/jobadd.html',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    'X-Requested-With':
    'XMLHttpRequest'
}
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

# 代理隧道验证信息
proxyUser = "HP07809N4O4MEA8D"
proxyPass = "49A1ECE7666C0CF0"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}

session = requests.session()
data = {
    'type':'1',
    'groupid': '0',
    'jobpostionnumber': '',
    'currentdate': int(time.time()),
    'filterid': '0',
    'jobTemplates': '0',
    'jobtitle': '第四季度及四',
    'positionnature': '2',
    'traveloption': '1',
    'jobTypeMain': '160000',
    'subJobTypeMain': '45',
    'provinceid': '489',
    'cityid': '530',
    'cqid': '0',
    'workplace': '莱西市经济开发区滨河东路60号',
    'startdate': '2018-03-27',
    'enddate': '30',
    'monthsalary': '0100002000',
    'quantity': '1',
    'mineducationlevel': '-1',
    'minyearsval': '',
    'minyears': '-1',
    'jobdescription':
    '<p>萨季度撒谎大蒜的挥洒udhsaudhsaudhsaudhsaudhasududhsaudhsaudh</p>',
    'benefit': '',
    'emaillist': '',
    'departmentid': '0',
    'seqnumber': '500',
    'applicationmethod': '1'
}
url='https://ihr.zhaopin.com/api/job/jobaddpost.do'
session.post(url,headers=headers,params=data,proxies=proxies)
print(session)