# Number of Occurrences of a Number in a Sorted Array
def countFreq(self, arr, target):
    def start(arr):
        low = 0
        high = len(arr) - 1
        start = -1
            
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                start = mid
                high = mid - 1
            elif arr[mid] < target:
                low = mid + 1
            else: 
                high =  mid -1
        return start
        
            
    def end(arr):
        low = 0
        high = len(arr) - 1
        end = -1
            
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                end = mid
                low = mid + 1
            elif arr[mid] < target:
                low = mid + 1
            else: 
                high =  mid -1
        return end

    x = start(arr)

    if x == -1:
        return 0
        
    y = end(arr)
    
    return y - x + 1

# TC - O(log n)
# SC - O(1)