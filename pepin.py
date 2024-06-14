import time

import requests
import feedparser


同事的名字 = ['yunyoujun']
上班时间 = 10
下班时间 = 18
回溯天数 = 7


def feed(人):
    for page in range(1, 8):
        r = requests.get(f'https://github.com/{人}.atom?page={page}')
        r.raise_for_status()
        feed = feedparser.parse(r.content)
        yield from feed.entries


现在 = time.time()

for 人 in 同事的名字:
    d = {}
    坏 = 0
    for i in feed(人):
        if (现在 - time.mktime(i['updated_parsed'])) / 86400 > 回溯天数:
            break
        hour = (i['updated_parsed'].tm_hour + 8) % 24   # 这个值好像没有GMT+8所有用手加1下
        d[hour] = d.get(hour, 0) + 1
        if hour < 上班时间 or hour >= 下班时间:
            坏 += 1
    print('-' * 40)
    print(人, f'坏: {坏}/{sum(d.values())}')
    m = max(d.values())
    for i in range(24):
        print(f'{i:2}点|' + '▇'*int(20 * d.get(i, 0) / m))
