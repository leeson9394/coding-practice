import urllib
import urllib2
import httplib

conn = httplib.HTTPSConnection("www.python.org") #define connection 
conn.request("GET","/")  #Send GET request
res = conn.getresponse()  #Get reponse
print res.status, res.reason #print status code

url= 'http://www.google.com'

try:
	request=urllib2.Request(url)
	response=urllib2.urlopen(request)
	content=response.read()
except urllib2.URLError, e:
	print e.code
