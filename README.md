# CodeAlpha_WebScrapingtask_2
Conducted Exploratory Data Analysis (EDA) to examine data structure, identify patterns and anomalies, validate assumptions, and detect data quality issues using statistical analysis and visualizations


# Ask meaningful questions
1. What is the total number of quotes in the dataset?
2. How many unique authors are represented?
3. Which author has contributed the most quotes?
4. Are there any missing values in the Quote or Author columns?
5. Are there any duplicate quotes or duplicate records?
5.5What is the average length of a quote?
7. Which quote is the longest and which is the shortest?
8. Do some authors tend to have longer quotes than others?
9. Is the distribution of quotes balanced across authors, or are a few authors dominating the dataset?
10. Are there any unusual characters, formatting issues, or inconsistencies in the text data?
11. What themes or topics appear most frequently in the quotes?
12.Is the dataset suitable for further text analysis, sentiment analysis, or visualization?

## Explore the Data Structure

The dataset was created by scraping quotes from the Quotes to Scrape website. It contains three variables:

* **Quote**: The text of the quote.
* **Author**: The name of the author.
* **Domain**: Tags/categories associated with the quote.

All three variables are stored as text data (`object` type). The dataset contains 10 records and 3 columns with no missing values. This structure makes the dataset suitable for text analysis, author-based analysis, and category-based exploration.


## Trends, Patterns, and Anomalies

### Trends
- Inspirational and life-related quotes appear frequently.
- Some authors contribute multiple quotes.
- Certain domains/tags are more common than others.

### Patterns
- Each quote is associated with an author and one or more domains.
- All variables are text-based.

### Anomalies
- No missing values were found.
- Duplicate records were checked.
- Quote lengths vary, with some quotes significantly longer than others.
