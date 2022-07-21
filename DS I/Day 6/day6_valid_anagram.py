class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #if strings having different length of word they cant be Anagram So return False
        if len(s)!=len(t): 
            return False
        
        countS,countT = {},{} #creating two hashmaps for counting of words
        
        for i in range(len(s)): #iterating through any string
            #get function will helps to handle keyerror by passing default value as 0 
            countS[s[i]] = 1 + countS.get(s[i],0) 
            countT[t[i]] = 1 + countT.get(t[i],0)
        
        for c in countS: # here we used c as iterator 
            if countS[c] !=countT.get(c,0): #if counting of both string not equal return false
                return False
        
        return True #otherwise return True