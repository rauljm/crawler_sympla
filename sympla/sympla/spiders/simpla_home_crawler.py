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
        page = response.url.split("/")[-2]
        filename = 'sympla-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
