from typing import Dict, List

import requests
from bs4 import BeautifulSoup


def scrape_page(page_number: str) -> List[Dict[str, str]]:
    response = requests.get(f"https://news.ycombinator.com/news?p={page_number}")
    yc_web_page = response.text
    soup = BeautifulSoup(yc_web_page, 'html.parser')

    articles = []

    for article_tag in soup.find_all(name="span", class_="titleline"):
        title = article_tag.getText()
        link = article_tag.find("a")["href"]
        articles.append({"title": title, "link": link})

    return articles
