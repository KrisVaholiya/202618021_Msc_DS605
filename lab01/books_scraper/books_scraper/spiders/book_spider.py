import scrapy


class BookSpiderSpider(scrapy.Spider):
    name = "books"

    allowed_domains = ["books.toscrape.com"]

    start_urls = [
        "https://books.toscrape.com/catalogue/page-1.html"
    ]

    def parse(self, response):

        books = response.css("article.product_pod")

        for book in books:

            book_url = response.urljoin(
                book.css("h3 a::attr(href)").get()
            )

            yield scrapy.Request(
                book_url,
                callback=self.parse_book
            )

        next_page = response.css("li.next a::attr(href)").get()

        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_book(self, response):

        table = response.css("table tr")

        description = response.css(
            "#product_description + p::text"
        ).get()

        breadcrumb = response.css(
            "ul.breadcrumb li a::text"
        ).getall()

        rating = response.css(
            "p.star-rating::attr(class)"
        ).get().split()[-1]

        yield {

            "title": response.css(
                "div.product_main h1::text"
            ).get(),

            "category": breadcrumb[2],

            "price": response.css(
                "p.price_color::text"
            ).get(),

            "rating": rating,

            "availability": response.css(
                "p.instock.availability::text"
            ).getall()[-1].strip(),

            "description": description,

            "upc": table[0].css("td::text").get(),

            "reviews": table[6].css("td::text").get(),

            "product_url": response.url,
        }