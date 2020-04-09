if __name__ == "__main__":
    trie = {}
    nb_elements = 0  # number of elements (referencing a number) stored in the structure
    n = int(input())
    for i in range(n):
        current_node = trie
        phone_number = input()
        for digit in phone_number:
            if digit in current_node:
                current_node = current_node[digit]
            else:
                current_node[digit] = {}
                current_node = current_node[digit]
                nb_elements += 1
    
    print(nb_elements)
