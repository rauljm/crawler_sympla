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
        yield self.get_data_url_events(response)

    def get_data_url_next_page(self, response):
        for res in response.css('button.btn-dark-transparent'):
            return {
                'url': res.root.values()[1]
            }

    def get_data_url_events(self, response):
        urls = {}
        response = response.css('a.event-box-link').xpath('@href').extract()
        for index, res in enumerate(response):
            urls.update({'url_{}'.format(index): res})
        return urls
    
    def get_next_page_url(self, response):
        for res in response.css('button.btn-dark-transparent'):
           return res.root.values()[1] 