from scraper import EightKunPageScraper
import scrapy, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from eightKun import EightKunPageScraper

class EightkunSpider(scrapy.Spider):
    name = 'eightKun'
    allowed_domains = ['8kun.top']
    start_urls = ['http://8kun.top/']

    def parse(self, response):
        EightKunPageScraper.get_posts(
            EightKunPageScraper.parse_content(
            response))
