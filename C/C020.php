<?php
    // 自分の得意な言語で
    // Let's チャレンジ！
    $input_line = fgets(STDIN);
    $input = explode(" ", $input_line);

    $m = $input[0];
    $p = $input[1];
    $q = $input[2];

    $a = $m-0.01*$m*$p;
    $b = $a-0.01*$a*$q;
    echo $b;


?>