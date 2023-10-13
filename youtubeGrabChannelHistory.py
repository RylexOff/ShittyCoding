from googleapiclient.discovery import build
from datetime import datetime
import os
import html
from tqdm import tqdm

def fetch_channel_videos(api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    channel_id = input("Veuillez entrer l'ID de la chaîne YouTube : ")
    
    channel_request = youtube.channels().list(
        part="snippet",
        id=channel_id
    )
    
    channel_response = channel_request.execute()
    channel_name = channel_response['items'][0]['snippet']['title'] if channel_response['items'] else "Unknown_Channel"
    
    next_page_token = None
    current_date = datetime.now().strftime("%Y-%m-%d")
    output_file = f"Titre_video_de_{channel_name}_{current_date}.txt"
    
    if os.path.exists(output_file):
        os.remove(output_file)
    
    video_count = 0 
    max_videos = 100  # Max video grab 
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"=============================={channel_name}============================\n")
        
        pbar = tqdm(total=max_videos)
        
        while True:
            video_request = youtube.search().list(
                part="snippet",
                channelId=channel_id,
                maxResults=50,
                pageToken=next_page_token,
                order="date"
            )
            video_response = video_request.execute()
            
            for i, item in enumerate(video_response['items']):
                if item['id'].get('videoId'):
                    video_id = item['id']['videoId']
                    
                    stats_request = youtube.videos().list(
                        part="statistics",
                        id=video_id
                    )
                    stats_response = stats_request.execute()
                    stats = stats_response['items'][0]['statistics']
                    
                    video_title = item['snippet']['title']
                    video_title = html.unescape(video_title)
                    
                    video_count += 1
                    f.write(f"=================== VIDEO {video_count} ==================\n")
                    f.write(f"Nom de la video : {video_title}\n")
                    f.write(f"Lien : https://www.youtube.com/watch?v={video_id}\n")
                    f.write(f"Nombre de vues : {stats.get('viewCount', 'N/A')}\n")
                    f.write(f"Nombre de likes : {stats.get('likeCount', 'N/A')}\n")
                    
                    pbar.update(1)
                    
                    if video_count >= max_videos: 
                        break
            
            if video_count >= max_videos:  
                break
            
            next_page_token = video_response.get('nextPageToken')
            
            if not next_page_token:
                break
        
        pbar.close()
            
    print(f"Les détails des vidéos ont été enregistrés dans {output_file}")

if __name__ == "__main__":
# Api key here
    API_KEY = ""  # Api key here
    fetch_channel_videos(API_KEY)