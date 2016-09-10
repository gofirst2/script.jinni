import os
import json
import sys
import xbmc
 
def log(msg, level=xbmc.LOGNOTICE):
	xbmc.log("[%s] %s" % ("script.jinni", msg.encode("utf-8")), level=level)

def getMoviesWith(*fields):
	params = {'properties':fields, 'sort':{'order':'ascending', 'method':'label', 'ignorearticle':True }}
	movies = executeJSON('VideoLibrary.GetMovies', params)
	return movies["result"]["movies"]

def executeJSON(method, params):
	data = json.dumps({'jsonrpc':'2.0', 'method':method, 'params':params, 'id':1})
	result = json.loads(xbmc.executeJSONRPC(data))
	if "error" in result:
		log("method: " + method + "params: " + str(params) + " throws: " + str(result["error"]))
		result = []
	return result

if __name__ == '__main__':
	id = sys.listitem.getVideoInfoTag().getIMDBNumber()
	found = []
	f = open(os.path.dirname(os.path.realpath(__file__)) + "/jinni-links", "r")
	while 1:
		s = f.readline()
		if s == "": break
		if s[0:9] == id:
			found = s[10:].split()
			break
	f.close()
	if len(found) == 0:
		xbmc.executebuiltin("Notification(Jinni, Nothing found)")
		sys.exit(0)

	xbmc.executebuiltin("Notification(Jinni, Writing playlist)")
	movies = getMoviesWith("imdbnumber", "title", "file")
	f = open(os.path.join(xbmc.translatePath("special://profile/playlists/video"), "Jinni.m3u"), "w")
	f.write("#EXTM3U\n")
	for x in found:
		id = x.split("=")[0]
		for m in movies:
			if m["imdbnumber"] == id:
				f.write("#EXTINF:0," + m["title"].encode("utf-8") + "\n")
				f.write(m["file"].encode("utf-8") + "\n")
	f.close()

	xbmc.executebuiltin("XBMC.ActivateWindow(Videos,special://profile/playlists/video/Jinni.m3u,return)")

