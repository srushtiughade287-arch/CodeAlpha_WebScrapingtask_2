import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

data = []

for quote_block in soup.find_all("div", class_="quote"):
    quote = quote_block.find("span", class_="text").text
    author = quote_block.find("small", class_="author").text

    tags = [tag.text for tag in quote_block.find_all("a", class_="tag")]
    domain = ", ".join(tags)

    data.append({
        "Quote": quote,
        "Author": author,
        "Domain": domain
    })

df = pd.DataFrame(data)

print(df)

df.to_csv("quotes_dataset.csv", index=False)

print("Dataset saved successfully!")
