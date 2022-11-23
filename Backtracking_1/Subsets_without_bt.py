#Time_Complexoty: O(n)
#Space_Complexity: O(n) - Recursive stack space

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums    #Initialize nums as nums
        self.result = []    #Initialize result as an empty array
        self.backtrack(0, [])   #Recursive function call

        return self.result  #Return the result
        
        
    def backtrack(self, i, subset): #Recursive function with i and subset
        #Base condition
        if i == len(self.nums): #If i is equal to the lenght of nums then append that subset into the result adn return which unfolds the recursion
            self.result.append(subset)
            return
            
        #Logic
        #No choose
        self.backtrack(i+1, subset[:])  #Recursive call by not choosing increment the index and add a shallow copy of the subset
        
        subset.append(self.nums[i]) #Append the elements of that index into the subset array
        
        #Choose
        self.backtrack(i+1, subset[:])  #ERecursive call by choosing that element incrementing the index and add a shallow copy of the subset array