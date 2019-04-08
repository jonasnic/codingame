const nbElements: number = Number(readline()); // Number of elements which make up the association table.
const nbNames: number = Number(readline()); // Number of file names to be analyzed.
let table: object = {} // object to map file extensions to mime types
for (let i: number = 0; i < nbElements; i++) {
  const [extension, mimeType]: [string, string] = readline().split(' ');
  table[extension.toLowerCase()] = mimeType;
}

// For each of the filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
for (let i: number = 0; i < nbNames; i++) {
  const name: string = readline();
  const dotIndex: number = name.lastIndexOf('.');
  if (dotIndex === -1 || dotIndex === name.length - 1) {
    console.log("UNKNOWN");
  } else {
    const extension: string = name.substring(dotIndex + 1).toLowerCase();
    if (extension in table) {
      console.log(table[extension]);
    } else {
      console.log("UNKNOWN");
    }
  }
}
