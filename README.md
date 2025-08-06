# WebScraping-AnyCallMobile
WebScraping for AnyCallMobileMM

---

# Web Scraper for AnyCall Smartphone Products

This project contains a web scraper that extracts product data (names and prices) from the **AnyCall Mobile** website’s smartphone category and saves the data into an Excel file.

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [How It Works](#how-it-works)
5. [Dependencies](#dependencies)
6. [License](#license)

---

## Overview

This Python script scrapes product details (such as **product names** and **prices**) from the **Smartphone** category on **AnyCall Mobile's** e-commerce website. The scraper:

* Fetches all pages containing smartphone products.
* Extracts product names and prices from each page.
* Saves the extracted data in an Excel file for further use or analysis.

---

## Installation

### 1. Clone the Repository

First, clone the repository to your local machine using Git:

```bash
git clone https://github.com/yourusername/anycall-mobile-scraper.git
```

### 2. Install Required Libraries

Make sure you have Python 3.x installed. Then, install the necessary libraries using `pip`:

```bash
pip install -r requirements.txt
```

Alternatively, you can manually install the required libraries by running:

```bash
pip install beautifulsoup4 requests pandas tqdm
```

### 3. Ensure You Have Excel Support

You will need `openpyxl` to save the data in Excel format. Install it via:

```bash
pip install openpyxl
```

---

## Usage

1. **Run the Python Script**

Once everything is set up, run the script to start scraping the data:

```bash
python scraper.py
```

This will:

* Extract the total number of pages for the smartphone category.
* Scrape product names and prices from each page.
* Save the extracted data in an Excel file named `AnyCall Data.xlsx`.

2. **View the Results**

After running the script, open `AnyCall Data.xlsx` in any spreadsheet application like Microsoft Excel or Google Sheets to view the scraped data.

---

## How It Works

### 1. **Extract Maximum Page Number**

The script begins by determining the total number of pages in the smartphone category. This is done by sending a request to the main category page, parsing the HTML, and extracting the maximum page number from the pagination.

### 2. **Extract Product Data**

The script then loops through each page of the product category. For each page:

* It sends an HTTP GET request to the page.
* It parses the page's HTML content using **BeautifulSoup**.
* It collects the product names (from the `<h3>` tags with the class `wd-entities-title`) and prices (from the `<span>` tags with the class `price`).
* The product prices are cleaned up by removing any unwanted characters (e.g., commas and currency symbols).

### 3. **Store the Data**

After scraping all pages, the script stores the product names and prices in a **Pandas DataFrame**. The DataFrame is then saved as an Excel file.

---

## Dependencies

This project requires the following Python libraries:

* **BeautifulSoup4**: For parsing HTML and extracting data from web pages.
* **Requests**: For sending HTTP requests and fetching webpage content.
* **Pandas**: For data handling and exporting the results to Excel.
* **TQDM**: For displaying progress bars during the scraping process.

To install all dependencies, use the following:

```bash
pip install -r requirements.txt
```

Or manually install using:

```bash
pip install beautifulsoup4 requests pandas tqdm openpyxl
```

---

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute this code.

---

