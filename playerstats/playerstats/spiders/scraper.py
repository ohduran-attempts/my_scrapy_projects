import scrapy

class BrickSetSpider(scrapy.Spider):
    """Scraper for accessing the BrickSet."""
    name = 'laliga_scraper'
    start_urls = ['http://www.laliga.es/en/laliga-santander/real-madrid']

    def parse(self, response):
        # Since we are looking for a class, we will use '.set' in the selector.
        SET_SELECTOR = '.box-jugador'
        for player in response.css(SET_SELECTOR):
            # The brickset object has its own css method,
            # so we can pass in a selector to locate child elements.
            NAME_SELECTOR = '.nombre-perfil div ::text'  # append ::text to fetch text inside of the a tag

            yield {
                'name': player.css(NAME_SELECTOR).extract_first(),
            }

        # NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        # next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        # if next_page:
        #     yield scrapy.Request(
        #         response.urljoin(next_page),
        #         callback=self.parse  # recursively call self parse until next_page is None
        #     )
