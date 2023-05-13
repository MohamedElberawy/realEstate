import scrapy


class Estate1PySpider(scrapy.Spider):
    name = "estate1.py"
    start_urls = ["https://realestate.eg/en/for-sale"]

    def parse(self, response):
        for item in response.css('.inner-text'):
            yield{
                'title':item.css('.title a::text').get(),
                'number':item.css('.number::text').get(),
                'location':item.css('.text::text').get(),
                'unit-space':item.css('.listing__attribute li:nth-child(4)::text').get(),
                'unit-type':item.css('.listing__attribute li:nth-child(1)::text').get()
            }
        
        # to go into the next pages
        next_page = response.css('[rel="next"]::attr(href)').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page)) 
