import scrapy


class PlayerStastsScraper(scrapy.Spider):
    """Scraper for accessing the BrickSet."""

    name = 'laliga_scraper'
    start_urls = ['http://www.laliga.es/en/laliga-santander/real-madrid']

    def parse(self, response):
        """Parse the web start_urls."""
        player_items = {}

        POSITION_SELECTOR = '.posiciones-equipo'
        for position in response.css(POSITION_SELECTOR)[1:]:

            POSITION_NAME_SELECTOR = '.titulo_posicion ::text'
            player_items['position'] = position.css(
                POSITION_NAME_SELECTOR).extract_first()

            PLAYER_SELECTOR = '.posiciones .box-jugador'
            for player in position.css(PLAYER_SELECTOR):

                PLAYER_NAME_SELECTOR = '.nombre-perfil ::text'
                player_items['player_name'] = player.css(
                    PLAYER_NAME_SELECTOR).extract_first()

                STATS_PAGE_SELECTOR = '::attr(href)'
                stats_page = response.css(STATS_PAGE_SELECTOR).extract_first()
                if stats_page:
                    player_stats = scrapy.Request(
                        response.urljoin(stats_page),
                        callback=self.parse_stats)
                    player_items['stats'] = player_stats

                yield player_items

    def parse_stats(self, response):
        """Parse specific stats page for each player"""
        # http://laliga.es/en/player/keylor-navas
        player_stats = {}
        stats = [
            'min',
            'games played',
            'PC games played',
            'full games played',
            'PC full games played'
        ]

        a_selector_css = '.estadisticas-jugador-1'
        b_selector_xpath_0 = '//section[@id="box-estadisticas-jugador"]'  #take element 0 of this
        c_selector_css_1 = 'div'  # take element 1 of this
        d_selector_xpath = '//table[@class="datatable"]/tbody/tr'  # for item in d
        e_selector_xpath = 'td/text()'
