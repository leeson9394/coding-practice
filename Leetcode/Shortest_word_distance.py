# Leetocde #243 Shortest Word Distance
import sys

def shortestDistance(words,word1,word2):
    idx1=-1
    idx2=-1
    distance=sys.maxint
    for i in xrange(len(words)):
        if word1 == words[i]:
            idx1 = i
            if idx2 != -1 :
                distance = min(abs(idx1 - idx2), distance)
        if word2 == words[i]:
            idx2 = i
            if idx1 != -1 :
                distance = min(abs(idx1 - idx2), distance)
    return distance


words = ["practice", "makes", "perfect", "coding", "makes","python"]
word1 = "makes"
word2 = "python"

print shortestDistance(words, word1, word2)