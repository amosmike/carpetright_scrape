import scrapy


class CarpetspiderSpider(scrapy.Spider):
    name = "carpetspider"

    def start_requests(self):
        yield scrapy.Request('https://www.carpetright.co.uk/carpets/',
                              meta={'playwright': True})

    def parse(self, response):
        pass
