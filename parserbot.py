import requests
from bs4 import BeautifulSoup as BS

from fake_useragent import UserAgent
import configparser


config = configparser.ConfigParser()
config.read('config.cfg')

MAIN_URL = config.get("parser_bot", "MAIN_URL", fallback='')
BLOG_URL = config.get("parser_bot", "BLOG_URL", fallback='')

user_agent = UserAgent()
headers = {'user-agent': user_agent.random}


# Return a page for the parsing
def get_response(url, headers):
    page = requests.get(url=url, headers=headers).text
    response = BS(page, 'lxml')
    return response


# Made pagination of pages
def made_pagination(response):
    pagination = response.find('span', class_='pagination__current').get_text()[0]
    return pagination


# Get collects of articles
def get_articles(paginate, headers, articles, page_article):
    print("Parsing of new article is began")
    for page in range(page_article, int(paginate)):
        article = []
        url = f'{BLOG_URL}?page={page + 1}'
        request = get_response(url=url, headers=headers)
        block_contents = request.find_all('div', class_='blog-post-card__info')

        for content in block_contents:
            title = content.find('a').text.strip()
            link_post = MAIN_URL + content.find('a').get('href')
            if title not in articles:
                article.append({
                    'Title': title,
                    'Link': link_post
                })
                return article, page_article
            else:
                continue
        page_article += 1


# Main parsing function
def parse_articles(articles, page_article):
    response = get_response(url=BLOG_URL, headers=headers)
    paginate = made_pagination(response=response)
    article, page_article = get_articles(
        paginate=paginate,
        headers=headers,
        articles=articles,
        page_article=page_article
        )
    return article, page_article


if __name__ == '__main__':
    pass
