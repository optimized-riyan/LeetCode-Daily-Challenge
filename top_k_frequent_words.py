# Use map(a.k.a. dictionary in Python) #

from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # For sorting tuples we define "key" functions
        def second(n):
            return -n[1]
        def first(n):
            return n[0]
        
        record = Counter(words)
        records = sorted([(key, record[key]) for key in record.keys()], key = second)
        n = len(records)
        
        i = 0
        j = 0
        # to sort lexicographically
        while j < k:
            j = i + 1
            while j < n and records[i][1] == records[j][1]:
                j += 1
            if j > i + 1:
                records = records[:i] + sorted(records[i:j], key = first) + records[j:]
            i = j
        
        print(records)
        return [word[0] for word in records[:k]]