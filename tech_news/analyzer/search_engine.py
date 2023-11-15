from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    """Seu código deve vir aqui"""
    query = {"title": {"$regex": title, "$options": "i"}}

    result = search_news(query)

    result = [(doc["title"], doc["url"]) for doc in result]

    return result


def converter_date(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    date_formated = date_obj.strftime("%d/%m/%Y")

    return date_formated


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        date = converter_date(date)
        query = {"timestamp": {"$eq": date}}
        result = [(doc["title"], doc["url"]) for doc in search_news(query)]
        return result
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
