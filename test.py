# # from bs4 import BeautifulSoup

# # soup = BeautifulSoup("<p>hello</p>", "lxml")
# # print(soup.p.string)
# from bs4 import BeautifulSoup
# from bs4.element import Tag

# HTML = """
# <html><head><title>The Dormouse's story</title></head>
# <body >
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story''>Once upon a time there were three little sisters; and their names were <a href="http://example.com/elsie" class="sister" id="linkl"><! - Elsie ...></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a> ;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """

# soup = BeautifulSoup(HTML, "lxml")
# # print(soup.prettify())
# print(soup.title)
# print(type(soup.title))
from pyquery import PyQuery as pq

html = """
<div class='wrap'>
<div id ='container'>
<ul class = 'list'>
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="old">third item</span></a></li> 
<li class =" item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="links .html">fifth item</a></li> </ul>
</div>
</div>
"""

doc = pq(html)
items = doc(".list")
# parents = items.parents()
# print(type(parents))
print(items.text())
