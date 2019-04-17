// Reference: https://en.wikipedia.org/wiki/Trie

class Vertice {
  children;
  value;

  constructor() {
    this.children = new Map(); // character => Vertice
    this.value = null;
  }
}

let root = new Vertice();
let size: number = 0;
const n: number = Number(readline());
for (let i: number = 0; i < n; i++) {
  const telephone = readline();
  
  let vertice = root;
  for (const char of telephone) {
    if (!vertice.children.has(char)) {
      let child = new Vertice();
      vertice.children.set(char, child);
      size += 1;
    }
    vertice = vertice.children.get(char);
  }
  vertice.value = telephone;
}

console.log(size);
