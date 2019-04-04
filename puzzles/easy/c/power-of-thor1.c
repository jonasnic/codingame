#include <stdio.h>

int main() {
  int lightX; // the X position of the light of power
  int lightY; // the Y position of the light of power
  int x; // Thor's X position
  int y; // Thor's Y position
  scanf("%d%d%d%d", &lightX, &lightY, &x, &y);

  // game loop
  while (1) {
    // possible moves: N NE E SE S SW W or NW

    if (y > lightY) {
      printf("N");
      y--;
    } else if (y < lightY) {
      printf("S");
      y++;
    }

    if (x > lightX) {
      printf("W");
      x--;
    } else if (x < lightX) {
      printf("E");
      x++;
    }

    printf("\n");
  }

  return 0;
}
