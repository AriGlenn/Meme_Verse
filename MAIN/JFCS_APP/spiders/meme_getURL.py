import scrapy, csv, time
import sqlite3 as lite

con = lite.connect('test43.db')
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS MemesTest")
cur.execute("CREATE TABLE MemesTest (ID INT, Name TEXT, DatePosted TEXT, URL TEXT);")
con.commit()

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
                time.sleep(0)
                yield scrapy.Request(linkExtensions1, self.parse_results)

    def parse_results(self, response):
        memeIMG_URLs = []
        print("URL: " + response.url)
        main = response.css("div.post-image")
        href = main.css('a.zoom::attr(href)').extract()

        mainLink = ''

        if href:
            for x in href:
                link = "https:" + x
                mainLink = link
                memeIMG_URLs.append(link)
        else:
            gif1 = response.css("div.video-container source::attr(src)").extract()
            if gif1:
                for x in gif1:
                    gif_link = "https:" + x
                    mainLink = gif_link
                    memeIMG_URLs.append(gif_link)
            else:
                imgSrc = main.xpath('//img/@src').extract_first()
                imgSrc = "https:" + imgSrc
                mainLink = imgSrc
                memeIMG_URLs.append(imgSrc)

        nameHome = response.css("div.post-title-container")
        name = nameHome.xpath('//h1/text()').extract_first()
        memeIMG_URLs.append(name)

        if name == '':
            name = 'None'
            memeIMG_URLs.append(name)


        DatePosted = response.css("span.date::text").extract_first()
        memeIMG_URLs.append(DatePosted)


        Views = response.css("div span.post-action-stats-points")




        with open('meme_img_URLs.csv', 'a') as out:
            writer = csv.writer(out)
            for links in memeIMG_URLs:
                writer.writerow(links.split(","))

        x = 0
        print(x)
        con = lite.connect('test43.db')
        cur = con.cursor()
        cur.execute("INSERT INTO MemesTest VALUES (?, ?, ?, ?);", (x, name, DatePosted, mainLink))
        con.commit()
        x += 1
        cursor = con.execute("SELECT ID, Name, DatePosted, URL  from MemesTest")
        for row in cursor:
           print("ID = ", row[0])
           print("Name = ", row[1])
           print("DatePosted = ", row[2])
           print("URL = ", row[3], "\n")
        con.close()
