class Node {
    constructor(data) {
      this.data = data;
      this.left = null;
      this.right = null;
    }
  }
  
  class BinarySearchTree {
    constructor() {
      this.root = null;
    }
  
    insert(data) {
      if (this.root === null) this.root = new Node(data);
      else this.#insert(this.root, data);
    }
  
    #insert(node, data) {
      if (node === null) {
        return new Node(data);
      }
  
      if (data <= node.data) {
        node.left = this.#insert(node.left, data);
      } else {
        node.right = this.#insert(node.right, data);
      }
  
      return node;
    }
  
    inorderTraversal() {
      this.#inorderTraversal(this.root);
    }
  
    #inorderTraversal(node) {
      if (node === null) {
          return;
      }
  
      this.#inorderTraversal(node.left)
      console.log(node.data)
      this.#inorderTraversal(node.right)
    }
  }
  
  let tree = new BinarySearchTree();
  
  tree.insert(tree, 30);
  tree.insert(tree, 25);
  tree.insert(tree, 40);
  tree.insert(tree, 15);
  tree.insert(tree, 20);
  tree.insert(tree, 10);
  tree.insert(tree, 5);
  
  tree.inorderTraversal()
  