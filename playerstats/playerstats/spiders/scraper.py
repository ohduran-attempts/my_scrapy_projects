import scrapy


class PlayerStastsScraper(scrapy.Spider):
    """Scraper for accessing the BrickSet."""

    name = 'laliga_scraper'
    start_urls = ['http://www.laliga.es/en/laliga-santander/real-madrid']

    def parse(self, response):
        """Parse the web start_urls."""
        # Since we are looking for a class, we will use '.set' in the selector.
        POSITION_SELECTOR = '.posiciones-equipo .posiciones'

        for position in response.css(POSITION_SELECTOR):
            NAME_SELECTOR = '.nombre-perfil ::text'
            yield {
                'player_name': position.css(NAME_SELECTOR).extract_first(),
            }


#/html/body/div[2]/section[2]/div/section/div[2]/div[2]/div[2]/a[1]/div[2]
        # NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        # next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        # if next_page:
        #     yield scrapy.Request(
        #         response.urljoin(next_page),
        #         callback=self.parse  # recursively call self parse until next_page is None
        #     )
