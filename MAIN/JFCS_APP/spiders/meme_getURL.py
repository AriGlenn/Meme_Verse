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
                yield scrapy.Request(linkExtensions1, self.parse_results)

    def parse_results(self, response):
        memeIMG_URLs = []
        print("\n\n\n\n\n\n\n\n\n" + "URL: " + response.url)
        main = response.css("div.post-image")
        href = main.css('a.zoom::attr(href)').extract()
        if href:
            print('The img url is in the href')
            for x in href:
                print(x)
                link = "https:" + x
                memeIMG_URLs.append(link)
        else:
            gif1 = response.css("div.video-container source::attr(src)").extract()

            if gif1:
                print('The img url is a movie/gif')
                for x in gif1:
                    gif_link = "https:" + x
                    print(gif_link)
                    memeIMG_URLs.append(gif_link)

            else:
                print('The img url is in the img src')
                imgSrc = main.xpath('//img/@src').extract_first()
                imgSrc = "https:" + imgSrc
                print(imgSrc)
                memeIMG_URLs.append(imgSrc)



        with open('meme_img_URLs.csv', 'a') as out:
            writer = csv.writer(out)
            for links in memeIMG_URLs:
                writer.writerow(links.split(","))
