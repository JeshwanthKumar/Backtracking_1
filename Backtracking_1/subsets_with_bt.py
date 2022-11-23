#Time_Complexity: O(n)
#Space_Complexity: O(n) - Recursive stack space

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums= nums #Initialize nums as nums
        self.result = []    #Initialize result as an empty array
        
        self.backtrack(0, [])   #Recursive function call with 0 as the starting index and an empty array which contains the subsets
        
        return self.result  #Return result
    
    
    def backtrack(self, pivot, path):   #Recursive fucntion with pivot as the index and path as an array that stores the subsets
        self.result.append(path[:])     #Append the path as a shallow copy to the result
        
        
        for i in range(pivot, len(self.nums)):  #Continue till the lenght of nums
            
            #action
            path.append(self.nums[i])   #Append the element into the path
            
            #recurs
            self.backtrack(i+1, path)   #Recursive call by incrementing the index and the path
            
            #backtrack
            path.pop()  #Pop the last element in the path which will remove the last element which is not choosen