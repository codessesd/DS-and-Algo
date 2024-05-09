<?php

//bubble sort
function bubbleSort($arr)
{
  $counter = 0;
  $sorted = false;
  while (!$sorted) {
    $sorted = true;
    for ($i = 0; $i < count($arr) - 1; $i++) {
      if ($arr[$i] > $arr[$i + 1]) {
        $temp = $arr[$i];
        $arr[$i] = $arr[$i + 1];
        $arr[$i + 1] = $temp;
        $sorted = false;
        $counter++;
      }
    }
  }
  echo "Number of swaps: " . $counter . "\n";
  return $arr;
}


print_r(bubbleSort(['eeeeee', 'aaaa', 'bxs', 'c', 'd'])); //Works for strings
print_r(bubbleSort([16, 5, 3, 7, 9, 1, 32])); //Works for numbers

print_r([1, 2, 3, 4, 5, 6, 'one', 'two']);
