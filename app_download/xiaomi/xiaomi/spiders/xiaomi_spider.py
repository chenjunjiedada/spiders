from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.statscollectors import StatsCollector
from xiaomi.items import AppItem

class XiaomiSpider(Spider):
    name = "xiaomi"
    allowed_domain = ["mi.com"]
    start_urls = ["http://app.mi.com/topList"]
    items = []
    app_num = 0
    page = 1

    def parse(self, response):
        self.crawler.stats.set_value('app_num', 0)
        return Request("http://app.mi.com/topList?page=%d" % self.page, callback=self.parse_apps, dont_filter=True);


    def parse_apps(self, response):
        apps = response.selector.xpath('//ul[@class="applist"]/li')
        count = 0
        for app in apps:
            rank = self.crawler.stats.get_value('app_num') + 1
            self.app_num = rank;
            self.logger.info("get app %d" % rank)
            item = AppItem()
            item['app_name'] = app.xpath('//h5/a/text()')[count].extract()
            item['down_link'] ="http://app.mi.com"+ app.xpath('//h5/a/@href')[count].extract()
            item['app_rank'] = rank;
            self.items.append(item)
            count += 1
            self.crawler.stats.inc_value('app_num');

        if (self.app_num < 200):
            self.page +=1
            return Request("http://app.mi.com/topList?page=%d" % self.page, callback=self.parse_apps, dont_filter=True);
        else:
            return self.items

    def parse_details(self, response):
        details = response.selector.xpath('//div[@class='details preventDefault']/ul/li')
        for detail in details


