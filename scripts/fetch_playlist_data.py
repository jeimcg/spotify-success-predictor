#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
print(sys.path)


# In[ ]:


import sys
import os
## setting relative path to folder
script_path = os.path.abspath("../scripts")
sys.path.append(script_path)


# In[ ]:


print(os.listdir("../scripts"))


# In[1]:


import os
from spotify_api import SpotifyAPI
from data_utils import save_json


# In[ ]:


# defining credentials
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

#initialize spotify api client
spotify = SpotifyAPI(CLIENT_ID, CLIENT_SECRET)

def fetch_playlist(playlist_id, save_path):
    """
    Fetch tracks from a playlist and save to a JSON file
    """
    print(f"Fetching tracks from playlist: {playlist_id}")
    tracks = spotify.get_playlist_tracks(playlist_id)
    save_json(tracks, save_path)
    print(f"Saved {len(tracks)} tracks to {save_path}")

if __name__ == "__main__":
    # enter playlist id
    playlist_id = ""
    save_path = "../data/raw/playlist_tracks.json"

fetch_playlist(playlist_id, save_path)

