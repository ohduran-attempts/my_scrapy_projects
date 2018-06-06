# BrickSet

In this tutorial, we'll use [BrickSet](https://brickset.com/), a community-run site that contains information about LEGO sets.


## Step 1 - Creating a Basic Scraper
Scraping is a two-step process:
1. Find and download web pages
2. Take those web pages and extract information from them.

Both of those steps can be implemented in many ways. You can build a scraper from scratch using modules or libraries provided, but then you have to deal with some potential headaches as your scraper grows in complexity.

In this case, we are using Scrapy, the most popular and powerful Python scraping libraries, one that handles a lot of the common functionality that all scrapers need so developers don't have to reinvent the wheel.

We'll start by making a very basic scraper that uses Scrapy as its foundation. To do that, we'll create a Python class that subclasses scrapy.Spider, a basic spider class provided by Scrapy. This class will have two required attributes:

- `name`
- `start_urls`

Once you have created the spider, it's time to run it:

`$ scrapy runspider scraper.py`


- The scraper initialized and loaded additional components and extensions it needed to handle reading data from URLs.
- It used the URL we provided in the start_urls list and grabbed the HTML, just like your web browser would do.
- It passed that HTML to the parse method, which doesn't do anything by default. Since we never wrote our own parse method, the spider just finishes without doing any work.

## Step 2 - Extracting Data from a Page
