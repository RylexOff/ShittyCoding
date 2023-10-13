# ShittyCoding Repository

Welcome to the "ShittyCoding" repository. Here, you'll find a collection of small, seemingly insignificant, yet functional scripts. There useless like me ='(

## Table of Contents

1. [Recuperateur.py](#recuperateurpy)
2. [FindFriend.py](#findfriendpy)
3. [NotifMinecraftServer.py](#notifminecraftserverpy)
4. [youtubeGrabChannelHistory.py](#youtubegrabchannelhistorypy)
5. [autoclick.py](#autoclickpy)

### Recuperateur.py

**Prerequisites:**
```bash
pip install requests beautifulsoup4
```
A script that downloads images from a specified web page. It prompts the user to input a URL and then retrieves all the images found within a specific div element. The images are saved in a folder with a name derived from an h2 element on the page.
A utility script useful for downloading manga scans.

### FindFriend.py

**Prerequisites:**
```bash
pip install shodan
```
This script uses the Shodan API to find and display information about Minecraft servers in various countries. It provides options to select a country, fetches Minecraft servers from that country, and allows the user to ping the servers to verify their status.

### NotifMinecraftServer.py

**Prerequisites:**
```bash
pip install win10toast mcstatus
```
Monitors specified Minecraft servers and sends a Windows toast notification whenever a new player connects to the server. It also logs the player's connection and disconnection events.

### youtubeGrabChannelHistory.py

**Prerequisites:**
```bash
pip install google-api-python-client tqdm
```
Fetches video details, including title, link, views, and likes, from a specific YouTube channel using the YouTube API. The user needs to input the channel ID, and the script will retrieve details of the most recent videos from that channel.

### autoclick.py

**Prerequisites:**
```bash
pip install pynput
```
A utility script useful for playing Cookie Clicker. A simple auto-clicker script that simulates mouse clicks. The auto-clicking can be toggled on and off using the "delete" key, and the script can be stopped using the "esc" key.
