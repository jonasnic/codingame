use strict;
use warnings;
use 5.20.1;

select(STDOUT); $| = 1; # DO NOT REMOVE

chomp(my $width = <STDIN>);
chomp(my $height = <STDIN>);
chomp(my $text = <STDIN>);
for my $i (0..$height-1) {
  chomp(my $row = <STDIN>);
  my $output = "";
  for my $j (0..(length($text)-1)) {
    my $character = uc substr($text, $j, 1);
    my $position = ord($character) - ord('A');
    if ($position < 0 || $position > 25) {
      $position = 26;
    }
    my $start = $position * $width;
    $output .= substr($row, $start, $width);
  }
  print "$output\n";
}
