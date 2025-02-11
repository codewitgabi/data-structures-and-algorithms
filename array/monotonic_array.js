// @ts-check

/**
 *
 * @param {Array<number>} array
 * @description An array is monotonic if it is either monotone increasing or monotone decreasing. An array is monotone increasing if all its elements from left to right are non-decreasing. An array is monotone decreasing if all  its elements from left to right are non-increasing. Given an integer array return true if the given array is monotonic, or false otherwise.
 * @returns {boolean}
 */

const checkMonotonic = function (array) {
  // write code here to return either true or false

  const leftPointer = array[0];
  const lastPointer = array[array.length - 1];

  if (leftPointer === lastPointer) {
    for (let i = 0; i < array.length - 1; i++) {
      if (array[i] !== array[i + 1]) {
        return false;
      }
    }
  } else if (leftPointer > lastPointer) {
    // Monotone decreasing...

    for (let i = 0; i < array.length - 1; i++) {
      if (array[i] < array[i + 1]) {
        return false;
      }
    }
  } else {
    // Monotone increasing...

    for (let i = 0; i < array.length - 1; i++) {
      if (array[i] > array[i + 1]) {
        return false;
      }
    }
  }

  return true;
};

console.log(checkMonotonic([]));
console.log(checkMonotonic([1]));
console.log(checkMonotonic([1, 2, 3]));
console.log(checkMonotonic([2, 2, 2, 1]));
console.log(checkMonotonic([2, 2, 2, 5]));
console.log(checkMonotonic([5, 4, 3, 2, 2, 2]));
console.log(checkMonotonic([5, 4, 3, 2, 2, 2, 3]));
