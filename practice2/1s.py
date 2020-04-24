import requests
from bs4 import BeautifulSoup
import urllib
import xlwt
import json


class JdDownloadProduct:
    def __init__(self):
        pass

    def download(self, keyword):
        url = f"https://search.jd.com/Search?keyword={keyword}&enc=utf-8"
        html = self.fetchHtml(url)
        dates = self.parseHtml(html)
        self.writeFile(dates)
        return

    def fetchHtml(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
        }
        req = requests.get(url, headers=headers)
        req.encoding = req.apparent_encoding  # 为了避免乱码
        return req.text

    def parseHtml(self, html):
        bf = BeautifulSoup(html, "lxml")
        titles = bf.find_all(class_="p-name p-name-type-2")
        prices = bf.find_all(class_="p-price")
        comments = bf.find_all(class_="p-commit")
        shops = bf.find_all(class_="curr-shop hd-shopname")
        imgs = bf.find_all(class_="p-img")
        datas = []
        for title, price, comment, shop, img in zip(titles, prices, comments, shops, imgs):
            datas.append({
                "title": title.text.strip(),
                "price": price.text.strip(),
                "comments": comment.text.strip(),
                "shop": shop.text.strip(),
                "link": title.find_all("a")[0].get("href"),
                "img": img.find_all("a")[0].find("img").get("source-data-lazy-img"),
            })
        return datas

    def writeFile(self, dates):
        w = xlwt.Workbook()
        sheet1 = w.add_sheet("商品列表", cell_overwrite_ok=True)
        row0 = ["商品名称", "商品价格", "商品图片", "店铺", "商品详情链接"]
        for i in range(0, len(row0)):
            sheet1.write(0, i, row0[i])
        for i, item in enumerate(dates):
            rownum = i + 1
            sheet1.write(rownum, 0, item["title"])
            sheet1.write(rownum, 1, item["price"])
            sheet1.write(rownum, 2, item["img"])
            sheet1.write(rownum, 3, item["shop"])
            sheet1.write(rownum, 4, item["link"])
        w.save("./practice2/jd-product.xls")


if __name__ == "__main__":
    keyword = input("请输入要搜索的内容：")
    jd = JdDownloadProduct()
    jd.download(keyword)
