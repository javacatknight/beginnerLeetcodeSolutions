class Solution:
    def isPalindrome(self, s: str) -> bool:
        #two pointer strategy 
        #have one pointer one end, have one on the other end. move towards each other as required.
        #if non-numeric, ignore that char and move on to the next
        
        
        pointOne = 0
        pointTwo = len(s)-1
        
        while (pointOne < pointTwo):
            #if non-alphanumeric, remove;
            if not s[pointOne].isalnum():
                pointOne+=1
                continue
                
            if not s[pointTwo].isalnum():
                pointTwo-=1
                continue
                
            if s[pointOne] == s[pointTwo] or s[pointOne].upper() == s[pointTwo].upper(): #checks ignore case
                pointOne+=1
                pointTwo-=1
            else:
                return False
        return True
            
