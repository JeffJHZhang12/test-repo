import time

import requests
from bs4 import BeautifulSoup

import dbhelper


def getdata(url):
    hds = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27",
    }
    try:
        r = requests.get(url, headers=hds)
        r.raise_for_status()
        data = r.json()
        title = data["data"]["trackInfo"]["title"]
        title = title.strip()[:7]
        details = data["data"]["trackInfo"]["richIntro"]
        soup = BeautifulSoup(details, features="html.parser")
        pitems = soup.select("p")
        ret = []
        for item in pitems:
            s = item.getText()
            s = s.replace("  ", " ")
            ret.append((title, s))

    except Exception as e:
        print("url:{}, error:{}".format(url, e))
        return None
    else:
        return ret


if __name__ == "__main__":
    sql = "select cast([index] as int) as chid, substr(title,1,7) as title, substr(url,8) as url from lesson_raw order by chid limit 1000 offset 50"

    rows = dbhelper.getdata(sql)
    url = "https://www.ximalaya.com/revision/track/simple?trackId={}"
    for r in rows:
        print(r)
        data = getdata(url.format(r[2]))
        sql = "Insert into lesson_detail values (?,?)"
        dbhelper.insertdata(sql, data)
        time.sleep(2)
