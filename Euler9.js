var math = require('mathjs');

var p = 3;
var q = 1;

function a() {
  return p*q;
}
function b(){
  return (math.pow(p,2) - math.pow(q,2))/2;
}
function c(){
  return (math.pow(p,2) + math.pow(q,2))/2;
}

for(q = 1; q < 100; q++){
  for(p = 3; p < 100; p++) {
    var tSum = a()+b()+c();
    if(parseInt(tSum) == 1000){
      console.log(a());
      console.log(b());
      console.log(c());
      console.log('Product is: ' + a()*b()*c());
      p = 101
      q = 101;
    }
  }
}
