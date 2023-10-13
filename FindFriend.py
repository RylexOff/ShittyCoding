import shodan
import subprocess

# place your  api key here
SHODAN_API_KEY = ''

api = shodan.Shodan(SHODAN_API_KEY)

countries = [
    {"code": "JP", "name": "Japon"},
    {"code": "KR", "name": "Corée du Sud"},
    {"code": "US", "name": "États-Unis"},
    {"code": "BR", "name": "Brésil",},
    {"code": "DE", "name": "Allemagne"},
    {"code": "FR", "name": "France"},
    {"code": "RU", "name": "Russie"},
    {"code": "GB", "name": "Royaume-Uni"},
    {"code": "IT", "name": "Italie"},
    {"code": "TR", "name": "Turquie"}
]

print("Sélectionnez le pays ciblé:")
for index, country in enumerate(countries, start=1):
    print(f"{index}. {country['name']}")
choice = input("Entrez le chiffre correspondant au pays : ")

if choice.isdigit() and 1 <= int(choice) <= len(countries):
    selected_country = countries[int(choice) - 1]['code']
    query = f'product:"Minecraft Server" country:"{selected_country}" players:[1 TO *]'
    
    try:
        results = api.search(query)

        for result in results['matches']:
            ip = result['ip_str']
            name = result.get('data', {}).get('hostname', 'N/A')
            players_online = result.get('data', {}).get('players', {}).get('online', 'N/A')
            max_players = result.get('data', {}).get('players', {}).get('max', 'N/A')
            description = result.get('data', {}).get('description', 'N/A')
            whitelist = result.get('data', {}).get('whitelist', 'Non disponible')

            separator = "-" * (len(name) + 4)

            print(separator)
            print(f"[{name}]")
            print(f"IP: {ip}")
            print(f"Description: {description}")
            print(f"Joueurs en ligne: {players_online}/{max_players}")
            print(f"Liste blanche: {whitelist}")
            print(separator)
            
            ping_choice = input("Voulez-vous effectuer un ping pour vérifier les informations (oui/non) ? ")
            
            if ping_choice.lower() == "oui":
                response = subprocess.call(["ping", "-c", "3", ip])  # Remplacez par "ping" pour Windows
                if response == 0:
                    print("Le serveur est en ligne et répond au ping.")
                    
                    # Vérifier si des joueurs sont en ligne
                    if players_online != 'N/A' and int(players_online) > 0:
                        print(f"Il y a {players_online} joueurs en ligne sur le serveur.")
                    else:
                        print("Aucun joueur en ligne sur le serveur.")
                else:
                    print("Le serveur est hors ligne ou ne répond pas au ping.")
            
            print()

    except shodan.APIError as e:
        print('Erreur Shodan:', e)
else:
    print("Choix invalide. Veuillez entrer un chiffre valide.")

____________________________________________________________