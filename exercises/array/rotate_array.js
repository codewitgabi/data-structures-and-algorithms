// @ts-check

/**
 *
 * @param {Array<number>} array The array to be rotated
 * @param {number} d The number of times to rotate the array
 * @returns {Array<number>} The rotated array
 */
function rotate_array(array, d) {
  // Number of rotations

  for (let i = 0; i < d; i++) {
    // O(d)
    // Actual rotation of the array

    for (let i = 0; i < array.length - 1; i++) {
      // O(n)
      // Swap items

      let temp = array[i];
      array[i] = array[i + 1];
      array[i + 1] = temp;
    }
  }

  return array;
}

/**
 *
 * @param {Array<number>} array The array to be rotated
 * @param {number} d The number of times to rotate the array
 * @returns {Array<number>} The rotated array
 */
function better_rotate_array(array, d) {
  const arrayLength = array.length;

  if (d === arrayLength) {
    return array;
  }

  const output = new Array(arrayLength);

  if (d < arrayLength) {
    for (let i = d - 1; i > -1; i--) {
      output[arrayLength - (i + 1)] = array[i];
    }

    for (let i = d; i < arrayLength; i++) {
      output[i - d] = array[i];
    }
  } else {
    const n = d - arrayLength;

    for (let i = n - 1; i > -1; i--) {
      output[arrayLength - (i + 1)] = array[i];
    }

    for (let i = n; i < arrayLength; i++) {
      console.log({ i });
      output[d - (arrayLength + n)] = array[i];
    }
  }

  return output;
}

console.log(better_rotate_array([1, 2, 3, 4, 5], 8));
