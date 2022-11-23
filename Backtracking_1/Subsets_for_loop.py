#Time_Complexity: O(n)
#Space_Complexity: O(1)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]      #Initialize result as an empty array of arrays
        
        for num in nums:    #Continue till the last element in nums
            size = len(result)  #Size is the length of the result
            
            for i in range(size):   #Continue till the size
                temp = result[i][:] #Copy result into tmep as a shallow copy which only has the value
                temp.append(num)    #Append the num into temp
                result.append(temp) #Append the temp into result which will give the final output
                
                
        return result   #Returns all the subsets