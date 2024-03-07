import scrapy
import json
from ..items import BackpacksItem


class BagsSpider(scrapy.Spider):
    name = "bags"
    allowed_domains = ["target.com"]

    MAX_PAGES = 50

    def start_requests(self):
        for page_num in range(self.MAX_PAGES):
            offset = page_num * 24
            # url = f"https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v2?key=9f36aeafbe60771e321a7cc95a78140772ab3e96&channel=WEB&count=24&default_purchasability_filter=true&include_dmc_dmr=true&include_sponsored=true&keyword=backpacks&new_search=true&offset={offset}&page=%2Fs%2Fbackpacks&platform=desktop&pricing_store_id=1771&store_ids=1771%2C1768%2C1113%2C3374%2C1792&useragent=Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F122.0.0.0+Safari%2F537.36&visitor_id=018CB60F6F0E0201B85AB692A144B57D&zip=52404",
            url = f"https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v2?key=9f36aeafbe60771e321a7cc95a78140772ab3e96&channel=WEB&count=24&default_purchasability_filter=true&include_dmc_dmr=true&include_sponsored=true&keyword=backpacks&new_search=true&offset={offset}&page=%2Fs%2Fbackpacks&platform=desktop&pricing_store_id=1771&store_ids=1771%2C1768%2C1113%2C3374%2C1792&useragent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36&visitor_id=018CB60F6F0E0201B85AB692A144B57D&zip=52404"

            yield scrapy.Request(
                url,
                method="GET",
                callback=self.parse
            )

    def parse(self, response):
        data = json.loads(response.body)
        products = data.get("data").get("search").get("products")

        for product in products:

            bag_item = BackpacksItem()

            bag_item["item_name"] = product["item"]["product_description"]["title"]
            bag_item["brand_name"] = product["item"]["primary_brand"]["name"]
            bag_item["image_url"] = product["item"]["enrichment"]["images"]["primary_image_url"]
            bag_item["price"] = product["price"]["current_retail"]

            yield bag_item

