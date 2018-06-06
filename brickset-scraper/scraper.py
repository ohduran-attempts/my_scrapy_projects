import scrapy


class BrickSetSpider(scrapy.Spider):
    """Scraper for accessing the BrickSet."""
    name = 'brickset_spider'
    start_urls = ['http://brickset.com/sets/year-2016']

    def parse(self, response):
        # Since we are looking for a class, we will use '.set' in the selector.
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):
            # The brickset object has its own css method,
            # so we can pass in a selector to locate child elements.
            NAME_SELECTOR = 'h1 a ::text'  # append ::text to fetch text inside of the a tag
            yield {
                'name': brickset,css(NAME_SELECTOR).extract_first(),
            }
