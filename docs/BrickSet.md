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

The HTML for each article looks more or less like this:

```html
<body>
  <section class="setlist">
    <article class='set'>
      <a class="highslide plain mainimg" href=
      "http://images.brickset.com/sets/images/10251-1.jpg?201510121127"
      onclick="return hs.expand(this)"><img src=
      "http://images.brickset.com/sets/small/10251-1.jpg?201510121127"
      title="10251-1: Brick Bank"></a>
      <div class="highslide-caption">
        <h1><a href='/sets/10251-1/Brick-Bank'>Brick Bank</a></h1>
        <div class='tags floatleft'>
          <a href='/sets/10251-1/Brick-Bank'>10251-1</a> <a href=
          '/sets/theme-Advanced-Models'>Advanced Models</a> <a class=
          'subtheme' href=
          '/sets/theme-Advanced-Models/subtheme-Modular-Buildings'>Modular
          Buildings</a> <a class='year' href=
          '/sets/theme-Advanced-Models/year-2016'>2016</a>
        </div>
        <div class='floatright'>
          &copy;2016 LEGO Group
        </div>
        <div class="pn">
          <a href="#" onclick="return hs.previous(this)" title=
          "Previous (left arrow key)">&#171; Previous</a> <a href="#"
          onclick="return hs.next(this)" title=
          "Next (right arrow key)">Next &#187;</a>
        </div>
      </div>
      ...
    </article>
    <article class='set'>

      ...

    </article>
</section>
</body>
```

Scraping this page is a two step process:
1. Grab each LEGO set by looking for the parts of the page that have the data we want.
2. For each set, grab the data we want from it by pulling the data out of the HTML tags.

Scrapy grabs data based on selectors that you provide, patterns we can use to find one or more elements on a page so that we can work with the data within the element. We'll use CSS selectors for now.

Since we are looking for a class, we will use '.set' in the selector. Another look at the source tells us that the name of each set is stored within an a tag inside an h1 tag for each set.

```html
<div class='highslide-caption'><h1>Brick Bank</h1></div>
```

The brickset object has its own css method, so we can pass in a selector to locate child elements.
