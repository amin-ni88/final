import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('imdb_movies.csv')

#14
for year in year_average_budgets.index:
    year_movies = df.loc[df['year'] == year]
    most_profitable_movie = year_movies.loc[year_movies['profit'] == year_movies['profit'].max()]
    print(f"year {year}:")
    print(f" year_average_budgets: {most_profitable_movie['title'].values[0]} "
          f"({most_profitable_movie['profit'].values[0]} Dollers)")

#15
production_companies = df['production_companies'].str.split(',').str.get(0)
company_counts = production_companies.value_counts()
most_productive_company = company_counts.index[company_counts.argmax()]
print(f"Max_product: {most_productive_company}")

#16
top_5_by_votes = df.sort_values('vote_count', ascending=False).head(5)
for i in range(5):
    print(f"{i + 1}. {top_5_by_votes['title'].values[i]} ({top_5_by_votes['vote_count'].values[i]} vote)")

#17
top_5_by_rating = df.sort_values('vote_average', ascending=False).head(5)
for i in range(5):
    print(f"{i + 1}. {top_5_by_rating['title'].values[i]} ({top_5_by_rating['vote_average'].values[i]} rating)")

