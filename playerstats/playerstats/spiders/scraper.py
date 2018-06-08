import scrapy


class PlayerStastsScraper(scrapy.Spider):
    """Scraper for accessing the BrickSet."""

    name = 'laliga_scraper'
    start_urls = ['http://www.laliga.es/en/laliga-santander/real-madrid']

    def parse(self, response):
        """Parse the web start_urls."""
        items = {}
        # Since we are looking for a class, we will use '.set' in the selector.
        POSITION_SELECTOR = '.posiciones-equipo'

        for position in response.css(POSITION_SELECTOR)[1:]:
            POSITION_NAME_SELECTOR = '.titulo_posicion ::text'

            items['position'] = position.css(
                POSITION_NAME_SELECTOR).extract_first()

            PLAYER_SELECTOR = '.posiciones .box-jugador'

            for player in position.css(PLAYER_SELECTOR):
                PLAYER_NAME_SELECTOR = '.nombre-perfil ::text'
                items['player_name'] = position.css(
                    PLAYER_NAME_SELECTOR).extract_first()

                # REMOVE NONE VALUES
                yield items

            # REMOVE NONE VALUES
