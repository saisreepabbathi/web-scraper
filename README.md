🛒 Price Comparison Web Scraper
A Python tool to compare product prices across e-commerce platforms like Amazon and Flipkart.

📌 Overview
This project is a simple yet powerful web scraper built using Python. It allows users to enter the name of a product and automatically compares its prices across multiple online shopping websites. The scraper fetches real-time data from search result pages using HTTP requests, parses the HTML using BeautifulSoup, and identifies the best deal available.

💡 Features
Compare prices across Amazon and Flipkart

Command-line interface for user input

Dynamic URL generation and HTML parsing

Anti-blocking headers and random delays

Error handling and logging

Optional CSV export of price data

Modular and scalable code structure

🚀 Getting Started
🔧 Prerequisites
Python 3.x

Internet connection

📦 Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/price-comparison-scraper.git
cd price-comparison-scraper
Install required libraries:

bash
Copy
Edit
pip install requests beautifulsoup4 pandas
▶️ Usage
Run the script directly from the terminal:

bash
Copy
Edit
python scraper.py
Then enter the product name when prompted:

yaml
Copy
Edit
Enter product name: iPhone 13
✅ Sample Output
yaml
Copy
Edit
Amazon: ₹61,999  
Flipkart: ₹59,999  
Best deal: Flipkart at ₹59,999
🧠 How It Works
Takes user input for the product name.

Builds search URLs for supported platforms.

Sends HTTP requests with browser-like headers.

Parses returned HTML for price elements using BeautifulSoup.

Cleans and compares prices.

Displays the best deal and optionally saves results to a CSV file.

📁 Project Structure
cpp
Copy
Edit
📦 price-comparison-scraper/
├── scraper.py
├── requirements.txt
├── README.md
└── scraper.log  (auto-generated)
📌 Limitations
May break if website structure changes

Does not handle JavaScript-rendered content (e.g., dynamic loading)

Currently limited to Amazon and Flipkart

