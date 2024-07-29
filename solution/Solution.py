from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ## Approach: dynamic programming. Time: O(n^2), Space: O(n)
        
        # Get the length of the rating array
        n = len(rating)
        
        # Initialize two dynamic programming arrays to store the counts of lower and upper ratings
        lower_dps = [0] * n
        upper_dps = [0] * n
        
        # Initialize the count of teams
        count = 0
        
        # Iterate through the rating array
        for i in range(n):
            # Iterate through the previous ratings
            for j in range(i):
                # Check if the current rating is greater than the previous rating
                if rating[j] < rating[i]:
                    # Increment the count by the number of upper ratings for the previous rating
                    count += upper_dps[j]
                    # Increment the upper rating count for the current rating
                    upper_dps[i] += 1
                else:
                    # Increment the count by the number of lower ratings for the previous rating
                    count += lower_dps[j]
                    # Increment the lower rating count for the current rating
                    lower_dps[i] += 1
        
        # Return the total count of teams
        return count