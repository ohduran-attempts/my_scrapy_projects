import scrapy


class BrickSetSpider(scrapy.Spider):
    """Scraper for accessing the BrickSet."""
    name = 'brickset_spider'
    start_urls = ['http://brickset.com/sets/year-2016']
    
