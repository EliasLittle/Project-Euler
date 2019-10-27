var sPrime = 10001;
var pset = [2];

function primeCheck(num) {
  for(var i = 2; i < num/2; i++){
    if(num % i === 0){
      return false;
    }
  }
  return true;
}

var q = 3;
function listxPrimes(given) {
  while(pset.length < given){
    if(primeCheck(q)){
      pset.push(q);
    }
    q += 2;
  }
}

listxPrimes(sPrime);

console.log(pset[sPrime-1]);
