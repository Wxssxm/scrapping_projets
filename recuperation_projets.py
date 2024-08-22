import requests
import json
from bs4 import BeautifulSoup

url = "https://www.bpifrance.fr/nos-appels-a-projets-concours"

requete = requests.get(url)

soup = BeautifulSoup(requete.content, "html.parser")

cards = soup.find_all("div", class_="article-card card-our-project md-card")

data = []

for card in cards:
    title = card.find("h3").text.strip()
    link = "https://www.bpifrance.fr" + card.find("a", href=True)["href"]
    description = card.find("p").text.strip()
    date_range = card.find("span", class_="card-date").text.strip()

    data.append({
        "titre": title,
        "lien": link,
        "description": description,
        "date_range": date_range
    })

json_data = json.dumps(data, indent=4, ensure_ascii=False)

print(json_data)

file_path = "projets_recuperés.json"

with open(file_path, "w", encoding="utf-8") as file:
    file.write(json_data)