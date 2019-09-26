import time
import scrapy


class MemedroidSpider(scrapy.Spider):
    name = 'memedroid'

    start_urls = [
        'https://www.memedroid.com/memes/random',
        'https://www.memedroid.com/memes/top/day',
        'https://www.memedroid.com/memes/top/week',
        'https://www.memedroid.com/memes/top/month',
        'https://www.memedroid.com/memes/top/ever',
    ]

    def parse(self, response):
        for article in response.css('article'):
            img_id = article.css('article::attr(id)').get().split('-')[-1]
            img_url = article.css('img[src*="https"]::attr(src)').get()
            img_name = article.css('img[src*="https"]::attr(alt)').get()
            rating_container = article.css(
                'div[class="item-rating-container"]')
            img_score = rating_container.css(
                'span[class*="green"]::text').get()
            if not img_score:
                continue
            if int(img_score.replace('%', '')) < 80:
                continue

            yield {
                "_id": img_id,
                "img_url": img_url,
                "img_name": img_name,
                "img_score": img_score
            }
        time.sleep(0.2)
        next_page = response.css('nav[class="hidden"] a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
