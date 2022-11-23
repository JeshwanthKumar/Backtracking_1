#Time_Complexity: O(n)
#Space_Complexity: O(n) - Recursive stack space

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result  = []      #Initialize result as an empty array
        self.backtrack(candidates, target, 0, [])   #Recursive function call with candidates, target, starting index as 0, and an array to store the combinations
        
        return self.result  #Resturn result
    
    def backtrack(self, candidates, currSum, i, path): #Recursive function with candidates, currSum, index as i, and path as an array to store the combinations
        if currSum == 0:    #If the currSum is 0 append the path as a shallow copy into the result and return which unfolds the recursion
            self.result.append(path[:])
            return
        
        if currSum < 0 or i == len(candidates): #If the currSum is less than 0 and i is equal to lenght of candidates return
            return
        
        #logic
        #Nochoose
        self.backtrack(candidates, currSum, i+1, path[:])   #Recursive call by not choosing that element and incrementing the index by 1
        
        
        path.append(candidates[i])  #Append the element into the path
        #Choose
        self.backtrack(candidates, currSum-candidates[i], i, path[:])   #Recursive call by choosing that element and incrementing the index by 1