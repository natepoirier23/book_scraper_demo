import time
import random
from fetch import fetch_url
from parsing import extract_books, extract_next_page_url
from export import write_to_csv, write_to_json

START_URL = "https://books.toscrape.com/catalogue/page-1.html"
MAX_PAGES = 200

def main():
    all_books = []
    page_counter = 0
    next_url = START_URL

    while next_url:
        print(f"Scraping: {next_url}")

        html = fetch_url(next_url)
        if html is None:
            print("Could not fetch page. Stopping.")
            break

        books = extract_books(html)
        print(f"  Found {len(books)} books")
        all_books.extend(books)

        next_url = extract_next_page_url(html)

        wait = random.uniform(0.8, 1.8)
        print(f"Waiting {wait:.2f}s...")
        time.sleep(wait)

        page_counter += 1
        if page_counter >= MAX_PAGES:
            print("Reached max pages. Stopping.")
            break

    print(f"Total books collected: {len(all_books)}")

    write_to_csv(all_books, "books.csv")
    write_to_json(all_books, "books.json")


if __name__ == "__main__":
    main()
