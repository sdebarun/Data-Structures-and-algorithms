/**
 * finding the first occurence usning hash tables ort hash maps
 * 
 */
//given array [2,5,5,2,3,5,1,2,4] , should return 5
//given array [2,5,1,1,3,5,1,2,4], should return 1,  
//given array [2,8,1,2,3,5,1,2,4] should return 2
// given array [1,2,3,4,5,6,7,8,9]   should give undefined             

function firstOccurence(arr){
    let assoc = {};
    for(let i = 0; i< arr.length; i++ ){
        if(assoc[arr[i]] !== undefined){
            return arr[i];
        }else{
            assoc[arr[i]] = i;
        }
    }
    console.log(assoc);
    return undefined;
}

console.log(firstOccurence([2,5,5,2,3,5,1,2,4]));
// if(0){
//     console.log('I am falsy');
// }else{
//     console.log('fun time: if is falsy');
// }