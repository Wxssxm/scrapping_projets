import requests
import json
from bs4 import BeautifulSoup
import pandas as pd

# Récupère le contenu HTML d'une URL.
def fetch_page_content(url):

    response = requests.get(url)
    return BeautifulSoup(response.content, "html.parser")

# Extrait les cartes de projets à partir du contenu HTML.
def extract_project_cards(soup):
    
    return soup.find_all("div", class_="article-card card-our-project md-card")

# Extrait les données des projets à partir des cartes HTML.
def extract_project_data(cards):

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
    return data

#     Scrappe toutes les pages en suivant la pagination et retourne les données récupérées.
def scrape_all_pages(base_url):
    page = 1
    all_data = []

    while True:
        url = f"{base_url}?page={page}"
        soup = fetch_page_content(url)
        cards = extract_project_cards(soup)

        if not cards: 
            break

        all_data.extend(extract_project_data(cards))
        page += 1

    return all_data

# Sauvegarde les données dans un fichier JSON.
def save_to_json(data, file_path):

    json_data = json.dumps(data, indent=4, ensure_ascii=False)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(json_data)

# Sauvegarde les données dans un fichier CSV en utilisant Pandas.
def save_to_csv(data, file_path):

    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False, encoding="utf-8")

def main():
    base_url = "https://www.bpifrance.fr/nos-appels-a-projets-concours"
    data = scrape_all_pages(base_url)

    # Enregistrer les données dans un fichier JSON
    json_file_path = "appels_à_projets.json"
    save_to_json(data, json_file_path)

    # Enregistrer les données dans un fichier CSV
    csv_file_path = "appels_à_projets.csv"
    save_to_csv(data, csv_file_path)

if __name__ == "__main__":
    main()
