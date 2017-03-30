
class BlogSpider(scrapy.Spider):
    name = 'BlogSpider'
    start_urls = ['https://blog.scrapinghub.com'] #the url that has all the posts on it

    def parse(self, response): #gets all the info off page 1 and breaks it down
        for title in response.css('div.textwidget'): #loops through all the posts on the page
            print(title.css('a ::text').extract_first()) #prints the posts title

        if response.css('div.prev-post > a ::attr(href)').extract_first(): #checks if there is a next page
            yield scrapy.Request(response.urljoin(response.css('div.prev-post > a ::attr(href)').extract_first()), callback=self.parse) #get all the posts off the next page

'''
To create a csv file:
scrapy crawl SPIDER_NAME -o filename.csv



Run: scrapy shell 'http://quotes.toscrape.com/page/1/'
to get info on the url

Run: response.css('title::text')[0].extract()
to get the first response of this code, as indicated by the [0] index


Run: quote = response.css("div.quote")[0]

    FROM: (div.quote)

<div class="quote">
    <span class="text">“The world as we have created it is a process of our
    thinking. It cannot be changed without changing our thinking.”</span>
    <span>
        by <small class="author">Albert Einstein</small>
        <a href="/author/Albert-Einstein">(about)</a>
    </span>
    <div class="tags">
        Tags:
        <a class="tag" href="/tag/change/page/1/">change</a>
        <a class="tag" href="/tag/deep-thoughts/page/1/">deep-thoughts</a>
        <a class="tag" href="/tag/thinking/page/1/">thinking</a>
        <a class="tag" href="/tag/world/page/1/">world</a>
    </div>
</div>


Run: title = quote.css("span.text::text").extract_first()
to get the title








Run: response.css('title')
to get a css version of the code used to write the title

Run: response.css('title::text').extract()
to get a text (extracted) version of the title




Run: response.css('title::text')[0].extract()
to get the first response of this code, as indicated by the [0] index

Run: response.css('title::text').extract_first()
to get the first response of this code

However, using .extract_first() avoids an IndexError and returns None when it doesn’t find any element matching the selection.
'''
