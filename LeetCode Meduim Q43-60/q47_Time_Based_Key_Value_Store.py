# https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:

    def __init__(self):
        self.keyTimeMap = defaultdict(list) # keys:[timestamps]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyTimeMap[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        # check if for key if there exists a timestamp that is <= the pssed in one, and if so
        # then return the item associate with it
        arr = self.keyTimeMap[key]
        n = len(arr)
        
        left = 0
        right = n
        
        while left < right:
            mid = left + (right-left) // 2
            if arr[mid][1] <= timestamp:
                left = mid + 1
            elif arr[mid][1] > timestamp:
                right = mid
        
        return "" if right == 0 else arr[right - 1][0]
        
        #the challenge here is checking if it exists or somethign that is <= exists in fast time
        # so since it is strictly ascending, we can do it in logn binary search or o(1) if we can find a way
        # to do so
    
    # since set in increasing we can rely on the fact that it is sorted already, so we could do binar
    # search on the index of value in the set to see if it exists or if there is a number before since
    # logn < n
    # we could also use a set if necessary

    # want to return -1 if there is nothig at or befire it 

    # [5,7,9] target = 3
    # would return 0 
    # [1,5,7,9] target = 3
    # would return 0 aswell
    # but if we add a -1 to it, it would return 1. ez

    # your idea of a dictionary and binary search is right but your code is spaghetti



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)