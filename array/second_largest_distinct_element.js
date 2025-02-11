// @ts-check

/***
 * @param {Array<number>} array
 * @returns {number} Returns -1 if first and second largest elements are the same. Otherwise returns the second largest element
 */
function secondLargestDistinctElement(array) {
  let largest = array[0];
  let secondLargest = largest;

  // Check if array is empty

  if (array.length === 0) return -1;

  for (let i = 0; i < array.length; i++) {
    if (array[i] > largest) {
      secondLargest = largest;
      largest = array[i];
    } else if (array[i] < largest && array[i] > secondLargest) {
      secondLargest = array[i];
    }
  }

  if (largest === secondLargest) {
    return -1;
  }

  return secondLargest;
}

console.log(secondLargestDistinctElement([10, 10, 10]));
console.log(secondLargestDistinctElement([12, 35, 1, 10, 34, 1]));
console.log(secondLargestDistinctElement([]));
console.log(secondLargestDistinctElement([10, 5, 10]));
console.log(secondLargestDistinctElement([5, 10, 10]));
