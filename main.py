from web_scraper import WebScraper

scraper = WebScraper()

while True:
    print("\n📚 PYTHON WEB SCRAPER")
    print("1. View Books")
    print("2. Search Book")
    print("3. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        scraper.show_books()

    elif choice == "2":
        keyword = input("Enter book name: ").strip()

        if keyword:
            scraper.search_book(keyword)
        else:
            print("Search cannot be empty. ❌")

    elif choice == "3":
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice!")