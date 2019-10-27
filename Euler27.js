var math = require('mathjs');

function f(a,b,n) {
  return n^2 + a*n + b;
}
function isPrime(x) {
  if(x == 2){return true;}
  if(x == 3){return true;}
  if(x%2 == 0){return false;}
  if(x%3 == 0){return false;}

  var i = 5
  var w = 2
  while(i*i <= x){
    if(x%i == 0){return false;}
    i+=w;
    w=6-w;
  }
  return true;
}

var largeA = 0;
var largeB = 0;
var mostPrimes = 0;

for(var a = 0; a < 100; a++){
  for(var b = 0; b <= 100; b++){
    var limit = 0
    if(math.abs(a) >= math.abs(b)){
      limit = math.abs(a);
    }else{
      limit = math.abs(b);
    }
    var n = 0;
    var allPrimes = true;

    while(allPrimes){
      if(isPrime(math.abs(f(a,b,n))) ){
        n++;
      }else{
        allPrimes = false;
      }
    }
    if(n>mostPrimes){
      mostPrimes = n;
      largeA=a;
      largeB=b;
      console.log(""+mostPrimes+" A: "+largeA+" B: "+largeB);
    }
  }
}
