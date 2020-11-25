#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 15:40:33 2020

@author: myriam
"""
fetch("http://rss.jobsearch.monster.com/rssquery.ashx?")response.xpath("/http://rss.jobsearch.monster.com/rssquery.ashx?").extract()
response.xpath("//div[@class='quote']/span[@class='text']/text()").extract()