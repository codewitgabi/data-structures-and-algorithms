/**
 *
 * @param array The array to be searched
 * @param value The value to be searched for
 * @returns The index of the value if found or -1 if not found
 */
function unorderedLinearSearch(array: Array<number>, value: number): number {
  // Time complexity => O(n)
  // Space complexity => O(1)

  for (let i = 0; i < array.length; i++) {
    if (array[i] === value) {
      return i;
    }
  }

  return -1;
}

console.log(unorderedLinearSearch([5, 3, 6, 2, 6, 1, 8], 2));
console.log(unorderedLinearSearch([5, 3, 6, 2, 6, 1, 8], 0));
