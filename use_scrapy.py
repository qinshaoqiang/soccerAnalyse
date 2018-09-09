# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 21:31:10 2018

@author: Administrator
"""
import scrapy
class Baisibudejie(scrapy.Spider):
    name = 'jokes'
    start_urls = ['http://www.budejie.com/text/']

    def parse(self, response):
        lies = response.css('div.j-r-list >ul >li')
        for li in lies:
            username = li.css('a.u-user-name::text').extract()
            content = li.css('div.j-r-list-c-desc a::text').extract()
            yield {'username': username, 'content': content}