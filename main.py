import requests
from bs4 import BeautifulSoup
import pandas as pd


def extract_data_from_listing(listing):
    price = listing.find("span", {"class": "homecardV2Price"}).get_text(strip=True)
    address = listing.find("span", {"class": "collapsedAddress"}).get_text(strip=True)
    stats = listing.find_all("div", {"class": "stats"})
    try:
        bed_count_elem, bath_count_elem, size_elem = stats[0], stats[1], stats[2]
    except IndexError:
        raise Exception("Got less stats than expected")

    bed_count = bed_count_elem.get_text(strip=True)
    bath_count = bath_count_elem.get_text(strip=True)
    size = size_elem.get_text(strip=True)

    return {
        "price": price,
        "address": address,
        "bed_count": bed_count,
        "bath_count": bath_count,
        "size": size,
    }


USERNAME = "USERNAME"
PASSWORD = "PASSWORD"

payload = {
    "source": "universal",
    "url": "https://www.redfin.com/city/29470/IL/Chicago",
}

response = requests.post(
    "https://realtime.oxylabs.io/v1/queries",
    auth=(USERNAME, PASSWORD),
    json=payload,
)
response.raise_for_status()

html = response.json()["results"][0]["content"]
soup = BeautifulSoup(html, "html.parser")

data = []

for listing in soup.find_all("div", {"class": "bottomV2"}):
    entry = extract_data_from_listing(listing)
    data.append(entry)


df = pd.DataFrame(data)
df.to_csv("real_estate_data.csv")
