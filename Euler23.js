var math = require('mathjs');

var abNums = [];
var nonAbSumNums = [];

function factor(x) {
  var divisors = [];

  var largest = int(math.sqrt(x));
  if(largest * largest != x){
    largest += 1;
  }

  for(int i = 1; i <= largest; i++){
    if(x%i = 0){
      divisors.push(i);
      divisors.push(x/i);
    }
  }

  return divisors;
}

function abundantCheck(n) {
  var total = 0;
  for(var i in arr){
    total += n[i];
  }

  if(total > n){
    abNums.push(n);
  }
}

function abSumCheck(arg) {
  var total = 0;
    for(var i in abNums){

    }
}

for(var i=1; i < 28124; i++){
  abundantCheck(i);
}

for(var i=23; i < 28123; i++){
  abSumCheck(i);
}
