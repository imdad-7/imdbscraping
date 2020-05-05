import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
soup = BeautifulSoup(page.content, 'html.parser')
movies_list = soup.find_all('tr')
movie_names = []
movie_year = []
movie_rating = []
for item in movies_list:
    if item.find(class_='titleColumn') is not None:
        movie = item.find(class_='titleColumn').find('a').get_text()
        movie_names.append(movie)
        year = item.find(class_='titleColumn').find('span').get_text()
        movie_year.append(year)
        rating = item.find(class_='ratingColumn imdbRating').find('strong').get_text()
        movie_rating.append(rating)

Top_250_rated_movies_by_users = pd.DataFrame({
    'IMDB Rating': movie_rating,
    'Movie Name': movie_names,
    'Year': movie_year,
})

Top_250_rated_movies_by_users.set_index('IMDB Rating', inplace=True)
print(Top_250_rated_movies_by_users)
# Top_250_rated_movies_by_users.to_csv('Top_250_movies_rated_by_users')

