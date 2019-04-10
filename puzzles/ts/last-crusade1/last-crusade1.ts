function printNextRoom(roomType: number, x: number, y: number, entrance: string) {
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
  console.log(`${x} ${y}`);
}

let rooms: number[] = [];
let inputs: string[] = readline().split(' ');
const nbColumns: number = Number(inputs[0]);
const nbRows: number = Number(inputs[1]);
for (let i: number = 0; i < nbRows; i++) {
  let line = readline().split(' ').map(Number);
  rooms.push(line);
}
readline();

// game loop
while (true) {
  const inputs: string[] = readline().split(' ');
  const x: number = Number(inputs[0]);
  const y: number = Number(inputs[1]);
  const entrance: string = inputs[2];
  printNextRoom(rooms[y][x], x, y, entrance);
}
