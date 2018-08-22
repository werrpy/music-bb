# music-bb
Discogs &amp; Spotify BBCode Formatter

Requirements  
Python 2 or 3
```
pip install discogs_client
pip install spotipy
```

Usage
```
python musicbb.py discogsid spotifyid
```

Sample Output
```
> python musicbb.py 1368437 5dj2UjtSxuKGlb17Bzu1mL
Title: Various - K.F. Presents Misc. And Björn Scheurmann Remixes
Tags: Electronic
Label: Glassnote Entertainment Group LLC
Name: Love Is Dead
Release Date: 2018-05-25
Images:
[center][img]https://img.discogs.com/AuqfWkXxKf4WqvFuICFtnkfyd3I=/fit-in/583x600/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-1368437-1218049494.jpeg.jpg[/img][/center]
[center][img]https://i.scdn.co/image/159e339c6cd980e4787e7d464079d822b19425be[/img][/center]
[center][img]https://i.scdn.co/image/7757d5799cf45c08c2a84f6ed942399080ea16d8[/img][/center]
[center][img]https://i.scdn.co/image/ea4bb5007473a22fbdcaeac7aea037b25ebedd2b[/img][/center]
Tracklist:
[list=1][*]1 Reggae Culture (Misc. Remix) 6:06[/*][*]2 Bongospace (Bjoern Scheurmann Remix) 7:00[/*][/list]
Spotify: [url=https://open.spotify.com/album/5dj2UjtSxuKGlb17Bzu1mL]https://open.spotify.com/album/5dj2UjtSxuKGlb17Bzu1mL[/url]
Discogs: [url=https://www.discogs.com/release/1368437]https://www.discogs.com/release/1368437[/url]
```

#### Discogs API
Generate a personal access token at https://www.discogs.com/settings/developers. Replace `user_token` and set a unique `user_agent` here: https://github.com/werrpy/music-bb/blob/master/musicbb.py#L55-L61
