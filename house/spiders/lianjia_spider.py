import scrapy

class LianjiaSpider (scrapy.Spider):
    name = "lianjia"
    allowed_domains = ["lianjia.com"]
    start_urls = [
        "http://bj.lianjia.com/ershoufang"
        # "http://bj.lianjia.com/ershoufang/101100840849.html"
    ]

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            title = sel.xpath('div/div/a/text()').extract()
            print title
