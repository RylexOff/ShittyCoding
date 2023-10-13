import requests
from bs4 import BeautifulSoup
import os
import re

def clean_folder_name(name):
    cleaned_name = re.sub(r'[<>:"/\\|?*\n]', '-', name)
    cleaned_name = cleaned_name.strip()
    return cleaned_name[:80]

URL = input("Veuillez entrer l'URL de la page web : ")

response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

div = soup.find('div', class_='vung-doc')
images = div.find_all('img')

div_info_top = soup.find('div', class_='info-top-chapter')
h2_content = ' '.join(div_info_top.find('h2').text.replace('\n', ' ').split()).strip()

folder_name = clean_folder_name(h2_content)

folder_increment = 1
while os.path.exists(folder_name):
    folder_name = f"{folder_increment}-{clean_folder_name(h2_content)}"
    folder_increment += 1

os.makedirs(folder_name)

with open(os.path.join(folder_name, 'Nom officiel.txt'), 'w', encoding='utf-8') as txt_file:
    txt_file.write(h2_content)
    txt_file.write('\n')
    txt_file.write('Source :')
    txt_file.write('\n')
    txt_file.write(URL)

for index, img in enumerate(images, start=1):
    img_url = img.get('src') or img.get('data-src')
    if img_url:
        extension = os.path.splitext(img_url)[1]
        img_name = f"page_{index}{extension}"
        
        img_data = requests.get(img_url).content
        with open(os.path.join(folder_name, img_name), 'wb') as handler:
            handler.write(img_data)

print("Téléchargement terminé!")
