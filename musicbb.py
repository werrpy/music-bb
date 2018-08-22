import discogs_client
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import argparse

class BBCode:
  def link(self, url):
    return '[url=' + str(url) + ']' + str(url) + '[/url]'

  def image(self, url):
    return '[center][img]' + str(url) + '[/img][/center]'

  def tracklist_discogs(self, list):
    bbcode = '[list=1]'
    for track in list:
      if not track.position and not track.title and not track.duration:
        break
      bbcode += '[*]'
      if track.position:
        bbcode += track.position
      if track.title:
        bbcode += ' ' + track.title
      if track.duration:
        bbcode += ' ' + track.duration
      bbcode += '[/*]'
    bbcode += '[/list]'
    return bbcode
    
  def tracklist_spotify(self, list):
    bbcode = '[list=1]'
    for track in list:
      if not 'track_number' in track and not 'name' in track and not 'duration_ms' in track:
        break
      bbcode += '[*]'
      if 'track_number' in track:
        bbcode += str(track['track_number'])
      if 'name' in track:
        bbcode += ' ' + track['name']
      if 'duration_ms' in track:
        millis = int(track['duration_ms'])
        seconds = str(int((millis / 1000) % 60))
        minutes = str(int((millis / (1000 * 60)) % 60))
        hours = int((millis/(1000 * 60 * 60)) % 24)

        duration = ''
        if hours is not 0:
          duration += str(hours) + ':'
        duration = '{0}{1}:{2}'.format(duration, minutes.zfill(2), seconds.zfill(2))

      bbcode += ' ' + duration + '[/*]'
    bbcode += '[/list]'
    return bbcode

# Discogs personal access token
# https://www.discogs.com/settings/developers
discogs_user_token = 'NFHgaaPhqdTByXxfjSEWpIBtXAGgnRcNnhnoMzqh'

# A user-agent is required with Discogs API requests. Be sure to make your user-agent
# unique, or you may get a bad response.
discogs_user_agent = 'MusicBBCode/1.0'

# Authenticate
d = discogs_client.Client(discogs_user_agent, user_token=discogs_user_token)

# https://developer.spotify.com/dashboard/applications
spotify_client_id = '1da5c5eb87144ca3a8afeca6a9d9b7cb'
spotify_client_secret = 'caee448f0fbb48188d5909ede63250e7'

# Authenticate
spotify_client_credentials_manager = SpotifyClientCredentials(spotify_client_id, spotify_client_secret)
sp = spotipy.Spotify(client_credentials_manager=spotify_client_credentials_manager)

# Parse arguments
parser = argparse.ArgumentParser(description='Discogs API')
parser.add_argument('discogs', type=int, help='Discogs ID')
parser.add_argument('spotify', type=str, help='Spotify Album ID')
args = parser.parse_args()

# Discogs ID = args.discogs
discogs_release = d.release(args.discogs)

# Spotify Album ID = args.spotify
spotify_results = sp.album(args.spotify)

# comma seperated artists
artists = ', '.join(str(artist.name) for artist in discogs_release.artists)

# artists - title
title = artists + ' - ' + discogs_release.title
print('Title: ' + title)

# comma seperated genres
tags = ', '.join(discogs_release.genres)
print('Tags: ' + tags)

print('Label: ' + spotify_results['label'])
print('Name: ' + spotify_results['name'])
print('Release Date: ' + spotify_results['release_date'])

# BBCode formatter
bb = BBCode()

# images
print('Images: ')

# Discogs images
if discogs_release.images is not None:
  for img in discogs_release.images:
    print(bb.image(img['uri']))

# Spotify images
if spotify_results['images'] is not None:
  for img in spotify_results['images']:
    print(bb.image(img['url']))

# tracklist
print('Tracklist:')
print(bb.tracklist_discogs(discogs_release.tracklist))
#print(bb.tracklist_spotify(spotify_results['tracks']['items']))

# Spotify urls
for k, v in spotify_results['external_urls'].items():
  print(k.capitalize() + ': ' + bb.link(v))

# Discogs url
print('Discogs: ' + bb.link('https://www.discogs.com/release/' + str(args.discogs)))
