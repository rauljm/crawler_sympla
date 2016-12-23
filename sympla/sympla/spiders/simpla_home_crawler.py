import scrapy


class QuotesSpider(scrapy.Spider):
    name = "sympla"

    def start_requests(self):
        urls = [
            'http://www.sympla.com.br/eventos/sao-paulo-sp',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for sympla in response.css('div.input-group-btn'):
            yield {
                'span': str(sympla.css('span::text').extract()).encode('utf8'),
                'a': str(sympla.css('a::text').extract()).encode('utf8')
                # 'author': sympla.css('span small::text').extract_first(),
                # 'tags': sympla.css('div.tags a.tag::text').extract(),
            }