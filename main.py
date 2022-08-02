# from bs4 import BeautifulSoup
# import requests
#
# URL = "https://www.billboard.com/charts/hot-100/"
# CLIENT_ID = "___"
# CLIENT_SECRET = "___"
#
# date = input("Which year do you want to travel to? Type a date in a format YYYY-MM-DD: ")
# # print(date)
#
# response = requests.get(URL + date)
#
# soup = BeautifulSoup(response.text, "html.parser")
# song_names_h3 = soup.findAll("h3", class_="a-no-trucate")
# song_names = [song.getText().strip('\t\n') for song in song_names_h3]
# print(song_names)

# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
#
# sp = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#         scope="playlist-modify-private",
#         redirect_uri="http://example.com",
#         client_id=CLIENT_ID,
#         client_secret=CLIENT_SECRET,
#         show_dialog=True,
#         cache_path="token.txt"
#     )
# )
# user_id = sp.current_user()["id"]

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint

# =============== Top 100 Billboard Web scraping =========
URL_billboard = "https://www.billboard.com/charts/hot-100/"

date = input("What year do you want to travel to? Type the date in this format, YYYY-MM-DD: ")
year = date[:4]

response = requests.get(f"{URL_billboard}{date}/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

scraped = [song.getText().strip("\n") for song in soup.find_all(name="h3", class_="c-title", id="title-of-a-story")][5:]

scraped_art = [artist.getText().strip("\n") for artist in soup.find_all(name="span", class_="c-label")]

song_names = [name.replace("'", "").replace("!", "") for name in scraped
              if 'Songwriter(s):' not in name
              if 'Producer(s):' not in name
              if 'Imprint/Promotion Label:' not in name
              if 'Additional Awards' not in name
              ][:100]

artist_names = [artist.split(" Featuring")[0].split(" Duet")[0].replace("Ke$ha", "Kesha") for artist in scraped_art
                if not artist.isnumeric()
                if artist != "-"
                if artist != "NEW"
                if 'ENTRY' not in artist
                ]

# # ==================== Spotify API =======================

spotify_client_id = "CLIENT_ID_TO_BE_USE"
spotify_client_secret = "CLIENT_SECRET_TO_BE_USE"
redirect = "http://example.com"


spotify_auth = spotipy.oauth2.SpotifyOAuth(client_id=spotify_client_id,
                                           client_secret=spotify_client_secret,
                                           redirect_uri=redirect,
                                           scope="playlist-modify-private",
                                           cache_path="token.txt")

# spotify.get_access_token()

sp = spotipy.Spotify(oauth_manager=spotify_auth)

user_name = sp.current_user()["display_name"]
user_id = sp.current_user()["id"]

song_urls = []
for song, artist in zip(song_names, artist_names):
    items = sp.search(q=f"track: {song} artist: {artist}", type="track")["tracks"]["items"]
    if len(items) > 0:
        song_urls.append(items[0]["uri"])

playlist_id = sp.user_playlist_create(user=user_id, name=f"{date} Top 100 Popular", public=False)["id"]

sp.playlist_add_items(playlist_id=playlist_id, items=song_urls)
