import scrapy
import logging
from playerstats.items import PlayerItem, StatsItem, ConditionsStatsItems


class PlayerStastsScraper(scrapy.Spider):
    """Scraper for accessing the BrickSet."""

    name = 'laliga_scraper'
    start_urls = ['http://www.laliga.es/en/laliga-santander/real-madrid']
    download_delay = 2

    def parse(self, response):
        """Parse the web start_urls."""

        POSITION_SELECTOR = '.posiciones-equipo'
        POSITION_NAME_SELECTOR = '.titulo_posicion ::text'
        PLAYER_SELECTOR = '.posiciones .box-jugador'
        PLAYER_NAME_SELECTOR = '.nombre-perfil ::text'
        STATS_PAGE_SELECTOR = '::attr(href)'

        for position in response.css(POSITION_SELECTOR)[1:]:
            player_items = PlayerItem()

            player_items['position'] = position.css(
                POSITION_NAME_SELECTOR).extract_first()

            for player in position.css(PLAYER_SELECTOR):

                player_items['name'] = player.css(
                    PLAYER_NAME_SELECTOR).extract_first()

                stats_page = player.css(STATS_PAGE_SELECTOR).extract_first()
                if stats_page:
                    yield scrapy.Request(
                        stats_page,
                        callback=self.parse_stats,
                        meta={'item': player_items})

    def parse_stats(self, response):
        """Parse specific stats page for each player"""
        # http://laliga.es/en/player/keylor-navas
        player_items = response.meta['item']
        logging.info(player_items)

        player_stats = {}
        stats_keys = [
            'minutes',
            'games_played',
            'games_played_pc',
            'games_played_full',
            'games_played_full_pc',
            'games_started',
            'games_started_pc',
            'games_where_substituted',
            'games_where_subsituted_pc',
            'cards_yellow',
            'cards_red',
            'cards_doubleyellow',
            'goals_scored',
            'goals_scored_penalty',
            'goals_owngoals',
            'goals_conceded',
        ]

        a_selector_css = '.estadisticas-jugador-1'
        b_selector_xpath_0 = '//section[@id="box-estadisticas-jugador"]'  # take element 0 of this
        c_selector_css_1 = 'div'  # take element 1 of this
        d_selector_xpath = '//table[@class="datatable"]/tbody/tr'  # for item in d
        e_selector_xpath = 'td/text()'

        try:
                a = response.css(a_selector_css)
                b = a.xpath(b_selector_xpath_0)
                c = b[0].css(c_selector_css_1)
                d = c[1].xpath(d_selector_xpath)
        except Exception:
                return player_items

        stats_values_by_condition = []
        for item in d:
            e = item.xpath(e_selector_xpath).extract()
            stats_values_by_condition.append(e)

        for condition in stats_values_by_condition:
                if condition[0] == u'2017/2018':
                        condition[0] = 'Season'

                player_stats_in_condition = dict(zip(stats_keys, condition[1:]))
                player_stats[condition[0]] = player_stats_in_condition

        player_items['stats'] = player_stats

        return player_items
