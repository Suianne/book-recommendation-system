import pandas as pd

books = pd.read_csv('./goodbooks-10k/books.csv')
ratings = pd.read_csv('./goodbooks-10k/ratings.csv')

print(books.head())
print(ratings.head())
print(ratings.isnull().sum())
print(books.isnull().sum())

user_counts = ratings['user_id'].value_counts()
ratings = ratings[ratings['user_id'].isin(user_counts[user_counts >= 10].index)]

