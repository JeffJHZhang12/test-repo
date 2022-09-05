import requests
from bs4 import BeautifulSoup


def getdata(url):
    hds = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27",
    }
    try:
        r = requests.get(url, headers=hds)
        r.raise_for_status()
        data = r.json()
        title = data["data"]["trackInfo"]["title"]
        details = data["data"]["trackInfo"]["richIntro"]
        soup = BeautifulSoup(details, features="html.parser")
        pitems = soup.select("p")
        for item in pitems:
            print(item.getText())

    except Exception as e:
        print(e)


if __name__ == "__main__":
    url = "https://www.ximalaya.com/revision/track/simple?trackId=452803861"
    getdata(url)
