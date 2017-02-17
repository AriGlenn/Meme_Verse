import scrapy, csv


class QuotesSpider(scrapy.Spider):
    name = "memes_ext"
    start_urls = [
        #Make list from csv file

        'http://imgur.com/t/memes/',
    ]

    def parse(self, response):

        homes = response.css("div.post")
        memeURL_IMGs = []
        x = 0
        for home in homes:
            homes1 = homes[x]
            postS_urlS_extensionS = homes1.css('a.image-list-link::attr(href)').extract()
            x += 1







        with open('meme_img_URLs.csv', 'w') as out:
            writer = csv.writer(out)
            for imgs in memeURL_IMGs:
                writer.writerow(memes.split(","))
