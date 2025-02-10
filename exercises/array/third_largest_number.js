/**
 * @param {Array<number>} array
 * @returns {number}
 */
function naive_third_largest_number(array) {
  if (array.length < 3) {
    return -1;
  }

  // Sort the array O(n**2)

  for (let i = 0; i < array.length - 1; i++) {
    for (let j = 0; j < array.length - i; j++) {
      if (array[j] < array[j + 1]) {
        // Swap elements

        let temp = array[j];
        array[j] = array[j + 1];
        array[j + 1] = temp;
      }
    }
  }

  return array[2];
}

/**
 * @param {Array<number>} array
 * @returns {number}
 */
function effective_third_largest_number(array) {
  if (array.length < 3) {
    return -1;
  }

  let largest = array[0];
  let secondLargest = -10000000
  let thirdLargest = -100000000;

  for (let i = 1; i < array.length; i++) {
    if (array[i] > largest) {
      thirdLargest = secondLargest;
      secondLargest = largest;
      largest = array[i];
    } else if (array[i] > secondLargest) {
      thirdLargest = secondLargest;
      secondLargest = array[i];
    } else if (array[i] > thirdLargest) {
      thirdLargest = array[i];
    }
  }

  return thirdLargest;
}

console.log(effective_third_largest_number([1, 2, 3, 5, 0]));
console.log(effective_third_largest_number([2, 1, 5, 0]));
console.log(effective_third_largest_number([]));
console.log(effective_third_largest_number([19, -10, 20, 14, 2, 16, 10]));
console.log(effective_third_largest_number([1, 14, 2, 16, 10, 20]));
console.log(effective_third_largest_number([0, -2, -2, -5, -8, 10]));
