"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

class Solution:
    def groupAnagrams(self, strs):
        ss = []
        arr = []
        d = []
        cnt = 0
        k = False

        for i in strs:
            ss.append(''.join(sorted(i)))

        dictr = {ss[0]: "temp"}

        for i in strs:
            sr = ''.join(sorted(i))
            l = []
            l.append(i)

            if sr not in dictr:
                dictr[sr] = l
            else:
                l = dictr.get(sr)
                if l == "temp":
                    l = []
                l.append(i)
                dictr[sr] = l




        r = [*dictr.values()]
        
        return r