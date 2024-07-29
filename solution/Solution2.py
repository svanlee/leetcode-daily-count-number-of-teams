import bisect
from typing import List


class Solution:
    # Alternative solution for performance testing
    def numTeams(self, rating: List[int]) -> int:
        # Initialize an empty list to store the ratings in sorted order
        l = []
        
        # Create a sorted copy of the rating array
        sr = sorted(rating)
        
        # Create a dictionary to store the indices of the sorted ratings
        low = {}
        for idx, r in enumerate(sr):
            low[r] = idx
        
        # Initialize the result variable
        res = 0
        
        # Get the length of the rating array
        n = len(rating)
        
        # Iterate through the rating array
        for idx, r in enumerate(rating):
            # Find the insertion point of the current rating in the sorted list
            i = bisect.bisect(l, r)
            
            # Insert the current rating at the correct position in the sorted list
            l.insert(i, r)
            
            # Calculate the number of teams that can be formed with the current rating
            j = low[r] - i
            res += i * (n - 1 - idx - j) + j * (idx - i)
        
        # Return the total number of teams
        return res

    # Second solution
    def numTeams2(self, rating: List[int]) -> int:
        # Initialize the result variable
        ans = 0
        
        # Get the length of the rating array
        n = len(rating)
        
        # Iterate through the rating array
        for j in range(n):
            # Initialize variables to count the number of ratings less than and greater than the current rating
            llt, lgt = 0, 0
            
            # Count the number of ratings less than and greater than the current rating in the range [0..j)
            for i in range(j):
                llt += rating[i] < rating[j]
                lgt += rating[i] > rating[j]
            
            # Initialize variables to count the number of ratings less than and greater than the current rating
            rlt, rgt = 0, 0
            
            # Count the number of ratings less than and greater than the current rating in the range (j..n)
            for k in range(j + 1, n):
                rlt += rating[k] < rating[j]
                rgt += rating[k] > rating[j]
            
            # Calculate the number of teams that can be formed with the current rating
            ans += llt * rgt + lgt * rlt
        
        # Return the total number of teams
        return ans

    # Brute force solution (time limit exceeded)
    def numTeams1(self, rating: List[int]) -> int:
        # Initialize the result variable
        ans = 0
        
        # Get the length of the rating array
        n = len(rating)
        
        # Iterate through all possible combinations of three soldiers
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    # Check if the rating conditions are met
                    ans += 1 if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k] else 0
        
        # Return the total number of teams
        return ans