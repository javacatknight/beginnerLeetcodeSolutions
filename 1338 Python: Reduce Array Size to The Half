class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        #hashmap/dictionary
        #greedy, remove the biggest elements and check
        
        
        #3 part solution:
        #1: make a dictionary of the occurences. so, 1 occurs 5 times, 2 occurs 2 times = {1: 5, 2: 2}
        
        dictionary = {}
        for i in arr:
            if (dictionary.get(i,0) == 0):
                dictionary[i] = 1
            else:
                dictionary[i] = dictionary[i]+1

         #2: least half the array must be removed
        length = len(arr)
        if (length%2 ==1):
            length = len(arr) +1
        #finally:
        length = length/2
        

        #3: sort the occurences by greatest to least and then loop and see how many you need
        keyslist = list(dictionary.values())
        keyslist.sort(reverse=True)
        count = 0
        sizeatm = 0
        for key in keyslist:
            sizeatm+= key
            count+=1
            if ( sizeatm>= length):
                return count
            
        return count
