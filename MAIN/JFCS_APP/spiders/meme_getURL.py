import scrapy, csv


class QuotesSpider(scrapy.Spider):
    name = "memes"
    start_urls = ['http://imgur.com/t/memes/',]


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
                yield scrapy.Request(linkExtensions1, self.parse_results)


    def parse_results(self, response):
        print("\n\n\n\n\n\n\n\n\n" + "URL: " + response.url)

        ffff = response.css("div.post-image")
        ff = ffff.css('a.zoom::attr(href)').extract()


        print(ff)
