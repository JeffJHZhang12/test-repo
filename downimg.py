"""
download math book A for class 6
"""

import os
import requests


def down(url, fd):
    try:
        r = requests.get(url)
        r.raise_for_status()
        _, filename = os.path.split(url)
        filename, _ = filename.split("?")
        filename = os.path.join(fd, filename)
        with open(filename, "wb") as fh:
            for chunk in r.iter_content(100000):
                fh.write(chunk)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    url = (
        r"https://download.pep.com.cn/xsxjc/22xjcsx61x/files/mobile/{}.jpg?220822003628"
    )
    downfolder = r"/Users/jeffjhzhang/Downloads/book6a"
    for i in range(1, 127):  # 127
        s = url.format(i)
        down(s, downfolder)
