# In this problem we will use two pointer method.

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        # We need to convert string to list of characters since we cannot assign value to a position in
        # string.
        d = list(dominoes)
        ptr1, ptr2 = 0, 0
        save = 0
        
        while ptr1 < n:
            if d[ptr1] == 'L':
                # If L is found, all '.' between the last save position and the new L position 
                # will be made an L
                for k in range(save, ptr1):
                    d[k] = 'L'
                ptr1 += 1
            elif d[ptr1] == 'R':
                ptr2 = ptr1 + 1
                while ptr2 < n and d[ptr2] == '.':
                    ptr2 += 1
                
                if ptr2 == n:
                    # If ptr2 reaches end with no R or L in the way, we replace all .'s b/w
                    # ptr1 and ptr2 with R and return the modified string
                    for k in range(ptr1, ptr2):
                        d[k] = 'R'
                    return "".join(d)
                elif d[ptr2] == 'R':
                    # If ptr2 finds an R we convert all .'s b/w ptr1 and ptr2 to R
                    for k in range(ptr1, ptr2):
                        d[k] = 'R'
                    ptr1 = ptr2
                elif d[ptr2] == 'L':
                    # If L is found after an R we convert '.' to L and R in sequence until we
                    # get an "LR" or "L.R"
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