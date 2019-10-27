var math = require('mathjs');

var set = [2];

function primeCheck(num) {
  for(i = 2; i <= math.sqrt(num); i++){
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

listPrimes(2000000);

console.log(set.reduce(function(a,b){return a+b;}));
