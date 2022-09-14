import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
# print(soup.prettify())

titles = soup.find_all("h3", class_="title")

top_100 = [title_tag.getText() for title_tag in titles]
top_100_in_order = top_100[::-1]

with open("top-100-movies.txt", mode="w") as file:
    for movie in top_100_in_order:
        file.write(f"{movie}\n")