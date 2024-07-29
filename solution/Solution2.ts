// numTeams.ts
/**
 * Function to calculate the number of teams that can be formed from a given rating array.
 * A team consists of three elements in increasing or decreasing order.
 * 
 * @param rating The input rating array
 * @returns The total count of teams that can be formed
 */
function numTeams(rating: number[]): number {
    // Initialize a variable to store the total count of teams
    let count = 0;
    
    // Get the length of the rating array
    const n = rating.length;
    
    // Iterate through the rating array
    for (let j = 0; j < n; j++) {
        // Initialize variables to store the count of less and more ratings on the left and right sides
        let leftLess = 0, leftMore = 0, rightLess = 0, rightMore = 0;
        
        // Iterate through the elements before the current element (left side)
        for (let i = 0; i < j; i++) {
            // If the current element is greater than the previous element, increment the leftLess count
            // This means the previous element is less than the current element
            if (rating[i] < rating[j]) leftLess++;
            // If the current element is less than the previous element, increment the leftMore count
            // This means the previous element is more than the current element
            if (rating[i] > rating[j]) leftMore++;
        }
        
        // Iterate through the elements after the current element (right side)
        for (let k = j + 1; k < n; k++) {
            // If the current element is greater than the next element, increment the rightLess count
            // This means the next element is less than the current element
            if (rating[k] < rating[j]) rightLess++;
            // If the current element is less than the next element, increment the rightMore count
            // This means the next element is more than the current element
            if (rating[k] > rating[j]) rightMore++;
        }
        
        // Calculate the count of teams that can be formed with the current element as the middle element
        // This is done by multiplying the count of less ratings on the left with the count of more ratings on the right
        // and adding the count of more ratings on the left with the count of less ratings on the right
        // This represents the number of teams that can be formed with the current element as the middle element
        count += leftLess * rightMore + leftMore * rightLess;
    }
    
    // Return the total count of teams
    return count;
}