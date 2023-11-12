import requests
from time import sleep
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    sleep(1)
    try:
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        if response.status_code != 200:
            return None
        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    all_noticies = selector.css("div.entry-thumbnail a::attr(href)").getall()
    # print(all_noticies)
    return all_noticies


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError


if __name__ == "__main__":
    URL_BLOG = "https://blog.betrybe.com/"
    html_content = fetch(URL_BLOG)
    # print(html_content)
    list_news = scrape_updates(html_content)
