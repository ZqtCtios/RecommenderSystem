import requests
import re
url='http://qq.yh31.com/zjbq/0551964.html'
html=requests.get(url).text
p=r'<img class="pic2" src="(.*?)"'
imgs=re.findall(p,html)
for x in imgs:
    'http://qq.yh31.com'+x)