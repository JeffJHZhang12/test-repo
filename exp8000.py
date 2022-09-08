import requests
import dbhelper


def getdata(url):
    hds = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27",
    }
    try:
        ret = []
        r = requests.get(url, headers=hds)
        r.raise_for_status()
        data = r.json()
        for track in data["data"]["tracks"]:
            # print(
            #     "Index: {}, title: {}, url: {}".format(
            #         track["index"], track["title"], track["url"]
            #     )
            ret.append((track["index"], track["title"], track["url"]))

    except Exception as e:
        print(e)
        return None
    else:
        return ret


if __name__ == "__main__":
    url = "https://www.ximalaya.com/revision/album/v1/getTracksList?albumId=52236920&pageNum={}&sort=0"

    for i in range(1, 13):
        data = getdata(url.format(i))
        sql = "Insert into lesson_raw values (?,?,?)"
        dbhelper.insertdata(sql, data)
