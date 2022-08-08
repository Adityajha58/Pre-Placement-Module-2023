class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        #Item index generation
        freq = dict()
        
        for i in range(len(S)):
            if S[i] in freq:
                freq[S[i]].append(i)
            else:
                freq[S[i]] = [i]
        
        intervals = []
        
        #Take first and last Index of Item
        for i in freq:
            intervals.append([freq[i][0], freq[i][len(freq[i])-1]])
        
        #Merge Intervals
        i = 1
        
        while i<len(intervals):
            
            if intervals[i-1][1]>= intervals[i][0]:
                intervals[i-1][0] = min(intervals[i-1][0], intervals[i][0])
                intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])

                intervals.pop(i)
            
            else:
                i+=1
                
        ans = []
        
        for i in range(len(intervals)):
            ans.append(intervals[i][1]-intervals[i][0]+1)
        
        
        return ans