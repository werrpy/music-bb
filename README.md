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
> python musicbb.py 12059367 5dj2UjtSxuKGlb17Bzu1mL
Title: CHVRCHES - Love Is Dead
Tags: Electronic, Pop
Label: Glassnote Entertainment Group LLC
Name: Love Is Dead
Release Date: 2018-05-25
Images:
[center][img]https://img.discogs.com/UGAqdJ1S1-1bXk6-a0fLl_VfBd8=/fit-in/600x532/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-12059367-1529417819-9960.jpeg.jpg[/img][/center]
[center][img]https://img.discogs.com/0raMOddBkyMYvNw8cLGW59eFjqc=/fit-in/600x533/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-12059367-1529417820-9665.jpeg.jpg[/img][/center]
[center][img]https://img.discogs.com/DB5hEEUKVCb44sWm2tLM_n1RWVs=/fit-in/600x510/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-12059367-1529417820-4941.jpeg.jpg[/img][/center]
[center][img]https://img.discogs.com/HraiOyoJlydZif3dN71OC3iIoqc=/fit-in/600x24/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-12059367-1529417819-7076.jpeg.jpg[/img][/center]
[center][img]https://img.discogs.com/77lF4zL0rjZd29qxXmUpPeZHzrY=/fit-in/600x531/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-12059367-1529417819-4120.jpeg.jpg[/img][/center]
[center][img]https://img.discogs.com/tEd2BQiF6C-XhStHhbObag6cs1Q=/fit-in/600x593/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-12059367-1529417819-9665.jpeg.jpg[/img][/center]
[center][img]https://img.discogs.com/ypFfiUhBuIpZuTtTamUqcVwLxDA=/fit-in/600x602/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-12059367-1529417819-8918.jpeg.jpg[/img][/center]
[center][img]https://img.discogs.com/qVUvzqkCBJIfgdqafS6r7yzZBHg=/fit-in/546x544/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-12059367-1529417818-9070.jpeg.jpg[/img][/center]
[center][img]https://img.discogs.com/E3400fizGnt-BNBjgIzW0CzhuqM=/fit-in/600x420/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-12059367-1529417819-4646.jpeg.jpg[/img][/center]
[center][img]https://i.scdn.co/image/159e339c6cd980e4787e7d464079d822b19425be[/img][/center]
[center][img]https://i.scdn.co/image/7757d5799cf45c08c2a84f6ed942399080ea16d8[/img][/center]
[center][img]https://i.scdn.co/image/ea4bb5007473a22fbdcaeac7aea037b25ebedd2b[/img][/center]
Tracklist:
[list=1][*]1 Graffiti 3:39[/*][*]2 Get Out 3:51[/*][*]3 Deliverance 4:13[/*][*]4 My Enemy 3:53[/*][*]5 Forever 3:44[/*][*]6 Never Say Die 4:24[/*][*]7 Miracle 3:08[/*][*]8 Graves 4:44[/*][*]9 Heaven/Hell 5:06[/*][*]10 God's Plan 3:32[/*][*]11 Really Gone 3:12[/*][*]12 ii 1:09[/*][*]13 Wonderland 4:36[/*][/list]
Spotify: [url=https://open.spotify.com/album/5dj2UjtSxuKGlb17Bzu1mL]https://open.spotify.com/album/5dj2UjtSxuKGlb17Bzu1mL[/url]
Discogs: [url=https://www.discogs.com/release/12059367]https://www.discogs.com/release/12059367[/url]
```

### Discogs API
Generate a personal access token at https://www.discogs.com/settings/developers. Replace `user_token` and set a unique `user_agent` here: https://github.com/werrpy/music-bb/blob/master/musicbb.py#L55-L61

### Spotify API
Create a client id at https://developer.spotify.com/dashboard/applications. Replace `client_id` and `client_secret` here: https://github.com/werrpy/music-bb/blob/master/musicbb.py#L66-L68

If you want to use Spotify's tracklist instead of Discogs', change https://github.com/werrpy/music-bb/blob/master/musicbb.py#L117-L120
