class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        cnt = dict([])
        lr = list(ransomNote) # convert into str
        lm = list(magazine)  # convert into str
        for i in range(len(lm)):
            if lm[i] in cnt.keys():
                cnt[lm[i]] += 1 # count letter times
            else:
                cnt[lm[i]] = 1
        for i in range(len(lr)):  # check if letter times is able to construct ransomNote.
            if lr[i] not in cnt.keys() or cnt[lr[i]] == 0:
                return False
            cnt[lr[i]] -= 1
        return True