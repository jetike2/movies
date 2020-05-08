import json 

with open("movies.json","r") as f:
    data = json.load(f)
    for i in data["movies"]:
        if i["year"] == '':
            print(i)
