import requests
from bs4 import BeautifulSoup
import json
from contextlib import closing


class BdDownloadImage:
    def __init__(self):
        self.url = ""
        pass

    def download(self):
        urls = self.fetchUrls()
        for i, v in enumerate(urls):
            print("正在下载第{}张图片...".format(i+1))
            self.writeImage(v, i+1)

    def fetchUrls(self):
        requests.packages.urllib3.disable_warnings()
        req = requests.get(url=self.url, verify=False)
        jDict = json.loads(req.text)
        data = jDict["data"]
        urls = []
        for item in data:
            if "hoverURL" in item:
                urls.append(item["hoverURL"])
        return urls

    def writeImage(self, url, filename):
        with closing(requests.get(url, verify=False)) as r:
            with open("./practice2/imgs/{}.jpg".format(filename), "ab+") as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()


if __name__ == "__main__":
    bd = BdDownloadImage()
    bd.url = "https://image.baidu.com/search/acjson?tn=resultjson_com&catename=pcindexhot&ipn=rj&ct=201326592&is=&fp=result&queryWord=&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=pcindexhot&face=0&istype=2&qc=&nc=1&fr=&pn=0&rn=30"
    bd.download()
