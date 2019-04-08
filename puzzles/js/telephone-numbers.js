class Node {
  constructor(digit) {
    this.digit = digit;
    this.children = [];
  }

  indexOf(digit) {
    for (let i = 0; i < this.children.length; ++i) {
      let child = this.children[i];
      if (child.digit === digit) {
        return i;
      }
    }
    return -1;
  }

  addChild(digit) {
    let child = new Node(digit);
    this.children.push(child);
  }
}

let size = parseInt(readline()); // The number of telephone numbers.
let elements = 0; // The number of elements (referencing a number) stored in the structure.
let root = new Node(-1); // root node of all the telephone numbers

for (let i = 0; i < size; ++i) {
  let telephone = readline();
  let current = root;
  for (let j = 0; j < telephone.length; ++j) {
    let digit = parseInt(telephone.charAt(j));
    let index = current.indexOf(digit);
    if (index === -1) {
      current.addChild(digit);
      ++elements;
    }
    index = current.indexOf(digit);
    current = current.children[index];
  }
}

print(elements);
