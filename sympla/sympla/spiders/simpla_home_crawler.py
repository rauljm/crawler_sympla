import os
import scrapy
import json
import random


class SymplaGenrateUrlsSpider(scrapy.Spider):
    name = "sympla_generate_url"

    def __init__(self):
        pass

    def start_requests(self):
        # url = 'http://www.sympla.com.br/eventos/belo-horizonte-mg'  # passo 1
        # yield scrapy.Request(url=url, callback=self.parse)  # passo 1

        #################################################################
        urls = self.read_json_archive()
        for url in urls:
            for key in url.keys():
                yield scrapy.Request(url=url[key], callback=self.parse)
        #################################################################

    def parse(self, response):
        # for url in self.get_url_events_for_pages(response):  # passo 1
        #     yield scrapy.Request(url=url, callback=self.parse_2)  # passo 1
        #################################################################
        yield self.save_data_from_event(response)
        ################################################################

    def parse_2(self, response):
        yield self.get_data_url_events(response)

    def get_data_url_events(self, response):
        urls = {}
        responses = response.css('a.event-box-link').xpath('@href').extract()
        for index, res in enumerate(responses):
            urls.update({'url_{}'.format(index): res})
        return urls

    def save_html_page(self, response):
        filename = 's_{}.html'.format(str(random.randrange(0, 100000000, 1)))
        path = "sympla/html_pages/"
        fullpath = os.path.join(path, filename)

        with open(fullpath, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

    def read_json_archive(self, file_path=None):
        if not file_path:
            file_path = '/home/raul/projects/scrapy/crawler_sympla/sympla/bh.json'
        _json = open(file_path, 'r')

        data = json.load(_json)
        return data

    def save_data_from_event(self, response):
        event = {}
        payment = response.css('form span::text').extract()

        event.update(
            {'event_name':
             response.css('title::text').extract()[0].replace("Sympla", "").replace("-", "")}
        )
        event.update({'event_date': response.css('div.col-md-12 div::text').extract()[2]})
        event.update(
            {'event_local': response.css('p.margin-bottom-20-xs::text').extract()[1]}
        )
        event.update(
            {'event_description': response.css(
                'div.container.border-top.border-left.border-right.event-section p'
            ).extract()}
        )
        event.update({'event_productor': response.css('h4.kill-top-margin::text').extract()[2]})
        event.update({'other_informations_productor': response.css('p.text-center-xs.text-left-md::text').extract()})
        event.update({'link': response.url})
        event.update({'payment': payment})
        return event

    def get_numbers_of_events(self, response):
        list_of_number = response.css(
            'div.header-list div.container h3 strong::text'
        ).extract()

        return int(list_of_number[0]) / 21

    def get_url_events_for_pages(self, response):
        lista_events = []

        for nan in range(0, self.get_numbers_of_events(response)):
            lista_events.append(
                'http://www.sympla.com.br/eventos/sao-paulo-sp?ordem=relev%C3%A2ncia&pagina={}'.format(nan)
            )
        return lista_events


class SymplaCatchDataSpider(scrapy.Spider):
    name = "sympla_catch_data"

    def __init__(self):
        pass

    def start_requests(self):
        urls = self.read_json_archive()
        for url in urls:
            for key in url.keys():
                yield scrapy.Request(url=url[key], callback=self.parse)

    def parse(self, response):
        yield self.save_data_from_event(response)

    def read_json_archive(self, file_path=None):
        if not file_path:
            file_path = '/home/raul/projects/scrapy/crawler_sympla/sympla/bh.json'
        _json = open(file_path, 'r')

        data = json.load(_json)
        return data

    def save_data_from_event(self, response):
        event = {}
        payment = response.css('form span::text').extract()

        event.update(
            {'event_name':
             response.css('title::text').extract()[0].replace("Sympla", "").replace("-", "")}
        )
        event.update({'event_date': response.css('div.col-md-12 div::text').extract()[2]})
        event.update(
            {'event_local': response.css('p.margin-bottom-20-xs::text').extract()[1]}
        )
        event.update(
            {'event_description': response.css(
                'div.container.border-top.border-left.border-right.event-section p'
            ).extract()}
        )
        event.update({'event_productor': response.css('h4.kill-top-margin::text').extract()[2]})
        event.update({'other_informations_productor': response.css('p.text-center-xs.text-left-md::text').extract()})
        event.update({'link': response.url})
        event.update({'payment': payment})
        return event
