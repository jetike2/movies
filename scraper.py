from bs4 import BeautifulSoup as bs
from requests import get
import json

movies = {}
movies["movies"] = []

def movie(genre):
    ind = 1
    for i in range(10):
        url = "https://www.imdb.com/search/title/?genres={0}&start={1}&explore=title_type,genres&ref_=adv_nxt".format(genre,ind)
        response = get(url)
        html_soup = bs(response.text, "html.parser")
        movie = html_soup.find_all("div",class_="lister-item-content")
        type(html_soup)
        for j in range(len(movie)):
            title = movie[j].find("a")
            rating = movie[j].find(class_="inline-block ratings-imdb-rating")
            year = movie[j].find(class_="lister-item-year text-muted unbold")
            link = "https://www.imdb.com" + title["href"]
            if rating is not None:
                year_num = []
                for k in year.text:
                    if k.isdigit():
                        year_num.append(k)
                s = ""
                s = s.join(year_num[:4])
                movie_dict = {
                        "tilte":    title.text,
                        "rating": rating["data-value"],
                        "year": s,
                        "genre": genre,
                        "link": link
                        }

                movies["movies"].append(movie_dict)


        ind += 50
        print(ind)
    with open("movies.json", "w") as f:
        data = json.dumps(movies, ensure_ascii=False, indent=True)
        f.write(data)

genres = ["comedy", "sci-fi", "horror", "romance", "action", "thriller", "drama", "mystery", "crime","animation", "adventure", "fantasy"]

for i in genres:
    movie(i)
print("finnished: " + str(len(movies["movies"])))
