function binarySearch(array: Array<number>, value: number): number {
  let leftPointer = 0;
  let rightPointer = array.length - 1;

  while (leftPointer <= rightPointer) {
    const mid = Math.floor((leftPointer + rightPointer) / 2);

    if (array[mid] === value) {
      return mid;
    } else if (array[mid] > value) {
      rightPointer = mid - 1;
    } else {
      leftPointer = mid + 1;
    }
  }

  return -1;
}

console.log(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 9));
console.log(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 0));
