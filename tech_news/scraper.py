import requests
import re
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
    selector = Selector(text=html_content)
    next_page = selector.css("div.nav-links a.next::attr(href)").get()
    if not next_page:
        return None
    return next_page


def remove_tags_html(text):
    # Usando uma expressão regular para remover as tags HTML
    clear = re.compile("<.*?>")
    text_without_tags = re.sub(clear, "", text)
    return text_without_tags


def remove_space_no_break(text):
    # clear = re.sub(r'\xa0', ' ', text)
    return re.sub(r"\xa0", "", text)


def scrape_news_url(selector):
    remove_facebook_link = "https://www.facebook.com/sharer.php?u="
    get_url_btn_facebook = selector.css(
        "div.pk-share-buttons-facebook a::attr(href)"
    ).get()
    return get_url_btn_facebook.replace(remove_facebook_link, "")


def scrape_news_title(selector):
    html_text = selector.css("h1.entry-title::text").get()
    html_text = remove_tags_html(html_text)
    html_text = remove_space_no_break(html_text)
    return html_text


def scrape_news_timestamp(selector):
    return selector.css("ul.post-meta li.meta-date::text").get()


def scrape_news_author(selector):
    author = selector.css("h5.title-author a::text").get()
    return author.replace("\n", "").replace("\t", "")


def scrape_news_reading_time(selector):
    reading_time = selector.css(
        "ul.post-meta li.meta-reading-time::text"
    ).get()
    time = re.search(r"\b(\d+)\b", reading_time)
    return int(time.group(1))


def scrape_news_summary(selector):
    html_text = selector.css("div.entry-content *").css("p").get()
    html_text = remove_tags_html(html_text)
    html_text = remove_space_no_break(html_text)
    # bode = BeautifulSoup(html_text, 'html.parser')
    return html_text.strip()


def scrape_news_category(selector):
    return selector.css("div.meta-category span.label::text").get()


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    infos = {
        "url": scrape_news_url(selector),
        "title": scrape_news_title(selector),
        "timestamp": scrape_news_timestamp(selector),
        "writer": scrape_news_author(selector),
        "reading_time": scrape_news_reading_time(selector),
        "summary": scrape_news_summary(selector),
        "category": scrape_news_category(selector),
    }
    return infos


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError


if __name__ == "__main__":
    URL_BLOG = "https://blog.betrybe.com/"
    URL_NEWS = (
        "https://blog.betrybe.com/carreira/empowerment-lideranca-o-que-e/"
    )
    html_content = fetch(URL_NEWS)
    # print(html_content)
    # list_news = scrape_updates(html_content)
    # next_page = scrape_next_page_link(html_content)
    scrape_news(html_content)
