public class Solution {
    public int NumTeams(int[] rating) {
        int n = rating.Length;
        
        // Initialize four arrays to store the counts of smaller and larger elements
        int[] smallerLeft = new int[n];  // count of smaller elements to the left
        int[] largerLeft = new int[n];  // count of larger elements to the left
        int[] smallerRight = new int[n];  // count of smaller elements to the right
        int[] largerRight = new int[n];  // count of larger elements to the right

        // Iterate through the rating array to populate the count arrays
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (rating[j] < rating[i]) {
                    // If rating[j] is smaller, increment smallerLeft[i] and largerRight[j]
                    smallerLeft[i]++;
                    largerRight[j]++;
                } else {
                    // If rating[j] is larger, increment largerLeft[i] and smallerRight[j]
                    largerLeft[i]++;
                    smallerRight[j]++;
                }
            }
        }

        // Calculate the total count of teams
        int count = 0;
        for (int i = 0; i < n; i++) {
            // For each element, add the product of smallerLeft and largerRight, and largerLeft and smallerRight
            count += smallerLeft[i] * largerRight[i] + largerLeft[i] * smallerRight[i];
        }

        return count;
    }
}