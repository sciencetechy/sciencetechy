"""
Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

Note that the word should be built from left to right with each additional character being added to the end of a previous word. 


"""

class Solution:
    def longestWord(self, words):
        p = []

        for i in words:
            p.append([i, len(i)])

        p.sort(key = lambda x : x[1])

        cnt = 2
        biggest = p[-1][0]
        f = False
        crr = biggest
        b = []
        cb = biggest
        a = 0
        le = 0
        longest = {}

        while not f:
            if len(crr) > 1:
                prev = crr[:-1]

                if prev in words:
                    crr = prev
                else:
                    if len(words)-cnt > 0:
                        biggest = p[len(p)-cnt][0]
                        crr = biggest
                        cnt += 1
                    else:
                        f = True


            else:
                if not longest:
                    cb = biggest
                    crr = cb
                    longest[len(cb)] = [cb]
                    le = len(cb)
                    biggest = p[len(p)-cnt][0]
                    crr = biggest
                    cnt += 1
                else:
                    if len(biggest) in longest.keys():
                        cb = biggest
                        crr = cb
                        l = longest[len(cb)]
                        l.append(cb)
                        longest[len(cb)] = l
                        biggest = p[len(p)-cnt][0]
                        crr = biggest
                        cnt += 1
                    else:
                        f = True

        if longest:
            t = longest[len(cb)]
            t.sort()
            return t[0]
        else:
            return ""