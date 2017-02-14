#JFCS_scrapy.py
import scrapy

class BlogSpider(scrapy.Spider):
    name = 'BlogSpider'
    start_urls = ['https://blog.scrapinghub.com'] #the url that has all the posts on it

    def parse(self, response): #gets all the info off page 1 and breaks it down
        for title in response.css('div.textwidget'): #loops through all the posts on the page
            print(title.css('a ::text').extract_first()) #prints the posts title

        if response.css('div.prev-post > a ::attr(href)').extract_first(): #checks if there is a next page
            yield scrapy.Request(response.urljoin(response.css('div.prev-post > a ::attr(href)').extract_first()), callback=self.parse) #get all the posts off the next page


#scrapy runspider JFCS_scrapy.py
