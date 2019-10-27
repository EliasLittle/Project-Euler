var math = require('mathjs');

var set = [2];
var pset = [];

function primeCheck(num) {
  for(var i = 2; i < num; i++){
    if(num % i === 0){
      return false;
    }
  }
  return true;
}

function listPrimes(given) {
  for(var q = 3; q < given; q += 2){
    if(primeCheck(q)){
      set.push(q);
    }
  }
}


function test(given){
  for(var k = 0; k < set.length; k++){
    if(given % set[k] === 0){
      pset.push(set[k]);
    }
  }
  console.log(pset);
}


listPrimes(1E4);
test(600851475143);
