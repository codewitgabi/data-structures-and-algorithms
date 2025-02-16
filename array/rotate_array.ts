/**
 *
 * @param array The array to be rotated
 * @param k The number of rotations to be performed
 * @returns The rotated array based on k
 */
function rotateArray(array: Array<number>, k: number): Array<number> {
  // Space complexity => O(n)
  // Time complexity => O(n)

  const arrayLength = array.length;
  const output = new Array(arrayLength);
  const kMod = k % arrayLength;

  // If array length is equal to k, no need for rotation

  if (arrayLength === k) {
    return array;
  }

  // Move the rotated part to the output array

  for (let i = kMod; i < arrayLength; i++) {
    output[i - k] = array[i];
  }

  for (let i = kMod - 1; i > -1; i--) {
    output[arrayLength - (kMod - i)] = array[i];
  }

  return output;
}

/**
 *
 * @param {Array<number>} array The array to be rotated
 * @param {number} k The number of times to rotate the array
 * @returns {Array<number>} The rotated array
 */
function naiveRotateArray(array: Array<number>, k: number): Array<number> {
  // Space complexity => O(1)
  // Time complexity => O(k * n)

  // Perform rotation k times

  for (let i = 0; i < k; i++) {
    // Perform actual rotation (rotate once)

    for (let j = 0; j < array.length - 1; j++) {
      // Swap elements

      let temp = array[j];
      array[j] = array[j + 1];
      array[j + 1] = temp;
    }
  }

  return array;
}
