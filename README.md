# script.jinni - a Kodi add-on to recommend simliar movies

![](icon.png)

This add-on adds an entry **Jinni** to the context menu for movies in your video library.

When selected, the add-on reads the included file **jinni-links** to get a list
of all movies similar to the highlighted one.

Then it writes a **Jinni.m3u** playlist containing those movies which are found
in your video library, and opens the playlist.

All of this happens locally and offline.

Note that matching is based entirely on IMDB ids.
