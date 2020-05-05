import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://www.imdb.com/search/title/?release_date=2017-01-01,2017-12-31&sort=num_votes,desc&ref_=adv_prv')
soup = BeautifulSoup(page.content, 'html.parser')
# movie_containers = soup.find(class_='lister-list')
# print(movie_containers.find('div', class_='lister-item-content').find('a').get_text())
movie_containers = soup.find_all(class_='lister-item mode-advanced')

names = []
years = []
imdb_ratings = []
metascores = []
votes = []
for item in movie_containers:
    name = item.find(class_='lister-item-content').find('a').get_text()
    names.append(name)
    year = item.find(class_='lister-item-year text-muted unbold').get_text()
    years.append(year)
    rating = item.find(class_='inline-block ratings-imdb-rating').find('strong').get_text()
    imdb_ratings.append(rating)
    vote = item.find('span', attrs={'name': 'nv'})['data-value']
    votes.append(vote)
    if item.find(class_='inline-block ratings-metascore') is not None:
        for s in item.find(class_='inline-block ratings-metascore').get_text().split():
            if s.isdigit():
                metascores.append(s)
    else:
        metascores.append('NA')


Movie_rating_imdb_votes = pd.DataFrame({
    'IMDB Rating': imdb_ratings,
    'Meta Score': metascores,
    'Movie Name': names,
    'Votes': votes,
    'year': years
})
print(Movie_rating_imdb_votes)
