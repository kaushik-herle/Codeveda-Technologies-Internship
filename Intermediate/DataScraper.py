import requests
from bs4 import BeautifulSoup
import csv

def scrape_products():
    url = "https://webscraper.io/test-sites/e-commerce/static"

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        products = []

        # Each product card
        for item in soup.find_all("div", class_="thumbnail"):
            name = item.find("a", class_="title").text.strip()
            price = item.find("h4", class_="price").text.strip()
            description = item.find("p", class_="description").text.strip()

            products.append({
                "name": name,
                "price": price,
                "description": description
            })

        # Save to CSV
        with open("products.csv", "w", newline="", encoding="utf-8") as file:
            fieldnames = ["name", "price", "description"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(products)

        print(f"Scraped {len(products)} products and saved to products.csv")

    except requests.exceptions.ConnectionError:
        print("Error: No internet connection.")
    except requests.exceptions.HTTPError:
        print("Error: Failed to fetch page.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    scrape_products()
