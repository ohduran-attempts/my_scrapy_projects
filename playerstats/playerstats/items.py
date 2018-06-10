# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PlayerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    position = scrapy.Field()
    stats = scrapy.Field()


class ConditionsStatsItems(scrapy.Item):
    Home = scrapy.Field()
    Draws = scrapy.Field()
    Defeats = scrapy.Field()
    Away = scrapy.Field()
    Season = scrapy.Field()
    Wins = scrapy.Field()


class StatsItem(scrapy.Item):
    minutes = scrapy.Field()
    games_played = scrapy.Field()
    games_played_pc = scrapy.Field()
    games_played_full = scrapy.Field()
    games_played_full_pc = scrapy.Field()
    games_started = scrapy.Field()
    games_started_pc = scrapy.Field()
    games_where_subsituted = scrapy.Field()
    games_where_subsituted_pc = scrapy.Field()
    cards_yellow = scrapy.Field()
    cards_red = scrapy.Field()
    cards_doubleyellow = scrapy.Field()
    goals_scored = scrapy.Field()
    goals_scored_penalty = scrapy.Field()
    goals_owngoals = scrapy.Field()
    goals_conceded = scrapy.Field()
