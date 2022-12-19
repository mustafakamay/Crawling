
import scrapy

from trendyol.items import TrendyolItem
from crawl.models import Crawlerr

class Trendyol(scrapy.Spider):
    name = 'atari'


    def start_requests(self):
        yield scrapy.Request(url='https://www.trendyol.com/atari/retro-mini-620-mario-oyunlu-av-retro-mini-oyun-konsolu-scart-basliksiz-p-36587919', callback=self.parse)

    def parse(self,response):
        pname = response.xpath("//h1[@class='pr-new-br']//text()").get()
        brand = response.xpath("//h1[@class='pr-new-br']/span/text()").get()
        sellingPrice = response.xpath("//span[@class='prc-org']/text()").get()
        discountedPrice =response.xpath("//span[@class='prc-dsc']/text()").get()
        category =response.xpath("//div[@class='category-gender-desc']/text()").get()
        merchantName =response.xpath("//div[@class='merchant-box-wrapper']/a/text()").get()
        merchantCity =response.xpath("//div[@class='category-gender-desc']/text()").get()
        merchantScore =response.xpath("//div[@class='widget-title product-seller-line']/div/div/div[@class='sl-pn']/text()").get()
        data = response.xpath("//script[@type='application/javascript']/text()")[0].get()

        otherMerchantNames = [i.split("merchantBadges")[1].split("name")[-1].replace('":"', "").replace('","', "") for i in
                        data.split("officialName")[:-1]]
        otherCityNames = [i.split(":")[1].split(",")[0].replace('"', "") for i in data.split("cityName")[1:]]
        otherSellerScores = [float(i.split('sellerScore":')[1].replace(",", "")) for i in
                         data.split('"sellerScoreColor"')[:-1]] 

        item = TrendyolItem()
        item["name"] = pname

        Crawlerr.objects.create(name = pname,
                                brand = brand,
                                sellingPrice = sellingPrice,
                                discountedPrice = discountedPrice,
                                category = category,
                                merchantName = merchantName,
                                merchantCity=merchantCity,
                                otherMerchantNames=otherMerchantNames,
                                otherCityNames = otherCityNames,
                                otherSellerScores = otherSellerScores)
        return item
