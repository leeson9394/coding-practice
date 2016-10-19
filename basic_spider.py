import urllib
import urllib2

url= 'http://www.google.com'

try:
	request=urllib2.Request(url)
	response=urllib2.urlopen(request)
	content=response.read()
except urllib2.URLError, e:
	print e.code