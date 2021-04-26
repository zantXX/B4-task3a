import os
os.environ["http_proxy"] = "http://proxy.uec.ac.jp:8080/"
os.environ["https_proxy"] = "http://proxy.uec.ac.jp:8080/"

from icrawler.builtin import GoogleImageCrawler
crawler = GoogleImageCrawler(storage={"root_dir":"img/pasta"},downloader_threads=5)
crawler.crawl(keyword="pasta", max_num=100)