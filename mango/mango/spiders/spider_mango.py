from pathlib import Path
from scrapy_splash import SplashRequest
import scrapy


class MangoSpider(scrapy.Spider):
    name = 'mango'

    def start_requests(self):
        url = 'https://shop.mango.com/bg-en/women/skirts-midi/midi-satin-skirt_17042020.html?c=99response'
        yield SplashRequest(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        product = response.css('title')
        # for item in product:
        yield {
           'name': product.css('title::text').get()[0:16],

        }