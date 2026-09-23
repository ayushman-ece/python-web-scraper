# 📚 Python Web Scraper

A Python web scraping project that extracts book information from a website using `Requests` and `BeautifulSoup`.

---

## 🎯 Project Goal

Build a Python program that can access a webpage, read its HTML, extract useful information, and allow users to search the scraped data.

The project demonstrates:

**Website → HTML → BeautifulSoup → Python → Data**

---

## ✨ Features

- 🌐 Fetch webpage data
- 📄 Parse HTML using BeautifulSoup
- 📚 Extract book titles
- 💰 Extract book prices
- ⭐ Extract book ratings
- 🔎 Search books by title
- 📋 Display all scraped books
- ⚠️ Handle network/API errors
- ⏱️ Use request timeout

---

## 🛠️ Technologies Used

- Python
- Requests
- BeautifulSoup4
- HTML
- Object-Oriented Programming
- Lists
- Dictionaries

---

## 📁 Project Structure

```text
python-web-scraper/
│
├── main.py
├── web_scraper.py
├── README.md
└── .gitignore
```

---

## 🌐 Website Used

The project uses:

```text
https://books.toscrape.com/
```

Books to Scrape is a website designed for practicing web scraping.

---

## 🚀 Installation

Install the required libraries:

```bash
pip install requests beautifulsoup4
```

---

## ▶️ How to Run

Run the program:

```bash
python main.py
```

---

## 🖥️ Menu

```text
📚 PYTHON WEB SCRAPER
1. View Books
2. Search Book
3. Exit
```

---

# 🔄 How the Scraper Works

The application follows this flow:

```text
Website
   ↓
requests.get()
   ↓
HTML Response
   ↓
BeautifulSoup
   ↓
Find HTML Elements
   ↓
Extract Data
   ↓
Python Dictionaries
   ↓
Display / Search
```

---

# 🌐 Fetching the Website

The project uses:

```python
response = requests.get(url, timeout=10)
```

`requests.get()` sends a GET request to the website.

The response contains the webpage HTML.

---

# 📄 Reading HTML

The HTML is passed to BeautifulSoup:

```python
soup = BeautifulSoup(response.text, "html.parser")
```

BeautifulSoup allows Python to navigate and search the HTML structure.

---

# 🔎 Finding HTML Elements

The project finds book cards using:

```python
soup.find_all("article", class_="product_pod")
```

`find_all()` returns all matching elements.

Each book is represented by an HTML `article` element.

---

# 📚 Extracting Book Title

The title is extracted using:

```python
title = book.find("h3").find("a")["title"]
```

The program navigates:

```text
article
   ↓
h3
   ↓
a
   ↓
title attribute
```

---

# 💰 Extracting Price

The price is extracted using:

```python
price = book.find(
    "p",
    class_="price_color"
).get_text(strip=True)
```

`get_text()` extracts the visible text.

---

# ⭐ Extracting Rating

The rating is stored inside the HTML class.

For example:

```html
<p class="star-rating Three">
```

The program gets the class:

```python
rating_class = book.find(
    "p",
    class_="star-rating"
)["class"]
```

Then:

```python
rating = rating_class[1]
```

extracts:

```text
Three
```

---

# 📦 Storing Scraped Data

Each book is stored as a dictionary:

```python
{
    "title": title,
    "price": price,
    "rating": rating
}
```

All books are stored inside a list.

This makes the scraped data easy to process using normal Python.

---

# 🔎 Searching Books

The search feature uses:

```python
if keyword.lower() in book["title"].lower():
```

This provides case-insensitive partial searching.

For example:

```text
Search:
python
```

can find titles containing `Python`.

---

# ⚠️ Error Handling

The project handles network problems using:

```python
try:
    ...
except requests.RequestException:
    print("Network error. ❌")
```

The request also uses:

```python
timeout=10
```

so the program does not wait indefinitely for a response.

---

# 🧠 Important Concepts Learned

### Requests

```python
requests.get()
```

Used to request webpage data.

### BeautifulSoup

```python
BeautifulSoup()
```

Used to parse HTML.

### `find()`

Finds one matching HTML element.

### `find_all()`

Finds multiple matching HTML elements.

### `get_text()`

Extracts visible text from an HTML element.

### HTML Attributes

```python
element["title"]
```

Extracts an HTML attribute.

### Lists

Used to store multiple scraped books.

### Dictionaries

Used to represent individual book information.

---

# 📚 Connection With Previous Project

Project #40:

```text
API → JSON → Python → Analysis
```

Project #41:

```text
Website → HTML → BeautifulSoup → Python → Analysis
```

The major difference is the type of data being received.

---

# 🔮 Future Improvements

The project can later be upgraded with:

- Pagination
- Scraping multiple pages
- Price filtering
- Rating filtering
- Sorting by price
- Export to CSV
- SQLite database storage
- Duplicate handling
- Streamlit interface
- Scheduled scraping
- Product/category filtering

---

# 👨‍💻 Author

**Ayushman Tiwari**

GitHub:

https://github.com/ayushman-ece

---

## ⭐ Project Status

**Completed — Basic Version ✅**

The advanced version will extend this project with pagination, filtering, sorting, data storage, and additional scraping features.