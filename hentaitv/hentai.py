import requests
import sys
import json
from lxml import etree

class HantaiTV:
    def __init__(self):
        self.host = r"https://hentai.tv"
        self.proxy = {'http': 'xxx'}

    def search(self, page):
        url = self.host + r"/wp-json/wp/v2/results?taxonomy=none&search=none&term=none&blacklist=&genres=&brands=&sort=1&page=" + page
        # print(url)
        referer = 'https://hentai.tv/?s='
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie':'_ga=03ba1e7d-2fb3-4384-bf24-0871c55a945e; cf_zaraz_google-analytics_v4_1fd5=true; google-analytics_v4_1fd5__ga4=91cdd9f7-a70b-4a3d-8b62-24387b859349; trp_language=en_US; popcashpu=1; google-analytics_v4_1fd5__ga4sid=2106471358; google-analytics_v4_1fd5__session_counter=7; google-analytics_v4_1fd5__engagementPaused=1676443559481; google-analytics_v4_1fd5__engagementStart=1676443665497; google-analytics_v4_1fd5__counter=159; google-analytics_v4_1fd5__let=1676443665497',
            'referer': referer,
            'x-requested-with': 'XMLHttpRequest'
        }

        res = requests.get(url, headers= headers, proxies=self.proxy).json()
        html = res['data']['html']

        selectors = etree.HTML(html)

        # imgs = selectors.xpath('//div/div[1]/figure/img/@src')
        # hrefs = selectors.xpath('//div/div[2]/div/a/@href')
        # title = selectors.xpath('//div/div[2]/div/a/text()')

        list = []
        for i in selectors:
            for j in i:
                img = j.xpath('div[1]/figure/img/@src')
                href = j.xpath('div[2]/div/a/@href')
                title = j.xpath('div[2]/div/a/text()')
                data = {}
                data['title'] = title[0]
                data['img'] = img[0]
                data['href'] = href[0]
                list.append(data)

        return list

    def dateinfo(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.5',
            'content-type': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie':'_ga=03ba1e7d-2fb3-4384-bf24-0871c55a945e; cf_zaraz_google-analytics_v4_1fd5=true; google-analytics_v4_1fd5__ga4=91cdd9f7-a70b-4a3d-8b62-24387b859349; trp_language=en_US; popcashpu=1; google-analytics_v4_1fd5__ga4sid=1741789799; google-analytics_v4_1fd5__session_counter=6; inter=1; google-analytics_v4_1fd5__engagementPaused=1676428721250; google-analytics_v4_1fd5__engagementStart=1676428722404; google-analytics_v4_1fd5__counter=105; google-analytics_v4_1fd5__let=1676428722404'
        }

        html = requests.get(url, headers=headers, proxies=self.proxy).content
        selector = etree.HTML(html)

        release_date = selector.xpath('//*[@id="aawp"]/div[2]/div/div[1]/div[4]/aside[2]/p/span[text()="Release Date"]/../span[2]/text()')
        upload_date = selector.xpath('//*[@id="aawp"]/div[2]/div/div[1]/div[4]/aside[2]/p/span[text()="Upload Date"]/../span[2]/text()')

        data = {}
        data['release_date'] = release_date[0] if release_date else None
        data['upload_date'] = upload_date[0] if upload_date else None

        return data

