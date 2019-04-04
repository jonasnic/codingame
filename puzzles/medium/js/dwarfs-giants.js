class Person {
  constructor(id) {
    this.id = id; // constant unique id
    this.depth = 1; // distance to it's most ancient giant
    this.dwarfs = []; // unique persons influenced
  }

  // Add this person to the array of the unique persons influenced.
  add(dwarf1) {
    this.dwarfs.forEach(dwarf2 => {
      if (dwarf1.id === dwarf2.id)
        return;
    }); // forEach
    this.dwarfs.push(dwarf1);
  } // add()

  updateDepths() {
    this.dwarfs.forEach(dwarf => {
      if (this.depth >= dwarf.depth) {
        dwarf.depth = this.depth + 1;
        dwarf.updateDepths();
      } // if
    }); // forEach
  } // updateDepths()
} // Person

class Graph {
  constructor(nbRelations) {
    this.persons = [];
    this.nbRelations = nbRelations; // the number of relationships of influence
  }

  update(isGiant) {
    let id = isGiant ? this.giant.id : this.dwarf.id;
    this.persons.forEach(person => {
      if (person.id === id) {
        isGiant ? this.giant = person : this.dwarf = person;
        return;
      }
    }); // forEach
    this.persons.push(isGiant ? this.giant : this.dwarf);
  } // update()

  parseInput() {
    for (let i = 0; i < this.nbRelations; ++i) {
      let inputs = readline().split(' ');
      let x = parseInt(inputs[0]); // a relationship of influence between two people (giant x influences dwarf y)
      let y = parseInt(inputs[1]);
      this.giant = new Person(x);
      this.dwarf = new Person(y);

      this.update(true);
      this.update(false);

      this.giant.add(this.dwarf);
      this.giant.updateDepths();
    } // for
  } // parseInput()

  printMaxDepth() {
    let maxDepth = 0; // The number of people involved in the longest succession of influences
    this.persons.forEach(person => {
      maxDepth = Math.max(maxDepth, person.depth);
    }); // forEach
    print(maxDepth);
  } // printMaxDepth()
} // Person

let graph = new Graph(parseInt(readline()));
graph.parseInput();
graph.printMaxDepth();
