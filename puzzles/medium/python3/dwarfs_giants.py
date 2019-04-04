class Person():
    def __init__(self, number):
        self.number = number
        self.depth = 1
        self.dwarfs = set()

    def add(self, dwarf):
        if dwarf not in self.dwarfs:
            self.dwarfs.add(dwarf)

    def update_depths(self):
        for dwarf in self.dwarfs:
            if self.depth >= dwarf.depth:
                dwarf.depth = self.depth + 1
                dwarf.update_depths()

    def __eq__(self, other):
        return self.number == other.number

    def __ne__(self, other):
        return self.number != other.number

    def __hash__(self):
        return self.number


persons = []
# The number of people involved in the longest succession of influences
max_depth = 0
nb_relations = int(input())  # the number of relationships of influence

for i in range(nb_relations):
    # a relationship of influence between two people
    x, y = [int(j) for j in input().split()]
    giant = Person(x)
    dwarf = Person(y)

    if giant in persons:
        giant = persons[persons.index(giant)]
    else:
        persons.append(giant)

    if dwarf in persons:
        dwarf = persons[persons.index(dwarf)]
    else:
        persons.append(dwarf)

    giant.add(dwarf)
    giant.update_depths()

for person in persons:
    max_depth = max(max_depth, person.depth)

print(max_depth)
