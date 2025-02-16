function orderedLinearSearch(array: Array<number>, value: number): number {
  // Time complexity => O(n)
  // Space complexity => O(1)

  for (let i = 0; i < array.length; i++) {
    if (array[i] === value) {
      return i;
    } else if (array[i] > value) {
      return -1;
    }
  }

  return -1;
}

console.log(orderedLinearSearch([1, 4, 2, 3, 4, 5, 6], 2));
