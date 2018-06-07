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
            NAME_SELECTOR = 'div h1 ::text'  # append ::text to fetch text inside of the a tag

            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]//dd/a/text()'
            MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]//dd[2]/a/text()'
            IMAGE_SELECTOR = 'img ::attr(src)'
            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(),
                'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
                'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
                'image': brickset.css(IMAGE_SELECTOR).extract_first(),
            }

        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse  # recursively call self parse until next_page is None
            )
