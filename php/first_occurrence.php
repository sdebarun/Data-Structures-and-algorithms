<?php
/**
 * a use of hash map (or hash table)
 */
//given array [2,5,5,2,3,5,1,2,4]  should return 5
//given array [2,5,1,1,3,5,1,2,4]  should return 1,  
//given array [2,8,1,2,3,5,1,2,4]  should return 2
// given array [1,2,3,4,5,6,7,8,9]   should give undefined

$arr = [1,2,3,4,5,6,7,8,9];
function getFirstRecurringOccurenceNumber($arr){
    $assoc = [];
    for($i = 0; $i < count($arr); $i++){
        if($assoc[$arr[$i]]){ // isset will work too
            return $arr[$i];
        }else{
            $assoc[$arr[$i]] = true; 
        }
    }
    return 'undefined';
}

$start = microtime();
print_r(getFirstRecurringOccurenceNumber($arr));
$end = microtime() - $start;
echo $end;

//! if we assign $i it renders $assoc[2] = 0 for the first time. 
//! so when the second $assoc[2] comes through the loop it simply results 0. 
//! That inside of if statement becomes false asn 0 is treated as false. if ac
//* possible solution is use isset function to check if the key exists in the first place
//* or we can simply set true false or explicit zero and non zero values while assiging values
//* in the else part.
//? Note that if() only accepts 0 or non 0 value. So, it doesn't matter what assignment you made. if() will recieve the value of your variable 'a' as an argument and act accordingly. In this case, since the value of a is 0, the if part will not get executed and the system will jump to else