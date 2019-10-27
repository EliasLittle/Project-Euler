var math = require('mathjs');

var num = 1;
var nxtNum = 2;
var divisors = 0; //# of divisors

 while(divisors < 500){
  divisors = 0;
  for(q = 0; q < math.sqrt(num); q++){ //finds # divisors of number
    if(q < math.sqrt(num)){
      if(num % q === 0){
        divisors += 2;
      }
    }else {
      if(num % q === 0){
        divisors += 1;
      }
    }
  }
  if(divisors > 500){
    console.log(num);
  }

  num += nxtNum;
  nxtNum++;
}
