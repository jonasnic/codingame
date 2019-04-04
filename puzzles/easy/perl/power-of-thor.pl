use strict;
use warnings;
use 5.20.1;

select(STDOUT); $| = 1; # DO NOT REMOVE

my $tokens;
chomp($tokens=<STDIN>);
my @line = split(/ /,$tokens);
my $light_x = int($line[0]);
my $light_y = int($line[1]);
my $thor_x = int($line[2]);
my $thor_y = int($line[3]);

# game loop
while (1) {
  my $direction = "";

  if ($thor_y > $light_y) {
    $direction .= "N";
    $thor_y -= 1;
  } elsif ($thor_y < $light_y) {
    $direction .= "S";
    $thor_y += 1;
  } 

  if ($thor_x > $light_x) {
    $direction .= "W";
    $thor_x -= 1;
  } elsif ($thor_x < $light_x) {
    $direction .= "E";
    $thor_x += 1;
  }

  # A single line providing the move to be made: N NE E SE S SW W or NW
  print "$direction\n";
}
