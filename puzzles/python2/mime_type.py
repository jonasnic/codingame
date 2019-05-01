# dictionary to map file extensions to mime types
table = {}
nb_elements = int(raw_input())
nb_names = int(raw_input())
for _ in range(nb_elements):
    extension, mime_type = raw_input().split()
    table[extension.lower()] = mime_type

for _ in range(nb_names):
    name = raw_input().lower()
    dot_index = name.rfind(".")
    if dot_index == -1 or dot_index == len(name) - 1:
        print("UNKNOWN")
    else:
        extension = name[dot_index + 1:]
        try:
            print(table[extension])
        except KeyError:
            print("UNKNOWN")
