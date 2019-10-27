var set = [0,1];
var total = 0;
var i = 2;

while(set[i-1] < 4000000){
  set.push(set[i-1]+set[i-2]);
  //console.log(set[i-1]);
  if(set[i] % 2 === 0){
    total += set[i];
  }
  i++;
}

console.log("Total is " + total);
