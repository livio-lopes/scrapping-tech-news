from tech_news.database import find_news


# Requisito 10
def top_5_categories():
    """Seu código deve vir aqui"""

    all_news = find_news()
    count_categories = dict()
    for new in all_news:
        if new["category"] in count_categories:
            count_categories[new["category"]] += 1
        else:
            count_categories.setdefault(new["category"], 1)
    output = sorted(
        count_categories.keys(), key=lambda x: (-count_categories[x], x)
    )
    print(output[:5])
    return output[:5]


if __name__ == "__main__":
    print(top_5_categories())
