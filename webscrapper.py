import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

def delay():
    """Random delay to avoid getting blocked"""
    time.sleep(random.uniform(1, 3))

def scrape_website(url, selectors):
    """Generic scraping function for all websites"""
    try:
        delay()
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for selector in selectors:
            element = soup.select_one(selector)
            if element:
                price_text = element.get_text().replace(',', '').replace('₹', '').strip()
                if price_text and price_text.replace('.', '').isdigit():
                    return int(float(price_text))
        return None
    except Exception as e:
        print(f"Error scraping {url}: {str(e)}")
        return None

def scrape_amazon(product_name):
    url = f"https://www.amazon.in/s?k={product_name.replace(' ', '+')}"
    selectors = [
        'span.a-price-whole',
        'span.a-offscreen',
        'span.priceToPay span.a-price-whole',
        'div.a-price-whole'
    ]
    return scrape_website(url, selectors)

def scrape_flipkart(product_name):
    url = f"https://www.flipkart.com/search?q={product_name.replace(' ', '%20')}"
    selectors = [
        'div._30jeq3._1_WHN1',
        'div._30jeq3',
        'div._25b18c',
        'div._2rQ-NK'
    ]
    return scrape_website(url, selectors)

def scrape_myntra(product_name):
    url = f"https://www.myntra.com/{product_name.replace(' ', '-')}"
    try:
        response = requests.get(url, headers=HEADERS, timeout=15, allow_redirects=True)
        if 'search' in response.url:
            url = f"https://www.myntra.com/{product_name.replace(' ', '%20')}"
    except:
        pass
    
    selectors = [
        'span.pdp-price',
        'span.pdp-final-price',
        'div.pdp-price',
        'span.price-discounted'
    ]
    return scrape_website(url, selectors)

def scrape_nykaa(product_name):
    url = f"https://www.nykaa.com/search/result/?q={product_name.replace(' ', '%20')}"
    selectors = [
        'span.post-card__content-price-offer',
        'span.pull-left.price-offer',
        'span.pdp-price',
        'div.price-offer-container'
    ]
    return scrape_website(url, selectors)

def compare_prices(product_name):
    print(f"\n🔍 Searching for '{product_name}' across stores...")
    
    scrapers = {
        "Amazon": scrape_amazon,
        "Flipkart": scrape_flipkart,
        "Myntra": scrape_myntra,
        "Nykaa": scrape_nykaa
    }
    
    results = {}
    for site, scraper in scrapers.items():
        price = scraper(product_name)
        if price:
            results[site] = price
            print(f"✔️ Found on {site}: ₹{price:,}")
        else:
            print(f"❌ Not available on {site}")
    
    if not results:
        print("\n⚠️ Product not found on any store. Try:")
        print("- Different product name")
        print("- Check spelling")
        print("- Try again later")
        return
    
    best_site = min(results, key=results.get)
    print(f"\n🏆 Best deal: {best_site} at ₹{results[best_site]:,}")

if __name__ == "__main__":
    while True:
        product = input("\nEnter product name (or 'quit' to exit): ").strip()
        if product.lower() == 'quit':
            break
        if product:
            compare_prices(product)
        else:
            print("Please enter a product name")














