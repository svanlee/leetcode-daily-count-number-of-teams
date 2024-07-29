// numTeams.ts
/**
 * Function to calculate the number of teams that can be formed from a given rating array.
 * A team consists of three elements in increasing or decreasing order.
 * 
 * @param rating The input rating array
 * @returns The total count of teams that can be formed
 */
function numTeams(rating: number[]): number {
    // Get the length of the rating array
    let n = rating.length;
    
    // If there are less than 3 elements, no teams can be formed
    if (n < 3) return 0;

    // Initialize two arrays to keep track of increasing and decreasing pairs
    let increasing = new Array(n).fill(0);
    let decreasing = new Array(n).fill(0);
    
    // Initialize the result variable to store the total count of teams
    let result = 0;

    // Iterate through the rating array
    for (let j = 0; j < n; j++) {
        // Iterate through the elements before the current element
        for (let i = 0; i < j; i++) {
            // If the current element is greater than the previous element, it's an increasing pair
            if (rating[i] < rating[j]) {
                // Increment the increasing count for the current element
                increasing[j]++;
                // Add the increasing count of the previous element to the result
                result += increasing[i];
            }
            // If the current element is less than the previous element, it's a decreasing pair
            else if (rating[i] > rating[j]) {
                // Increment the decreasing count for the current element
                decreasing[j]++;
                // Add the decreasing count of the previous element to the result
                result += decreasing[i];
            }
        }
    }

    // Return the total count of teams
    return result;
}