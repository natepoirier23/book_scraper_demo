from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Base URL to resolve relative book detail links and next-page links.
BASE_URL = "https://books.toscrape.com/catalogue/"

def extract_books(html: str) -> list[dict]:
    """
    Parse a listing page and extract:
    - title
    - price
    - rating
    - detail page URL
    """
    soup = BeautifulSoup(html, "html.parser")
    items = soup.select("article.product_pod")

    books = []
    for item in items:
        link = item.select_one("h3 a")
        if not link:
            continue

        title = link.get("title", "").strip()
        relative_url = link.get("href", "").strip()
        full_url = urljoin(BASE_URL, relative_url)

        price_tag = item.select_one(".price_color")
        price = price_tag.text.strip() if price_tag else ""

        rating_tag = item.select_one("p.star-rating")
        rating = ""
        if rating_tag:
            classes = rating_tag.get("class", [])
            rating = next((c for c in classes if c != "star-rating"), "")

        books.append({
            "title": title,
            "price": price,
            "rating": rating,
            "url": full_url,
        })

    return books

def extract_next_page_url(html: str) -> str | None:
    """
    Returns the full URL of the next page, if present.
    """
    soup = BeautifulSoup(html, "html.parser")
    next_link = soup.select_one("li.next a")

    if not next_link:
        return None

    relative = next_link.get("href", "").strip()
    return urljoin(BASE_URL, relative)
