#!/usr/bin/env python
# coding: utf-8

# In[1]:


import spotipy
from spotipy.oauth2 import SpotifyOAuth


# In[2]:

class SpotifyAPI:
    def __init__(self, client_id, client_secret, redirect_uri):
        """
        initializing the spotify api client
        """
        self.auth_manager = SpotifyOAuth(
			client_id=client_id, 
			client_secret=client_secret,
			redirect_uri=redirect_uri,
	        scope="playlist-read-private playlist-read-collaborative"
			)				
        self.sp = spotipy.Spotify(auth_manager=self.auth_manager)

		# In[4]:
    def playlist_tracks(self, playlist_id):
        """
        retrieve tracks in a playlist
        """
        results = self.sp.playlist_tracks(playlist_id, market="US")
        tracks = results["items"]
        # fetch additional tracks if playlist has more - pagination
        while results["next"]:
        	results = self.sp.next(results)
        	tracks.extend(results["items"])
        return tracks
			
			
		# In[3]:		
    def get_track(self, track_id):
    	"""
    	retrieve track details by track id		
    	"""
    	return self.sp.track(track_id)
			
						
		# In[6]:		
    def get_artist(self, artist_id):
    	"""
    	retrieve artist details by artist id
    	"""
    	return self.sp.artist(artist_id)

