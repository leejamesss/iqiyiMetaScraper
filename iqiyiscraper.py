import requests
from bs4 import BeautifulSoup

url = "https://www.iqiyi.com/v_xkt6z3z798.html"

# 发送HTTP请求并获取页面内容
response = requests.get(url)
html_content = response.text

# 使用BeautifulSoup库解析HTML文档
soup = BeautifulSoup(html_content, 'html.parser')

# 查找所有meta标签，并输出其属性名
print("meta标签的属性名：")
meta_tags = soup.find_all("meta")
for tag in meta_tags:
        print(tag.get("name") or tag.get("property") or tag.get("httpequiv")  or tag.get("itemprop"))

