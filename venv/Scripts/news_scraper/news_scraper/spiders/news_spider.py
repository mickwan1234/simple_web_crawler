import scrapy
import datetime
from scrapy import Request

class NewsSpider(scrapy.Spider) : 
    name = "news"

    start_urls= [
        'https://www.vsd.vn/vi/search?type=4&obj=110&buss=0'
    ]

    def parse(self, response):
        baselink = response.url.split("/")[0] +"/" + response.url.split("/")[1] +"/" + response.url.split("/")[2]
        base_selector = response.xpath("//ul[@class='list-news']/li/h3/a//@href").extract()
        urls = []
        for sel in base_selector:
              urls.append(baselink + sel)
        for link in urls:
            yield Request(link, callback=self.parse_link)

    def parse_link(self, response): 
        source_link = response.url
        source_news = "VSD"
        title = response.xpath("//h3[@class='title-category']/text()")[0].extract()
        publish_at = response.xpath("//div[@class='time-newstcph']/text()").extract()[0].rstrip()
        content = response.xpath("//div[@class='col-md-12']")[0].extract()
        slug = response.url.split("/")[-2]+"/"+response.url.split("/")[-1]
        created_at = datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")
        print("source_link: " + source_link)
        print("source_news: " + source_news)
        print("thumbnail: None")
        print("title: " + title)
        print("description: None")
        print("content: "+ content)
        print("publish_at: " + publish_at)
        print("slug_url: /" + slug)
        print("created_at: "+ created_at)
        print("created_by: None")
        

    
