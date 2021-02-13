<?php
    // 自分の得意な言語で
    // Let's チャレンジ！
    $input_line = fgets(STDIN);
    $tmp = explode(" ",$input_line);
    
    $type = $tmp[0];
    $Destination_distance = $tmp[1];
    $fare = 0;
    $cheapest_price = 5000;
    $Highest_price = 0;
    
    for($i=1; $i<=$type; $i++){
        $input_line = fgets(STDIN);
        $tmp = explode(" ",$input_line);
        
        
        ${"First_ride_distance_".$i} = $tmp[0];
        ${"First_fare_".$i} = $tmp[1];
        ${"Addition_distance_".$i} = $tmp[2];
        ${"Addition_fare_".$i} = $tmp[3];
        
        ${"fare_".$i} = 0;
        
        if(${"First_ride_distance_".$i} > $Destination_distance ){
            ${"fare_".$i} = ${"First_fare_".$i};
        }else{
            $distance = ${"First_ride_distance_".$i};
            ${"fare_".$i} = ${"First_fare_".$i};
            
            while($Destination_distance >= $distance){
                ${"fare_".$i} = ${"fare_".$i} + ${"Addition_fare_".$i};
                $distance = $distance + ${"Addition_distance_".$i};
            }
        }
        
        if($cheapest_price >= ${"fare_".$i}){
            $cheapest_price = ${"fare_".$i};
        }
        if($Highest_price < ${"fare_".$i}){
            $Highest_price = ${"fare_".$i};
        }
        
    }
    
    print_r($cheapest_price);
    print_r(" ");
    print_r( $Highest_price);


?>