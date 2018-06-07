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

Let's have another look at it:

```html
<article class="set">
  <a class="highslide plain mainimg" href="http://images.brickset.com/sets/images/10251-1.jpg?201510121127" onclick="return hs.expand(this)">
    <img src="http://images.brickset.com/sets/small/10251-1.jpg?201510121127" title="10251-1: Brick Bank"></a>
  ...
  <div class="meta">
    <h1><a href="/sets/10251-1/Brick-Bank"><span>10251:</span> Brick Bank</a> </h1>
    ...
    <div class="col">
      <dl>
        <dt>Pieces</dt>
        <dd><a class="plain" href="/inventories/10251-1">2380</a></dd>
        <dt>Minifigs</dt>
        <dd><a class="plain" href="/minifigs/inset-10251-1">5</a></dd>
        ...
      </dl>
    </div>
    ...
  </div>
</article>
```

- The image for the set is stored in the `src` attribute of an `img` tag inside an `a`.
- Getting the number of pieces is trickier: there is a `dt` tag that contains the text `Pieces`, and then a `dd` tag that follows it which contains the actual number of pieces.
- Getting the number of minigifs is similar to the number of pieces. There is a `dt` tag that contains the text `Minifigs`, followed by a `dd` tag after that with the number.

Once you have modified the scraper, run it again:

```scrapy runspider scraper.py```

The output will be a collection of something like this:

```python
{'minifigs': '5', 'pieces': '2380', 'name': 'Brick Bank', 'image': 'http://images.brickset.com/sets/small/10251-1.jpg?201510121127'}
```

## Step 3 - Crawling Multiple pages

Extracting data from the intial page is done, but we're not progressing past it to see the rest. The whole point of a spider is to detect and traverse links to other pages and grab data from those too.

You'll notice that the top and bottom of each page has a little right carat `>` that links to the next page.

```html
<div class='pagelength'>
  ...
  <li class='next'>
  <a href="https://brickset.com/sets/year-2016/page-2">›</a>
  </li>
  ...
</div>
```

There is, as you can see, a `li` tag with class 'next', and inside that tag, there is an `a` tag with a link to the next page.

Once the next page selector is defined, if you run the spider again you'll see that it doesn't just stop once it iterates through the first page of sets, but keeps going through all 23 pages.
