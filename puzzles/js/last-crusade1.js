function printNextRoom(roomType, x, y, entrance) {
  switch (roomType) {
    case 2: case 6:
      entrance === "LEFT" ? x++ : x--;
      break;
    case 4:
      entrance === "TOP" ? x-- : y++;
      break;
    case 5:
      entrance === "TOP" ? x++ : y++;
      break;
    case 10:
      x--;
      break;
    case 11:
      x++;
      break;
    default:
      y++;
  }
  print(x + " " + y);
}

let rooms = [];
let inputs = readline().split(' ');
const nbColumns = parseInt(inputs[0]);
let nbRows = parseInt(inputs[1]);
for (let i = 0; i < nbRows; i++) {
  let line = readline().split(' ').map(Number);
  rooms.push(line);
}
let exit = parseInt(readline());

// game loop
while (true) {
  let inputs = readline().split(' ');
  let x = parseInt(inputs[0]);
  let y = parseInt(inputs[1]);
  let entrance = inputs[2];
  printNextRoom(rooms[y][x], x, y, entrance);
}
