#Time_Complexity: O(n)
#Space_Complexity: O(n) - Recursive stack space

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []    #Initialize result as an empty array
        self.backtrack(candidates, target, 0, [])   #Recursive function call with candidates, target, starting index as 0, and an empty array
        
        return self.result  #Return result
    
    
    def backtrack(self, candidates, currSum, pivot, path):  #Recursive function with candidates, currSum, index as i, and path as an array to store the combinations
        #base condition
        if currSum == 0:    #If the currSum is 0 append the path as a shallow copy into the result and return which unfolds the recursion
            self.result.append(path)
            return
        
        if currSum < 0: #If the currsum is less than 0 return
            return 
        
        for i in range(pivot, len(candidates)): #Continue till the lenght of the candidates
            #action
            path.append(candidates[i])  #Append the element in candidates into path
            #recurse
            self.backtrack(candidates, currSum-candidates[i], i, path[:])   #Recursive function call by subtracting currSum with the element of candidates and a shallow copy of path
            #backtrack
            path.pop()  #Pop the element in path which removes the last element which is not choosen