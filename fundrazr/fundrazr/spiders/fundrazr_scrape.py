import scrapy
from fundrazr.items import FundrazrItem
from datetime import datetime
import re


class Fundrazr(scrapy.Spider):
    name = "my_scraper"

    # First Start url
    start_urls = ["https://fundrazr.com/find?category=Health"]

    npages = 2

    # This mimics getting the pages using the next button
    for i in range(2, npages + 2):
        start_urls.append("https://fundrazr.com/find?category=Health&page="+str(i)+"")

    def parse(self, response):
        for href in response.xpath("//h2[contains(@class, 'title headline-font')]/a[contains(@class, 'campaign-link')]//@href"):
            # add the scheme
            url = "https:" + href.extract()
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        item = FundrazrItem()

        item['campaignTitle'] = response.xpath("//div[contains(@id, 'campaign-title')]/descendant::text()").extract_first().strip()
