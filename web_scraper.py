import requests
from bs4 import BeautifulSoup


class WebScraper:

    def get_books(self):
        url = "https://books.toscrape.com/"

        try:
            response = requests.get(url, timeout=10)

            if response.status_code != 200:
                print("Failed to fetch website. ❌")
                return []

            soup = BeautifulSoup(response.text, "html.parser")

            books = []

            for book in soup.find_all("article", class_="product_pod"):
                title = book.find("h3").find("a")["title"]
                price = book.find(
                    "p",
                    class_="price_color"
                ).get_text(strip=True)

                rating_class = book.find(
                    "p",
                    class_="star-rating"
                )["class"]

                rating = rating_class[1]

                books.append({
                    "title": title,
                    "price": price,
                    "rating": rating
                })

            return books

        except requests.RequestException:
            print("Network error. ❌")
            return []

    def search_book(self, keyword):
        books = self.get_books()

        found = False

        for book in books:
            if keyword.lower() in book["title"].lower():
                print("\n===== BOOK FOUND =====")
                print(f"Title  : {book['title']}")
                print(f"Price  : {book['price']}")
                print(f"Rating : {book['rating']}")
                found = True

        if not found:
            print("No matching books found.")

    def show_books(self):
        books = self.get_books()

        if not books:
            print("No books found.")
            return

        print("\n===== BOOKS =====")

        for index, book in enumerate(books, start=1):
            print(f"\n{index}. {book['title']}")
            print(f"   Price  : {book['price']}")
            print(f"   Rating : {book['rating']}")