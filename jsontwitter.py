import urllib2
import json
import twitter

CONSUMER_KEY ="oz3AezIShZYmQPg656DtnMpbS"
CONSUMER_SECRET = "BM9dvFCImHpHw1JBmA4YCxKKEFD7dPfxI2BUtprB7e6CXLFfF9"
ACCESS_KEY = "3092945518-BWFv6uyTxOGBMM6v2k77FTDER5cUiEMWsf41jv1" 
ACCESS_SECRET = "hiRBJPrSLsSL9LRQD6XKkBobotwfTbsLH2nGTa3EdEawD"
auth = twitter.OAuth(ACCESS_KEY, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
t = twitter.Twitter(auth=auth)
usuario = raw_input("Nombre de usuario deseado: ")
numero = raw_input("Cantidad de tweets: ")
userid = t.users.show(screen_name=usuario)['id'] #Consigue la id del usuario que elegimos
datos = t.statuses.user_timeline(user_id=userid, count=numero) #Escoge los tweets del usuario elegido y la cantidad de tweets

for tweet in datos:
	print tweet['text'] 
