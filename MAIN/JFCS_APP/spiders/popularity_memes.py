
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "memes"
    start_urls = [
        'http://imgur.com/t/memes/',
    ]

    def parse(self, response):

        homes = response.css("div.post")

        x = 0
        for home in homes:
            homes1 = homes[x]
            postS_urlS_extensionS = homes1.css('a.image-list-link::attr(href)').extract()
            x += 1

            z = 0
            for linkExtensions in postS_urlS_extensionS:
                linkExtensions1 = postS_urlS_extensionS[z]
                print(linkExtensions1)
