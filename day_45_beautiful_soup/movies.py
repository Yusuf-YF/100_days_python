import requests
from bs4 import BeautifulSoup

URL = "https://www.theguardian.com/film/2019/sep/13/100-best-films-movies-of-the-21st-century"

response = requests.get(URL)

website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h2", class_="")

title = [movie.getText() for movie in all_movies]

with open("top_movies.txt", mode="w") as file:
    for num in range(0, len(title) + 2, 2):
        movies = f"{title[num]}: {title[num + 1]}.\n"
        file.write(movies)
