#!/usr/bin/env python3

from abc import abstractmethod
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


#urlParse = re.compile(r'https?://www.[\w_-].\w+/?[^\s]*')

def format_url_path(root, upath):
    parse = urlparse(upath)
    if (not parse.netloc) or (upath.startswith('//')):
        return urljoin(root, upath)
    return upath


class RequestError(Exception):
    pass


class EightKunCrawler

class EightKunPageScraper:

    def __init__(self, url) -> None:
        self._raw_content = None
        self._url = url
        self._raw_content = self._retrieve_content()

    def _retrieve_content(self):
        page = requests.get(self._url)
        if not page.ok:
            raise RequestError(
                f"request to {self._url} failed with {page.status_code}")
        return page.content

    @classmethod
    def parse_content(cls, content, parser="html.parser"):
        
        return BeautifulSoup(content, parser)
    
    def _get_text_from_post(self, postTagSet, segment_delimiter='\n'):
        out = ''
        for segment in postTagSet:
            out += segment.text + segment_delimiter
        return out
        
    @classmethod
    def get_posts(cls, soup):

        posts = soup.find_all('div', {
            'class': 'body'})
        pl = [tag.find_all('p', {'class': 'body-line'}) 
        for tag in posts]

        return list(map(self._get_text_from_post, pl))

    def get_all_links(self):
        return list(map(lambda l: format_url_path(
            self._url, l),
            filter(lambda t: t,
                   [tag.get('href') for tag in
                    self.parse_content().find_all('a')])))


# if __name__ == "__main__":
test = PageScraper("http://www.8kun.top")


parsed = test.parse_content()

links = test.get_all_links()
for link in links:
    print(link)
    # if 'qresearch' in link:
    #     print("\nFOUND IT\n")
print(f"{len(links)} links found in page")

test = PageScraper('http://www.8kun.top/qresearch/index.html')

posts = test.get_posts()