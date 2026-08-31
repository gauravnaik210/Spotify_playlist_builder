# Spotify Playlist Builder

This project scrapes the Billboard Hot 100 for a selected date and creates a private Spotify playlist from the matching tracks.

## Overview

The script does two main tasks:

1. Fetches the Billboard Hot 100 page for a chosen date.
2. Searches Spotify for each track and adds the matching songs to a new private playlist.

This makes it easy to recreate a playlist for a specific year or chart date.

## How the code works

### 1) Billboard scraping
The script uses BeautifulSoup to parse the Billboard page and extract:

- song titles
- artist names

It filters out unwanted labels and keeps only the track list from the selected chart date.

### 2) Spotify authentication
The script uses `spotipy` and `SpotifyOAuth` to authenticate the user.

It reads secrets from environment variables instead of hardcoding them into the source file, and it keeps the token in memory for the current session instead of saving it to a tracked token file.

### 3) Matching songs in Spotify
For each scraped track, it runs a Spotify search query like:

```python
sp.search(q=f"track: {song} artist: {artist}", type="track")
```

If a match exists, it stores the first matching Spotify track URI and adds it to the playlist.

### 4) Playlist creation
After matching the tracks, the script creates a new private playlist named like:

```text
YYYY-MM-DD Top 100 Popular
```

Then it adds the matched song URIs to the playlist.

## Setup

### 1) Install Python dependencies

```bash
pip install -r requirements.txt
```

### 2) Add Spotify API credentials
Create a `.env` file in the project folder with:

```env
SPOTIFY_CLIENT_ID=your_client_id_here
SPOTIFY_CLIENT_SECRET=your_client_secret_here
```

You can copy the example file:

```bash
copy .env.example .env
```

Then update the values with your real Spotify app credentials.

### 3) Run the script

```bash
python main.py
```

Then enter a date in this format:

```text
YYYY-MM-DD
```

Example:

```text
2010-08-14
```

## Project files

- `main.py` — main script for scraping Billboard and creating the Spotify playlist
- `.env.example` — template for local environment variables
- `.gitignore` — excludes sensitive and local files from Git
- `requirements.txt` — Python package requirements

## Security notes

Do not commit your real Spotify client ID, client secret, or auth tokens.

The project is configured to ignore:

- `.env`
- `token.txt`
- Python cache files
- `.venv` folders
- IDE config files

## Example usage

```text
What year do you want to travel to? Type the date in this format, YYYY-MM-DD: 2020-05-09
```

This will create a playlist based on the Billboard Hot 100 for that date.

## Recommended improvements

- Add retry logic for failed Spotify searches
- Add logging for songs that were not found
- Validate the HTML selectors against current Billboard markup
- Consider moving the playlist creation logic into functions for easier testing

## License

This project is for educational and personal use.
