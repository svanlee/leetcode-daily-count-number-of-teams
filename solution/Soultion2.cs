public class Solution
{
    public int NumTeams(int[] rating)
    {
        int n = rating.Length;
        int count = 0;
        
        // Iterate through the rating array, considering each element as the middle element of a team
        for (int j = 1; j < n - 1; j++) {
            int leftLess = 0, leftGreater = 0;  // count of elements less than and greater than rating[j] to the left
            int rightLess = 0, rightGreater = 0;  // count of elements less than and greater than rating[j] to the right
            
            // Calculate the counts of elements to the left of rating[j]
            for (int i = 0; i < j; i++) {
                if (rating[i] < rating[j]) leftLess++;  // increment leftLess if rating[i] is less than rating[j]
                if (rating[i] > rating[j]) leftGreater++;  // increment leftGreater if rating[i] is greater than rating[j]
            }
            
            // Calculate the counts of elements to the right of rating[j]
            for (int k = j + 1; k < n; k++) {
                if (rating[k] > rating[j]) rightGreater++;  // increment rightGreater if rating[k] is greater than rating[j]
                if (rating[k] < rating[j]) rightLess++;  // increment rightLess if rating[k] is less than rating[j]
            }
            
            // Calculate the number of teams that can be formed with rating[j] as the middle element
            count += leftLess * rightGreater + leftGreater * rightLess;
        }
        
        return count;
    }
}