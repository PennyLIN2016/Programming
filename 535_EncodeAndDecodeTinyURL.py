class Codec:
    #Runtime: 20 ms, faster than 70.81% of Python online submissions for Encode and Decode TinyURL.
    #Memory Usage: 11.8 MB, less than 35.71% of Python online submissions for Encode and Decode TinyURL.
    def __init__(self):
        self.count=0
        self.dmap={}
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        self.count+=1
        self.dmap[self.count]= longUrl
        return 'http://shortURL/'+str(self.count)


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        index = int(shortUrl.split('/')[-1])
        if index not in self.dmap:
            return ""
        return self.dmap[index]
    
    
        # the question is not clear. no mapping rule described
    def __init__(self):
        self._dict = {}
        self.key = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        txt = "tinyurl" + str(self.key)
        self._dict[txt] = longUrl
        self.key += 1
        return txt

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self._dict[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
