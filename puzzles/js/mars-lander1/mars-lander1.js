/* jshint esversion: 6 */

const surfaceN = parseInt(readline()); // the number of points used to draw the surface of Mars.
for (let i = 0; i < surfaceN; ++i) {
  readline();
}

// game loop
while (true) {
  let inputs = readline().split(' ');
  let vSpeed = parseInt(inputs[3]); // the vertical speed (in m/s), can be negative.
  let power = parseInt(inputs[6]); // the thrust power (0 to 4).
  let angle = 0;
  if (vSpeed <= -40) {
    power = 4;
  } else {
    power = 0;
  }
  print(angle + " " + power);
}
