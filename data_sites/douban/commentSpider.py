import re
import time
import random
import urllib3
import requests
import socket

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# 主入口
if __name__ == '__main__':
    proxies_list = get_ip()
    can_use_ip_list = check_ip(proxies_list)
    page = 200
    for i in range(1, page + 1):
        time.sleep(random.randint(1, 3))
        print('小爬虫在爬取第%s页' % i)
        url = 'https://movie.douban.com/subject/35422807/comments?percent_type=&start=%s&limit=20&status=P&sort=new_score&comments_only=1' % ((i - 1) * 20)
        print(url)
        tree = get_tree(url, can_use_ip_list)
        info_list = parse(tree)
        print('保存中....')
        save(info_list, i)

# 数据源获取
def parse(tree):
    global comment_set
    info_list = []
    comment_list = tree.xpath(
        '//div[@id="comments"]/div[@class="comment-item "]')
    for com in comment_list:
        comments_user = com.xpath(
            './div[@class="comment"]/h3/span[@class="comment-info"]/a/text()')[
                0]  # 评论者
        if comments_user in comment_set:
            pass
        else:
            stat_dict = {
                "10": "一星",
                "20": "二星",
                "30": "三星",
                "40": "四星",
                "50": "五星",
            }
            comment_star = com.xpath(
                './div[@class="comment"]/h3/span[@class="comment-info"]/span[2]/@class'
            )[0]  # 星级
            for i in stat_dict:
                if i in comment_star:
                    comment_star = stat_dict[i]
            try:
                comment_time = com.xpath(
                    './div[@class="comment"]/h3/span[@class="comment-info"]/span[3]/text()'
                )[0].split()[0]  # 评论时间
            except:
                comment_time = ""
            comment = com.xpath(
                './div[@class="comment"]/p[@class=" comment-content"]/span/text()'
            )[0]  # 评论
            comment_set.add(comments_user)
            info_list.append(
                [comments_user, comment_star, comment_time, comment])
    return info_list

# 文件存储
def save(item, title=None):
    # 创建文件对象
    try:
        if title == 1:
            content_list = ['评论者', '评论星级', '评论时间', '评论内容']
            with open('./扬名立万.csv', 'a+', newline='',
                        encoding='utf-8-sig') as file:
                writer = csv.writer(file, delimiter=',')
                writer.writerow(content_list)
                writer.writerows(item)
        if title == 1:
            print('>>>创建表格成功，并加入标题成功！')
        else:
            print('>>>写入成功！')
    except:
        pass

def get_ip():
    """
    查询本机ip地址
    :return:
    """
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip=s.getsockname()[0]
    finally:
        s.close()

    return ip
