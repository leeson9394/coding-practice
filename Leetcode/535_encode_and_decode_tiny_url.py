# 535. https://leetcode.com/problems/encode-and-decode-tinyurl/

from collections import defaultdict
import random, string

class Codec:
    codeDB, urlDB = defaultdict(), defaultdict()
    chars = string.ascii_letters + string.digits

    def getCode(self) -> str:
        # code = ''.join(random.choice(self.chars) for i in range(6))
        code_list = []
        for i in range(6):
            code_list.append(random.choice(self.chars))
        code = ''.join(code_list)
        return "http://tinyurl.com/" + code
 
    def encode(self, longUrl: str) -> str:
        if longUrl in self.urlDB: 
            return self.urlDB[longUrl]
        shortUrl = self.getCode()
        self.codeDB[shortUrl] = longUrl
        self.urlDB[longUrl] = shortUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        return self.codeDB[shortUrl]
    
    print(codeDB)

# Your Codec object will be instantiated and called as such:
url = "https://www.google.com/search?q=import+random+python&sxsrf=APq-WBvj-TYhyTcvTI0BDNWuqVgrZ7z7FA%3A1647414174831&ei=nosxYuOxMp3a0PEPhuC4-AE&oq=import+r&gs_lcp=Cgdnd3Mtd2l6EAMYADIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBMgcIABAKEMsBMgUIABDLAToECCMQJzoECAAQQzoFCAAQgAQ6BggjECcQE0oECEEYAEoECEYYAFAAWJEHYPcRaABwAXgAgAFciAHeBJIBATiYAQCgAQHAAQE&sclient=gws-wiz"
codec = Codec()
shortURL = codec.encode(url)
longURL = codec.decode(shortURL)
print(shortURL)
