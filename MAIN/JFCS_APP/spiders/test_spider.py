
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "test"
    start_urls = [
        'http://imgur.com/t/memes/ArsHb',
    ]
    def parse(self, response):

        images = response.css("div.post-image")
        print(type(images))
        x = 0
        for image in images:
            images1 = images[x]
            yield {
                'image_url' : images1.css('img').extract()
                }
            x += 1
