class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        d = list(dominoes)
        ptr1, ptr2 = 0, 0
        save = 0
        
        while ptr1 < n:
            if d[ptr1] == 'L':
                for k in range(save, ptr1):
                    d[k] = 'L'
                ptr1 += 1
            elif d[ptr1] == 'R':
                ptr2 = ptr1 + 1
                while ptr2 < n and d[ptr2] == '.':
                    ptr2 += 1
                
                if ptr2 == n:
                    for k in range(ptr1, ptr2):
                        d[k] = 'R'
                    return "".join(d)
                elif d[ptr2] == 'R':
                    for k in range(ptr1, ptr2):
                        d[k] = 'R'
                    ptr1 = ptr2
                elif d[ptr2] == 'L':
                    save = ptr2 + 1
                    ptr1 += 1
                    ptr2 -= 1
                    while ptr1 < ptr2:
                        d[ptr1] = 'R'
                        d[ptr2] = 'L'
                        ptr1 += 1
                        ptr2 -= 1
                    ptr1 = save
            else:
                ptr1 += 1
        return "".join(d)