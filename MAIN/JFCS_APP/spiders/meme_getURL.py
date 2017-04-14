import scrapy, pickle
import sqlite3 as lite

con = lite.connect('test47.db')
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS MemesTest1")
cur.execute("CREATE TABLE MemesTest1 (Name TEXT, DatePosted TEXT, URL TEXT, MAINURL TEXT);")
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
                yield scrapy.Request(linkExtensions1, self.parse_results)



    def parse_results(self, response):
        print("URL: " + response.url)
        main = response.css("div.post-image")
        href = main.css('a.zoom::attr(href)').extract()
        mainLinks = []
        if href:
            for x in href:
                link = "https:" + x
                mainLinks.append(link)
        else:
            gif1 = response.css("div.video-container source::attr(src)").extract()
            if gif1:
                for x in gif1:
                    gif_link = "https:" + x
                    mainLinks.append(gif_link)
            else:
                imgSrc = main.xpath('//img/@src').extract_first()
                imgSrc = "https:" + imgSrc
                mainLinks.append(imgSrc)
        nameHome = response.css("div.post-title-container")
        name = nameHome.xpath('//h1/text()').extract_first()
        if name == '':
            name = 'None'
        DatePosted = response.css("span.date::text").extract_first()

        con = lite.connect('test47.db')
        cur = con.cursor()
        cur.execute("INSERT INTO MemesTest1 VALUES (?, ?, ?, ?);", (name, DatePosted, pickle.dumps(mainLinks), response.url))
        con.commit()
        cursor = con.execute("SELECT rowid, Name, DatePosted, URL, MAINURL  from MemesTest1")
        for row in cursor:
           print("ID = ", row[0])
           print("Name = ", row[1])
           print("DatePosted = ", row[2])
           print("URLs = ", pickle.loads(row[3]))
           print("MAIN_URLs = ", row[4], "\n")
        con.close()
