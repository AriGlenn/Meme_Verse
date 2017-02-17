import scrapy, csv


class QuotesSpider(scrapy.Spider):
    name = "memes"
    start_urls = [
        'http://imgur.com/t/memes/',
    ]

    def parse(self, response):

        homes = response.css("div.post")
        memeURL_Extensions = []
        x = 0
        for home in homes:
            homes1 = homes[x]
            postS_urlS_extensionS = homes1.css('a.image-list-link::attr(href)').extract()
            x += 1
            z = 0
            for linkExtensions in postS_urlS_extensionS:
                linkExtensions1 = 'http://imgur.com' + str(postS_urlS_extensionS[0])
                memeURL_Extensions.append(linkExtensions1)
                print(linkExtensions1)

        with open('meme_post_URLs.csv', 'w') as out:
            writer = csv.writer(out)
            for memes in memeURL_Extensions:
                writer.writerow(memes.split(","))
