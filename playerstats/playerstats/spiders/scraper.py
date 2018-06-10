import scrapy
from playerstats.items import PlayerItem


class PlayerStastsScraper(scrapy.Spider):
    """Scraper for accessing the BrickSet."""

    name = 'laliga_scraper'
    start_urls = ['http://www.laliga.es/en/laliga-santander/real-madrid']

    def parse(self, response):
        """Parse the web start_urls."""
        player_items = PlayerItem()

        POSITION_SELECTOR = '.posiciones-equipo'
        for position in response.css(POSITION_SELECTOR)[1:]:

            POSITION_NAME_SELECTOR = '.titulo_posicion ::text'
            player_items['position'] = position.css(
                POSITION_NAME_SELECTOR).extract_first()

            PLAYER_SELECTOR = '.posiciones .box-jugador'
            for player in position.css(PLAYER_SELECTOR):

                PLAYER_NAME_SELECTOR = '.nombre-perfil ::text'
                player_items['name'] = player.css(
                    PLAYER_NAME_SELECTOR).extract_first()

                # STATS_PAGE_SELECTOR = '::attr(href)'
                # stats_page = player.css(STATS_PAGE_SELECTOR).extract_first()
                # if stats_page:
                #     stats = scrapy.Request(
                #         stats_page,
                #         callback=self.parse_stats)
                #
                # player_items['stats'] = stats
                yield player_items

    def parse_stats(self, response):
        """Parse specific stats page for each player"""
        # http://laliga.es/en/player/keylor-navas
        player_stats = {}
        stats_keys = [
            'min',
            'games played',
            'PC games played',
            'full games played',
            'PC full games played',
            'games started',
            'PC games started',
            'games where substituted',
            'PC games where substituted',
            'yellow cards',
            'red cards',
            '2 yellow cards',
            'goals scored',
            'penalties scored',
            'own goals',
            'goals conceded',
        ]

        a_selector_css = '.estadisticas-jugador-1'
        b_selector_xpath_0 = '//section[@id="box-estadisticas-jugador"]'  #take element 0 of this
        c_selector_css_1 = 'div'  # take element 1 of this
        d_selector_xpath = '//table[@class="datatable"]/tbody/tr'  # for item in d
        e_selector_xpath = 'td/text()'

        a = response.css(a_selector_css)
        b = a.xpath(b_selector_xpath_0)
        c = b[0].css(c_selector_css_1)
        d = c[1].xpath(d_selector_xpath)

        stats_values_by_condition = []
        for item in d:
            e = item.xpath('td/text()').extract()
            stats_values_by_condition.append(e)

        for condition in stats_values_by_condition:
                    player_stats_in_condition = dict(zip(stats_keys, condition[1:]))
                    player_stats[condition[0]] = player_stats_in_condition

        return player_stats
