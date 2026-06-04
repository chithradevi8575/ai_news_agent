import feedparser

def get_news():
    feed = feedparser.parse(
        "https://news.google.com/rss/search?q=Artificial+Intelligence"
    )

    news = []
    for entry in feed.entries[:10]:
        news.append({
            "title": entry.title,
            "link": entry.link
        })

    return news