/**
 *
 * @param {Array<number>} array
 * @description An array is monotonic if it is either monotone increasing or monotone decreasing. An array is monotone increasing if all its elements from left to right are non-decreasing. An array is monotone decreasing if all  its elements from left to right are non-increasing. Given an integer array return true if the given array is monotonic, or false otherwise.
 * @returns {boolean}
 */
function monotonicArray(array: Array<number>): boolean {
  if (array[0] === array[array.length - 1]) {
    // Check if every item in the array is the same

    for (let i = 1; i < array.length - 1; i++) {
      if (array[i] !== array[0]) {
        return false;
      }
    }
  } else if (array[0] > array[array.length - 1]) {
    // Check for monotone decreasing

    for (let i = 0; i < array.length - 1; i++) {
      if (array[i] < array[i + 1]) {
        return false;
      }
    }
  } else {
    // Check for monotone increasing

    for (let i = 0; i < array.length - 1; i++) {
      if (array[i] > array[i + 1]) {
        return false;
      }
    }
  }

  return true;
}

console.log(monotonicArray([]));
console.log(monotonicArray([1]));
console.log(monotonicArray([1, 2, 3]));
console.log(monotonicArray([2, 2, 2, 1]));
console.log(monotonicArray([2, 2, 2, 5]));
console.log(monotonicArray([5, 4, 3, 2, 2, 2]));
console.log(monotonicArray([5, 4, 3, 2, 2, 2, 3]));
