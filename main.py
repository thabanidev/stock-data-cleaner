import pandas as pd
from newsGetter import get_news
from sentimentAnalysis import get_sentiment


PG = pd.read_csv('PG.csv', parse_dates=True)
PG['Date'] = pd.to_datetime(PG['Date'], format='%Y-%m-%d')
print(PG["Date"].head(100))
print(PG.head(100))

# Drop the rows where the column 'opening' is equal to 0.0
PG = PG[PG["Open"] != 0.0]
print(PG.head(100))

PG['news'] = PG['Date'].apply(get_news)
PG["sentiment"] = PG["news"].apply(get_sentiment)

print(PG.head(50))