# Two pointer method #

class Solution:
    def findClosestElements(self, a: List[int], k: int, x: int) -> List[int]:
        out = []
        n = len(a)
        
        # Linear srch for the given number
        # If the number is not in the array, ptr will stop at value
        # just larger than the number
        def linSrch(num: int) -> int:
            nonlocal a
            ptr = 0
            while ptr < n - 1 and a[ptr] <= num:
                ptr += 1
            return ptr
        
        # Halt flags for left and right pointer
        rHalt, lHalt = False, False
        
        l = r = linSrch(x)
        # In case distance of a[l - 1] is less than or equal to the distance of a[l]
        if l - 1 >= 0:
            if abs(a[l - 1] - x) <= abs(a[l] - x):
                l = r = l - 1
        out.append(a[l])
        count = 1
        l -= 1
        r += 1
        if l < 0:
            lHalt = True
        if r >= n:
            rHalt = True
        
        while count < k:
            # If left or right pointer reaches end of array, remaining elements will be
            # selected using the other pointer
            if lHalt:
                while count < k:
                    out.append(a[r])
                    r += 1
                    if r == n:
                        count = k
                        break
                    count += 1
            elif rHalt:
                while count < k:
                    out.insert(0, a[l])
                    l -= 1
                    if l == -1:
                        count = k
                        break
                    count += 1
            else:
                dist1 = abs(a[l] - x)
                dist2 = abs(a[r] - x)
                if dist2 < dist1:
                    out.append(a[r])
                    r += 1
                    # Check if pointer reaches end of array
                    if r == n:
                        rHalt = True
                else:
                    out.insert(0, a[l])
                    l -= 1
                    # Check if pointer reaches end of array
                    if l < 0:
                        lHalt = True
                count += 1
                
        return out