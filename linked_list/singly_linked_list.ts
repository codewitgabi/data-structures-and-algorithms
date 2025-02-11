class DNode {
  public next: DNode | null;

  constructor(public data: number) {
    this.data = data;
    this.next = null;
  }
}

class LinkedList {
  public head: DNode | null;

  constructor() {
    this.head = null; // Root node
  }

  /**
   *
   * @param {number} data Number to be added at the end of the linked list
   * @description Adds a new node at the end of the linked list
   * @returns {void}
   */
  insertAtEnd(data: number): void {
    // Check if there is a head node

    if (!this.head) {
      this.head = new DNode(data);
    } else {
      // Since there is already a head node, go to the end of the link and point if to a new node

      let currentNode = this.head;

      while (currentNode.next) {
        currentNode = currentNode.next;
      }

      currentNode.next = new DNode(data);
    }
  }

  /**
   *
   * @param {number} data Number to be added at the end of the linked list
   * @description Adds a new node at the beginning of the linked list
   * @returns {void}
   */
  insertAtBeginning(data: number): void {
    // Check if there is a head node

    if (!this.head) {
      this.head = new DNode(data);
    } else {
      // Create a new node

      const newNode = new DNode(data);
      const currentHeadNode = this.head;

      // We can now either swap the data or swap the nodes

      this.head = newNode;
      this.head.next = currentHeadNode;
    }
  }

  /**
   *
   * @param {number} data Number to be inserted to the linked list
   * @param {number} n The position at which the data is to be inserted
   * @returns {void}
   */

  insertAtN(data: number, n: number): void {
    let currentIndex = 0;
    // Check if there is a head node

    if (!this.head) {
      this.head = new DNode(data);
    } else {
      let currentNode: DNode | null = this.head;
      let nextNode = this.head.next;

      if (currentIndex === 0) {
        // Insert at first position (rewrite or call the `InsertAtBeginning` method)

        const newNode = new DNode(data);

        newNode.next = this.head;
        this.head = newNode;
        return;
      }

      while (currentNode) {
        currentIndex++;

        if (currentIndex === n) {
          const newNode = new DNode(data);
          currentNode.next = newNode;
          newNode.next = nextNode;
        }

        currentNode = currentNode.next;
        nextNode = currentNode?.next ?? null;
      }
    }
  }

  /**
   * @description Remove the last element from a linked list
   */
  delete() {
    // Check if there is a head node

    if (!this.head) {
      return;
    }

    // Check if only one item in the link3ed list, remove head node

    if (!this.head.next) {
      this.head = null;
      return;
    }

    // Perform actual node deletion

    let currentNode: DNode | null = this.head;
    let previousNode: DNode | null = this.head;

    while (currentNode.next) {
      previousNode = currentNode;
      currentNode = currentNode.next;
    }

    currentNode = null;
    previousNode.next = null;
  }

  /**
   * @description Logs all items in the linked list to the console
   * @returns {void}
   */
  display(): void {
    let currentNode = this.head;
    let repr = "";

    while (currentNode) {
      repr += `${currentNode.data} -> `
      currentNode = currentNode.next;
    }

    repr += "null";

    console.log(repr)
  }

  /**
   * @returns {number} The total length of the linked list
   */
  length(): number {
    let currentNode = this.head;
    let total = 0;

    while (currentNode) {
      total++;
      currentNode = currentNode.next;
    }

    return total;
  }

  /**
   * @param {number} data
   * @returns {number} The index of the data if found or -1
   */

  search(data: number): number {
    let currentNode = this.head;
    let index = 0;

    while (currentNode) {
      if (currentNode.data === data) {
        return index;
      }

      index++;
      currentNode = currentNode.next;
    }

    return -1;
  }

  /**
   * @returns {boolean} Whether the linked list is empty or not
   */
  isEmpty(): boolean {
    return this.head ? false : true;
  }

  /**
   * @description Empty the linked list
   * @returns {void}
   */

  empty(): void {
    this.head = null;
  }

  /**
   * @description Reverse a singly linked list
   * @returns {void}
   */

  reverse(): void {
    // Check if the linked list has a head node

    if (!this.head || this.head.next === null) {
      return;
    }

    let prevNode = null;
    let curNode: DNode | null = this.head;
    let nextNode = curNode.next;

    while (curNode?.next) {
      curNode.next = prevNode;
      prevNode = curNode;
      curNode = nextNode;
      nextNode = curNode?.next ?? null;
    }

    this.head = curNode;

    if (this.head) {
      this.head.next = prevNode;
    }
  }

  /**
   * @description  Given the head of a singly linked list, swap every two nodes and return its head.  For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
   */

  swapNodes(): void {
    let currentNode = this.head;
    let index = 0;

    while (currentNode) {
      if (index % 2 === 0) {
        const currentNodeData = currentNode.data;
        const nextNodeData = currentNode.next?.data;

        // Swap if there is a next node (In a case of even length). Odd length is left unswapped

        if (currentNode.next) {
          currentNode.data = nextNodeData as number;
          currentNode.next.data = currentNodeData;
        }
      }

      index++;
      currentNode = currentNode.next;
    }
  }
}
