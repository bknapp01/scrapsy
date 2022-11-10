from scrapy import Spider
from time import time, ctime
from scrapy.crawler import CrawlerProcess

class aurica(Spider):
    name = 'aurica'
    allowed_domains = ['compreoro.com', 'aurica.cl', 'gainesvillecoins.com', 'goldstocklive.com']
    start_urls = ['https://aurica.cl/tienda/gold-maple-leaf-1oz/',
                  'https://aurica.cl/tienda/gold-canadian-maple-leaf-1-2-oz/',
                  'https://aurica.cl/tienda/american-eagle-1-2-oz/',
                  'https://aurica.cl/tienda/moneda-de-oro-maple-leaf-canada-1-4-oz/',
                  'https://aurica.cl/tienda/gold-maple-leaf-1-10oz/',
                  'https://compreoro.com/producto/moneda-canadian-maple-leaf-gold-1-oz/',
                  'https://compreoro.com/producto/moneda-american-eagle-type-2-gold-1-oz/',
                  'https://compreoro.com/producto/moneda-1993-canadian-maple-leaf-gold-1-10-oz/',
                  'https://compreoro.com/producto/moneda-canadian-maple-leaf-gold-1-oz-cev/',
                  'https://compreoro.com/producto/moneda-american-eagle-type-2-gold-1-oz-cev/',
                  'https://www.gainesvillecoins.com/products/158985/1-oz-american-gold-eagle-coins',
                  'https://www.gainesvillecoins.com/products/158550/1-2-oz-american-gold-eagle-coins',
                  'https://www.gainesvillecoins.com/products/180843/2022-1-4-oz-american-gold-eagle',
                  'https://www.gainesvillecoins.com/products/180331/2021-1-10-oz-gold-american-eagle-brilliant-uncirculated'
                  ]


    def parse(self, response):
        t = time()
        url = response.url
        if "aurica.cl" in url:
            coin_name = response.css("h1::text").get()
            coin_price = response.xpath("//*[@class='price']/span/bdi/text()").get()
            yield {"url": url,
                   "coin_name": coin_name,
                   "time": ctime(t),
                   "coin_price": coin_price}

        elif "compreoro.com" in response.url:
            coin_name = response.xpath("//h1/text()").extract_first()
            coin_price = response.xpath("//*[@class='price product-page-price price-not-in-stock']/span/bdi/text()").extract_first()
            if coin_price:
                yield {"url": url,
                       "coin_name": coin_name,
                       "time": ctime(t),
                       "coin_price": coin_price}
            else:
                coin_name = response.xpath("//h1/text()").extract_first()
                coin_price = response.xpath("//*[@class='price product-page-price ']/span/bdi/text()").extract_first()
                yield {"url": url,
                       "coin_name": coin_name,
                       "time": ctime(t),
                       "coin_price": coin_price}
        elif "gainesvillecoins.com" in response.url:
            coin_name = response.xpath("//h1/text()").extract_first()
            coin_price = response.xpath("//td[2]/text()").extract_first()
            if coin_price:
                coin_price.replace("$", "")
                yield {"url": url,
                       "coin_name": coin_name,
                       "time": ctime(t),
                       "coin_price": coin_price}
            else:
                yield {"url": url,
                       "coin_name": coin_name,
                       "time": ctime(t),
                       "coin_price": "None"}

