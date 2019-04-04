import sys

# dictionary to map file extensions to mime types
table = {}
nb_elements = int(input())
nb_names = int(input())
for i in range(nb_elements):
    extension, mime_type = input().split()
    table[extension.lower()] = mime_type

for i in range(nb_names):
    name = input().lower()
    dot_index = name.rfind(".")
    if dot_index == -1 or dot_index == len(name) - 1:
        print("UNKNOWN")
    else:
        extension = name[dot_index + 1:]
        try:
            print(table[extension])
        except KeyError:
            print("UNKNOWN")
