#LetMEStalkMyServer
from win10toast import ToastNotifier
import os
import socket
import time
from datetime import datetime
from mcstatus import JavaServer

def check_server(ip, port):
    try:
        sock = socket.create_connection((ip, port), timeout=5)
        sock.close()
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False

def get_online_players(ip, port):
    server = JavaServer.lookup(f"{ip}:{port}")
    try:
        status = server.status()
        return status.players.online, status.players.sample
    except:
        return 0, None  # Retourne None en cas d'erreur

def log_connection(ip, player_name, server_name, connection_type):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a") as log_file:
        log_file.write(f"{timestamp} {connection_type} sur {server_name} ({ip}) Player : {player_name}\n")


server_nicknames = {
    "192.168.12.12": "My Server Minecraft",
    "192.168.12.11": "My Server Minecraft",
    "192.168.12.11": "My Server Minecraft",
    #Add ip and nickname Here
}

toaster = ToastNotifier()
player_set = set()

while True:
    for server in server_nicknames:
        ip = server
        server_name = server_nicknames[server]
        port = 25565

        if check_server(ip, port):
            online_players_count, online_players = get_online_players(ip, port)
            if online_players is not None: 
                for player in online_players:
                    if player.name not in player_set:
                        player_set.add(player.name)
                        toaster.show_toast(
                            "Serveur Minecraft",
                            f" {datetime.now().strftime('%Y-%m-%d | %H:%M:%S')}  Une nouvelle connexion sur {server_name} ({ip}) Player : {player.name}",
                            duration=5
                        )
                        log_connection(ip, player.name, server_name, "Connexion")
        else:
            if server_name in player_set:
                player_set.remove(server_name)
                log_connection(ip, "", server_name, "Déconnexion")
                print(f"Le serveur {server_name} ({ip}:{port}) n'est pas en ligne.")

    time.sleep(300)