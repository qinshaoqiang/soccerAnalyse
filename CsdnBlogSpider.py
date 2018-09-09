# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 21:52:20 2018

@author: Administrator
"""
import scrapy
import urllib

class CsdnBlogSpider(scrapy.Spider):
    name = 'csdn_blog'
    start_urls = ['http://blog.csdn.net/u011054333/article/list/1']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.base_url = 'http://blog.csdn.net'

    def parse(self, response):
        articles = response.css('div#article_list div.article_item')
        for article in articles:
            title = article.css('div.article_title a::text').extract_first().strip()
            link = self.base_url + article.css('div.article_title a::attr(href)').extract_first().strip()
            yield {'title': title, 'link': link}

        pages = response.css('div#papelist')
        next_page_url = pages.css('a').re_first('<a href=\"(.*)\">下一页')
        if next_page_url is not None:
            yield scrapy.Request(urllib.parse.urljoin(self.base_url, next_page_url))