class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        
        #dictionary of substrings to instances.
        dictionary = {}
        setA = set() #the minSize set with <=maxLetters
        
        for start in range(0,len(s)-minSize+1):
            setA.clear()
            #try andreach minSize&&maxLetters. if can't, then skip to next
            reached = True
            for length in range(0,minSize-1): #one off index
                setA.add(s[start + length])
                if len(setA) > maxLetters:  
                    reached = False
                    break
                    
            if reached == False: #if bare mininum not reached skip next line.
                continue
            #else: then check the length of the substring:
            
            for q in range(minSize-1, maxSize): #one off index
                if (start+q>=len(s)):
                    break
                #else
                setA.add(s[start+q])
                if len(setA) > maxLetters:
                    break
                else:
                    substr = s[start:start+q+1] #one off index
                    occurences = dictionary.get(substr)
                    if (occurences == None):
                        dictionary[substr] = 1
                    else:
                        dictionary[substr]+=1
                       
       
    
        #pick the max occurences
        max = 0
        for i in dictionary.values():
            if i>max:
                max = i

                
        return max
