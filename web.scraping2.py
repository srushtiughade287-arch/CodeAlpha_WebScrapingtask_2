import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_1samp

# -------------------- Web Scraping --------------------

url = "https://quotes.toscrape.com/"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

data = []

for quote_block in soup.find_all("div", class_="quote"):
    quote = quote_block.find("span", class_="text").get_text(strip=True)
    author = quote_block.find("small", class_="author").get_text(strip=True)

    tags = [tag.get_text(strip=True) for tag in quote_block.find_all("a", class_="tag")]
    domain = ", ".join(tags)

    data.append({
        "Quote": quote,
        "Author": author,
        "Domain": domain
    })

# -------------------- DataFrame --------------------

df = pd.DataFrame(data)

df.to_csv("quotes_dataset.csv", index=False)

print("\nDataset")
print(df)

# -------------------- EDA --------------------

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Records")
print(df.duplicated().sum())

print("\nDataset Info")
df.info()

print("\nTop Authors")
print(df["Author"].value_counts())

print("\nTop Domains")
print(df["Domain"].value_counts())

# Quote Length
df["Quote_Length"] = df["Quote"].str.len()

print("\nQuote Length Statistics")
print(df["Quote_Length"].describe())

# -------------------- Data Quality Checks --------------------

print("\n================ Data Quality Checks ================")

# Missing Values
print("\n1. Missing Values:")
print(df.isnull().sum())

# Duplicate Records
print("\n2. Duplicate Records:")
print(df.duplicated().sum())

# Empty Quotes
empty_quotes = (df["Quote"].str.strip() == "").sum()
print("\n3. Empty Quotes:", empty_quotes)

# Empty Authors
empty_authors = (df["Author"].str.strip() == "").sum()
print("4. Empty Authors:", empty_authors)

# Empty Domains
empty_domains = (df["Domain"].str.strip() == "").sum()
print("5. Empty Domains:", empty_domains)

# Very Short Quotes (<20 characters)
short_quotes = (df["Quote_Length"] < 20).sum()
print("6. Very Short Quotes (<20 chars):", short_quotes)

# Unique Authors
print("\n7. Number of Unique Authors:", df["Author"].nunique())

# Unique Domains
print("8. Number of Unique Domains:", df["Domain"].nunique())

# -------------------- Hypothesis Testing --------------------

print("\n================ Hypothesis Testing ================")

# H0: Mean Quote Length = 100
# H1: Mean Quote Length ≠ 100

t_stat, p_value = ttest_1samp(df["Quote_Length"], popmean=100)

print(f"T-Statistic : {t_stat:.3f}")
print(f"P-Value     : {p_value:.5f}")

alpha = 0.05

if p_value < alpha:
    print("\nDecision : Reject the Null Hypothesis (H0)")
    print("Conclusion : Average quote length is significantly different from 100.")
else:
    print("\nDecision : Fail to Reject the Null Hypothesis (H0)")
    print("Conclusion : Average quote length is NOT significantly different from 100.")

# -------------------- Visualization --------------------

# Bar Chart - Top Authors
plt.figure(figsize=(8,5))
df["Author"].value_counts().plot(kind="bar", color="skyblue")
plt.title("Top Authors")
plt.xlabel("Author")
plt.ylabel("Number of Quotes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Histogram - Quote Length
plt.figure(figsize=(8,5))
plt.hist(df["Quote_Length"], bins=10, color="orange", edgecolor="black")
plt.title("Distribution of Quote Length")
plt.xlabel("Quote Length")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()