import re
import time
import random
import urllib3
import requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 爬取一页评论内容
def get_one_page(url):
    headers = {
        'User-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'Host' : 'weibo.cn',
        'Accept' : 'application/json, text/plain, */*',
        'Accept-Language' : 'zh-CN,zh;q=0.9',
        'Accept-Encoding' : 'gzip, deflate, br',
        'Cookie' : 'SUB=_2A25MupFEDeRhGeBO6VQR9y_Nyz6IHXVsRD8MrDV6PUNbktCOLUqskW1NSguy7gQycV1xO8TdlRv4lP8FsRA8b1_0; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhEAVD3K2Xz0RkKlJqEAJ8W5JpX5KzhUgL.Foq7eoq7S02pehz2dJLoIEBLxKqLBozLBKMLxKqLBo-LBoMLxKBLBonL12-LxKBLB.BLBK5t; SSOLoginState=1639899413; ALF=1642491413; _T_WM=99742468946; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D20000174',
        'DNT' : '1',
        'Connection' : 'keep-alive'
    }
    # 获取网页 html
    response = requests.get(url, headers = headers, verify=False)
    # 爬取成功
    if response.status_code == 200:
        # 返回值为 html 文档，传入到解析函数当中
        return response.text
    return None

# 解析保存评论信息
def save_one_page(html):
    comments = re.findall('<span class="ctt">(.*?)</span>', html)
    for comment in comments[1:]:
        result = re.sub('<.*?>', '', comment)
        if '回复@' not in result:
            with open('comments.txt', 'a+', encoding='utf-8') as fp:
                fp.write(result)

for i in range(1000):
    url = 'https://weibo.cn/comment/L6w2sfDXb?uid=5977512966&rl=0&page='+str(i)
    html = get_one_page(url)
    print('正在爬取第 %d 页评论' % (i+1))
    save_one_page(html)
    time.sleep(random.randint(0,5))