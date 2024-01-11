# Scraping Real Estate Data With Python

[![Oxylabs promo code](https://user-images.githubusercontent.com/129506779/250792357-8289e25e-9c36-4dc0-a5e2-2706db797bb5.png)](https://oxylabs.go2cloud.org/aff_c?offer_id=7&aff_id=877&url_id=112)

In this guide, you’ll learn how to collect public property data from [Redfin](https://www.redfin.com/) with the help of Oxylabs [Real Estate Scraper API](https://oxylabs.io/products/scraper-api/real-estate) and Python. You can scrape real estate data like prices, sizes, number of beds and baths available, and addresses, increasing the likelihood of finding a good deal or understanding the market better. 

For the full guide, check our [blog post](https://oxylabs.io/blog/scraping-real-estate-data).

## 1. Prepare environment

```python
touch main.py
```

### Install dependencies

```python
pip install bs4 requests pandas
```

### Import libraries

```python
import requests
import pandas as pd
from bs4 import BeautifulSoup
```

## 2. Prepare the API request





