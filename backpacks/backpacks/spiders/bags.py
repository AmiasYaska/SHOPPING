import scrapy
import json


class BagsSpider(scrapy.Spider):
    name = "bags"
    allowed_domains = ["target.com"]

    def start_requests(self):
        yield scrapy.Request(
            url="https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v2?key=9f36aeafbe60771e321a7cc95a78140772ab3e96&channel=WEB&count=24&default_purchasability_filter=true&include_dmc_dmr=true&include_sponsored=true&keyword=backpacks&new_search=true&offset=72&page=%2Fs%2Fbackpacks&platform=desktop&pricing_store_id=1771&scheduled_delivery_store_id=1771&store_ids=1771%2C1768%2C1113%2C3374%2C1792&useragent=Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F122.0.0.0+Safari%2F537.36&visitor_id=018CB60F6F0E0201B85AB692A144B57D&zip=52404",
            method="GET",
            callback=self.parse
        )

    def parse(self, response):
        print(response.body)
